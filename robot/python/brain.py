import threading
import math
import util
from queue import QueueFactory
from moving import Move
import time
 
class Brain(threading.Thread):
      def __init__(self,debug, show_contour, blink_time):
          super(Brain,  self ).__init__(name = "Brain")
          self.frameQueue = None
          self.feetCommandQueue = None
          self._debug_mode = debug
          self._last_time = time.time()
          self._blink_time = blink_time
          self._show_contour = show_contour

      def setQueue(self, qName, queue ):
          if qName in dir(self):
             setattr(self, qName, queue)
          else:
             print "Queue name not found", qName

      def run(self):
          while True:
             duration, updatedTime = util.get_duration_timestamp( self._last_time )
             frame = self._getFrame()
             if duration >= self._blink_time and not self._debug_mode and frame:
                self._last_time = updatedTime
                self._wayToGoBydrawContours(frame)             
             
      def _getFrame(self):
          if not self.frameQueue.isEmpty():
             item = self.frameQueue.get()
             return item
          return None
              
      def feetControl(self, *par):
          move = Move()
          if par[0] in dir(move):
              tmp = list(par)
              cmd = tmp.pop(0)
              par = tuple(tmp)
              getattr(move, cmd)( *par )
              self.feetCommandQueue.put(move)
          else:
              print 'No feet command', par[0] 

      def _wayToGoBydrawContours(self, frame): 
          if not frame:
             print "No Frame"
             return
          contours = Contours(frame)
          self.feetControl(*contours.runSteps())
          if self._show_contour:
             contours._contour.showFrame()

class Contours:
      def __init__(self, frame):
          self._forwardMargen = 10
          self._centralMargen = 5
          self._frame = frame
          self._steps = []
          self._return = None
          self._contourColor = (0, 255 , 0)     
          self._contour = None
          self._high = 0
          self._weight = 0
          self._mid = 0
          self._breakStepRun = False
          self._bottonLine = []
          self._candidatePosition = []
          self._finalPosition = self._mid
          self._movingPar = ('stop')
          self.setSteps()

      def runSteps(self):
          for step in self._steps:
              print ">>>>",step
              if self._breakStepRun:
                 break
              getattr(self,step)()          
          return self._movingPar

      def setSteps(self):  
          self._steps = ['setupContour', 
                          'findButtonLine',
                          'isOnTheWay',
                          'getFarthestPosition',
                          'findNearestPosition',
                          'generateMovingPar']

      def setupContour(self):
          self._contour = self._frame.applyProcessToFrame("drawContours", self._contourColor)
          self._high, self._weight, channels = self._contour.frame.shape 
          self._mid = self._weight/2           

      def findButtonLine(self):
          contourImg = self._contour.frame
          for w in range(self._weight):
              if list(contourImg[self._high-1][w]) == list(self._contourColor):
                 self._bottonLine.append(w)

      def isOnTheWay(self):
          if len([ p for p in self._bottonLine if math.fabs( p - self._mid ) < self._centralMargen ]) == 0 :
             self._candidatePosition = self._bottonLine
             self._steps.remove('getFarthestPosition')

      def getFarthestPosition(self):
          high_set = []
          contourImg = self._contour.frame
          for p in self._bottonLine:
              h_anchor = self._high - 6
              while not h_anchor < 0:
                    if list(contourImg[h_anchor][p]) == list(self._contourColor) or h_anchor == 0 :
                       #print "BBBBBBBBBb",(p, h_anchor)
                       high_set.append((p, h_anchor))
                       break
                    h_anchor = h_anchor - 1
          sorted_position = sorted( high_set, key = lambda x:x[1] )
          self._candidatePosition = [ p[0] for p in sorted_position if p[1] == sorted_position[1][1] ]
         
      def findNearestPosition(self):
          candWithDistFromMid = []
          for p in self._candidatePosition:
              candWithDistFromMid.append((p, math.fabs( p - self._mid)))
          sorted_position = sorted( candWithDistFromMid, key = lambda x:x[1] )
          if len(sorted_position) > 0:
             self._finalPosition = sorted_position[0][0]

      def generateMovingPar(self):
          way = self._mid - self._finalPosition
          way_percent = math.fabs(way/float(self._weight))
          print way
          if math.fabs(way) <= self._forwardMargen:
             print "forward>>>"
             self._movingPar = ('fullfw', 1)
          elif way > self._forwardMargen:
             self._movingPar = ('left', way_percent)
             print "left>>>>",way_percent
          elif way < -self._forwardMargen:
             self._movingPar = ('right', way_percent)
             print "right>>>",way_percent

