import threading

class Feet(threading.Thread):
      def __init__(self, kickstart):
          super(Feet,  self ).__init__(name = "Feet")
          self.feetCommandQueue = None
          self._kickstart = kickstart

      def setCommandQueue(self,queue):
          self.feetCommandQueue = queue

      def run(self):
          print "Not implement feet"

class WheelFeet(Feet):
      def __init__(self, kickstart):
          super(WheelFeet, self).__init__(kickstart)
          self._lastMove = None
         
      def run(self):
          while True:
                if self._kickstart.shouldRunFeet:
                   self._runFeetCommand()

      def _runFeetCommand(self):
          if not self.feetCommandQueue.isEmpty():
             move = self.feetCommandQueue.get()
             if not move.isEqualTo(self._lastMove):
                print "Truelyyyyyyyyy sent >>>>>>>>"
                move.setRobAddr(self._kickstart.robotIP)
                move.sendResponse()
                self._lastMove = move
