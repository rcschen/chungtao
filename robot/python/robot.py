from eyes import Eyes
from brain import Brain
from feet import WheelFeet

from queue import QueueFactory

class Robot(object):
      def __init__(self):
          self._senses = []
          self._set_senses()
          self._start_senses()

      def _set_senses(self):
          print "No senses are set!!!"
       
      def _start_senses(self):
          for sense in self._senses:
              sense.start()              

      def controller(self):
          pass

      def eyes(self):
          pass

      def do_action(self):
          pass

class Chuntao(Robot):
      def __init__(self, eyesUrl, feetUrl):
          self.eyes = Eyes(eyesUrl)
          self.brain = Brain()
          self.feet = WheelFeet(feetUrl) 
          super(Chuntao, self).__init__()

      def _set_brain(self):
          self._senses.append(self.brain)

      def _set_eyes(self):
          frameQueue = QueueFactory().getQueue('simple')
          self._senses.append(self.eyes)
          print dir(self.eyes)
          self.eyes.setFrameQueue(frameQueue)
          self.brain.setQueue('frameQueue', frameQueue)

      def _set_feet(self):
          feetCommandQueue = QueueFactory().getQueue('simple')
          self._senses.append(self.feet)
          self.feet.setCommandQueue(feetCommandQueue)
          self.brain.setQueue('feetCommandQueue', feetCommandQueue)

      def _set_senses(self):
          self._set_eyes()
          self._set_feet()
          self._set_brain()


if __name__ == '__main__':
   rob = Chuntao('http://192.168.1.235:8080/?action=stream','192.168.1.235')          
