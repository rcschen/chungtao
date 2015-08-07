from eyes import Eyes
from brain import Brain
from feet import WheelFeet

from queue import QueueFactory
import threading

class Robot(threading.Thread):
      def __init__(self):
          super(Robot, self).__init__(name="Robot")
          self._senses = []
          self._set_senses()
          self._start_senses()
          
      def _set_senses(self):
          print "No senses are set!!!"
       
      def _start_senses(self):
          for sense in self._senses:
              print sense
              sense.start()              

      def controller(self):
          pass

      def eyes(self):
          pass

      def do_action(self):
          pass

class Chuntao(Robot):
      def __init__(self, kickstart):
          self.eyes = Eyes(kickstart)
          self.brain = Brain(kickstart)
          self.feet = WheelFeet(kickstart)
          super(Chuntao, self).__init__()

      def _set_brain(self):
          self._senses.append(self.brain)

      def _set_eyes(self):
          frameQueue = QueueFactory().getQueue('simple')
          self._senses.append(self.eyes)
          self.eyes.setFrameQueue(frameQueue)
          self.brain.setQueue('frameQueue', frameQueue)

      def _set_feet(self):
          feetCommandQueue = QueueFactory().getQueue('simple')
          self._senses.append(self.feet)
          self.feet.setCommandQueue(feetCommandQueue)
          self.brain.setQueue('feetCommandQueue', feetCommandQueue)

      def _set_senses(self):
          self._set_eyes()
          print "eye"
          self._set_feet()
          print "feet"
          self._set_brain()
          print "brain"

      def manualFeetControl(self, *par):
          self.brain.feetControl(*par)


import kickstart
if __name__ == '__main__':
   rob = Chuntao(kickstart.KickStart())       
   rob.start() 

   leave = True
   while leave :
      control = raw_input(">>>>")
      try:
         if control == "s":
            print "stop"
            rob.manualFeetControl('stop')
         elif control == "d":
            print "right"
            rob.manualFeetControl('right',0.2)
         elif control == "a":
            print "left"
            rob.manualFeetControl('left',0.2)
         elif control == "w":
            print "fullfw"
            rob.manualFeetControl('fullfw')
         elif control == "x":
            print "back"
            rob.manualFeetControl('back')
         elif control =="q":
            print "bye-bye"
            leave = False
         else:
            print "Not control command"
      except Exception as e:
         print e

