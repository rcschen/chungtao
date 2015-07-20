from eyes import Eyes
from brain import Brain

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
      def __init__(self, eyesUrl):
          self._eyesUrl = eyesUrl 
          self.queue = QueueFactory().getQueue()
          print dir(self.queue)
          super(Chuntao, self).__init__()

      def _set_senses(self):
          self._senses.append(Eyes(self._eyesUrl, self.queue))
          self._senses.append(Brain(self.queue))



if __name__ == '__main__':
   rob = Chuntao('http://192.168.1.235:8080/?action=stream')          
