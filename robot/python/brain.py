import threading
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
             if frame:
                frame.applyProcessToFrame("drawContours").showFrame()

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
              print 'No feet command' 
 
