from restconnect import RestClient

class Move:
      def __init__(self, robotAddress = 'arduino.chuntao'):
          self._connection = RestClient( robotAddress ) 
          self._cmd = ''

      def setRobAddr(self, changedAddr ):
          self._connection.changeRestServer( changedAddr )
       
      def stop(self):
          self._cmd = '/arduino/stop'
 
      def fullfw(self):
          self._cmd = '/arduino/fullfw'
        
      def back(self):
          self._cmd = '/arduino/back'

      def right(self, factor=0.8):
          self._cmd = '/arduino/turnright/'+str(factor)

      def left(self, factor=0.8):
          self._cmd = '/arduino/turnleft/'+str(factor)

      def sendResponse(self, cmd = None):
          if cmd:
             self._cmd = cmd
          print self._cmd
          self._connection.sendResponse(self._cmd) 
 
