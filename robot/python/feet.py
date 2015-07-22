import threading

class Feet(threading.Thread):
      def __init__(self, feetUrl):
          super(Feet,  self ).__init__(name = "Feet")
          self.feetCommandQueue = None
          self.feetUrl = feetUrl

      def setCommandQueue(self,queue):
          self.feetCommandQueue = queue

      def run(self):
          print "Not implement feet"

class WheelFeet(Feet):
      def __init__(self, feetUrl):
          super(WheelFeet, self).__init__(feetUrl)
          
      def run(self):
          while True:
                self._runFeetCommand()

      def _runFeetCommand(self):
          if not self.feetCommandQueue.isEmpty():
             move = self.feetCommandQueue.get()
             move.setRobAddr(self.feetUrl)
             move.sendResponse()
