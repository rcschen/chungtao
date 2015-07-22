from restconnection import RestClient

class Move:
      def __init__(self, robotAddress = 'arduino.chuntao')
          self._connection = RestClient( robotAddress ) 
          self._cmd = ''

      def changeRobAddr( changedAddr ):
          self._connection.changeRestServer( changedAddr )
       
      def stop(self):
          self._sendResponse( 'arduino/stop' )
 
      def fullfw(self):
          cmd = 'arduino/fullfw'

      def back(self):
          cmd = 'arduino/back'

      def right(self, factor):
          cmd = 'arduino/turnright/'+str(factor)

      def left(self, factor):
          cmd = 'arduino/turnleft/'+str(factor)

      def sendResponse(self cmd = None):
          if not cmd:
             self._cmd = cmd
          self._connection.sendResponse(self._cmd) 
 
