from restconnect import RestClient

class Move:
      def __init__(self, robotAddress = 'arduino.chuntao'):
          self._connection = RestClient( robotAddress ) 
          self._cmd = ''

      def setRobAddr(self, changedAddr ):
          self._connection.changeRestServer( changedAddr )
       
      def stop(self):
          self._cmd = '/arduino/stop/usless'
 
      def fullfw(self, factor = 0.8):
          self._cmd = '/arduino/fullfw/'+str(factor)
        
      def back(self):
          self._cmd = '/arduino/back/usless'

      def right(self, factor=0.8):
          self._cmd = '/arduino/turnright/'+str(factor)

      def left(self, factor=0.8):
          self._cmd = '/arduino/turnleft/'+str(factor)

      def rotateright(self, factor=0.8):
          self._cmd = '/arduino/rotateright/'+str(factor)

      def rotateleft(self, factor=0.8):
          self._cmd = '/arduino/rotateleft/'+str(factor)

      def stepright(self, factor=0.8):
          self._cmd = '/arduino/stepright/'+str(factor)

      def stepleft(self, factor=0.8):
          self._cmd = '/arduino/stepleft/'+str(factor)

      def sendResponse(self, cmd = None):
          if cmd:
             self._cmd = cmd
          #print self._cmd
          self._connection.sendResponse(self._cmd) 
     
      def isEqualTo( move )
          for attr in dir(move):
              attrOnget = getattr(a, attr)
              if not attrOnget.__class__ == types.MethodType:
                 if not attrOnget == getattr(self, attr):
                    return False
          return True
