import threading
import math
from queue import QueueFactory
from moving import Move
 
class Brain(threading.Thread):
      def __init__(self):
          super(Brain,  self ).__init__(name = "Brain")
          self.frameQueue = None
          self.feetCommandQueue = None

      def setQueue(self, qName, queue ):
          if qName in dir(self):
             setattr(self, qName, queue)
          else:
             print "Queue name not found", qName

      def run(self):
          while True:
             frame = self._getFrame()
             self._wayToGoBydrawContours(frame)             

      def _getFrame(self):
          if not self.frameQueue.isEmpty():
             return self.frameQueue.get()
      
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
             return
          contours = Contours(frame)
          self.feetControl(*contours.runSteps())
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
          way_percent = way/float(self._weight)
          if math.fabs(way) <= self._forwardMargen:
             self._movingPar = ('fullfw',)
          elif way > self._forwardMargen:
             self._movingPar = ('left', way_percent)
          elif way < -self._forwardMargen:
             self._movingPar = ('right', way_percent)
