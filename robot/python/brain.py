import threading

class Brain(threading.Thread):
      def __init__(self, queue):
          super(Brain,  self ).__init__(name = "Brain")
          self.frameQueue = queue

      def run(self):
          while True:
             frame = self._getFrame()
             if frame:
                frame.applyProcessToFrame("drawContours").showFrame()

      def _getFrame(self):
          if not self.frameQueue.isEmpty():
             return self.frameQueue.get()

