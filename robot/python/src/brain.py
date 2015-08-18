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
             time_diff = diff/c.TIME_UNIT
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


