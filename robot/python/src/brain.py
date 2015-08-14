import threading
import math
import util
from queue import QueueFactory
from moving import Move
import time
from constants import *
 
class Brain(threading.Thread):
      def __init__(self, kickstart):
          super(Brain,  self ).__init__(name = "Brain")
          self.frameQueue = None
          self.feetCommandQueue = None
          self._last_time = time.time()
          self._kickstart = kickstart

      def setQueue(self, qName, queue ):
          if qName in dir(self):
             setattr(self, qName, queue)
          else:
             print "Queue name not found", qName

      def run(self):
          while True:
             diff, updatedTime = util.get_diff_timestamp( self._last_time )
             frame = self._getFrame()
             time_diff = diff/TIME_UNIT
             if time_diff >= self._kickstart.blinkTime:
                self._last_time = updatedTime
                if not self._kickstart.manualMode  and frame:
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
          if self._kickstart.shouldShowContour:
             contours._contour.showFrame()

class Contours:
      def __init__(self, frame):
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
          self._finalPosition = None
          self._movingPair = ('stop')
          self.setSteps()
          self._highVariance = 0

      def runSteps(self):
          for step in self._steps:
              #print ">>>>",step
              if self._breakStepRun:
                 break
              getattr(self,step)()          
          return self._movingPair

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
          if len(self._bottonLine) == 0:
             self._steps.remove('isOnTheWay') 
             self._steps.remove('getFarthestPosition')
             self._steps.remove('findNearestPosition')

      def isOnTheWay(self):
          if len([ p for p in self._bottonLine if math.fabs( p - self._mid ) < CENTRAL_MARGIN ]) == 0 :
             self._candidatePosition = self._bottonLine
             self._steps.remove('getFarthestPosition')

      def getFarthestPosition(self):
          high_set = []
          contourImg = self._contour.frame
          self._candidatePosition = []

          for p in self._bottonLine:
              h_anchor = self._high - 6
              while not h_anchor < 0:
                    if list(contourImg[h_anchor][p]) == list(self._contourColor) or h_anchor == 0 :
                       #print "BBBBBBBBBb",(p, h_anchor)
                       high_set.append((p, h_anchor))
                       break
                    h_anchor = h_anchor - 1

          if len(high_set)  > 0:
             sorted_position = sorted( high_set, key = lambda x:x[1] )
             save_high = ( 1-SAVE_MARGIN )*self._high        
             _candidate = [ p for p in sorted_position 
                              if p[1] == sorted_position[0][1] 
                              and p[1] <= save_high ]
             self._highVariance = sorted_position[-1][1] - sorted_position[0][1]
             self._candidatePosition = [p[0] for p in _candidate]
         
      def findNearestPosition(self):
          candWithDistFromMid = []
          for p in self._candidatePosition:
              candWithDistFromMid.append((p, math.fabs( p - self._mid)))
          sorted_position = sorted( candWithDistFromMid, key = lambda x:x[1] )
          if len(sorted_position) > 0:
             self._finalPosition = sorted_position[0][0]
          else:
             self._finalPosition = None

      def generateMovingPar(self):
          self._movingPair = MovingGenerator(self).generateMovingPar()


class MovingGenerator:
      def __init__(contours):
          self._contours = contours
          self.way = contour._mid - contour._finalPosition
          self.way_percent = ( 1.0 -  math.fabs(self.way/float(contour._weight)) )
          self.high_variance_percent = float( contour._highVariance/contour._high )

      def generateMovingPar(self):
          if not self._contours._finalPosition:
             print "stepright>>>"
             return  ('stepright', 0.6)

          elif self.high_variance_percent < HIGH_VARIANCE_MARGIN 
               or math.fabs(self.way) <= FORWARD_MARGIN:
             print "forward>>>"
             return('fullfw', 0.8)
            
          elif self.way > FORWARD_MARGIN:
             print "step left>>>>",way_percent
             return ('left', self.way_percent)

          elif self.way < -FORWARD_MARGIN:
             print "step right>>>",self.way_percent
             return ('right', self.way_percent)



