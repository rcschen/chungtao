from restconnect import RestClient
import types

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
     
      def isEqualTo(self, move ):
          '''
          for attr in dir(move):
              attrOnget = getattr(move, attr)
              if not attrOnget.__class__ == types.MethodType \
                 and not attrOnget.__class__ == types.InstanceType:
                 print ">>>>> move >>", attrOnget
                 print ">>>>> self >>", getattr(self, attr)
                 print "=====result==",attrOnget == getattr(self, attr)
                 if not attrOnget == getattr(self, attr):
                    return False
          return True
          '''
            
          if move and  move._cmd == self._cmd:
             return True
          return False



