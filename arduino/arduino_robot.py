import base64
import httplib
import urllib
from  msvcrt import *

class robotConnect(object):
      def __init__( self, robotAddress = 'arduino.cschen' ):
          self.robotAddress = robotAddress
          self.connection = httplib.HTTPConnection(self.robotAddress)

      def stop(self):
          cmd = "/arduino/stop"            
          self._connect(cmd)

      def left(self):
          cmd = "/arduino/turnleft/0.7"            
          self._connect(cmd)

      def right(self):
          cmd = "/arduino/turnright/0.8"            
          self._connect(cmd)

      def fullfw(self):
          cmd = "/arduino/fullfw"            
          self._connect(cmd)
		  
      def back(self):
          cmd = "/arduino/back"            
          self._connect(cmd)

      def test(self):
          cmd = "/arduino/test/123"
          self._connect(cmd)

      def _connect(self, action):
          print "action is ", action  
          self.connection.putrequest("GET", action)
          self.connection.endheaders()
          try:
             response = self.connection.getresponse()
             return response
          except Exception as e:
             print e
             

if __name__ == '__main__':
   address = raw_input('input address:')
   if len(address) == 0:
      address = '192.168.1.235'
   robotConnect = robotConnect(address)
   print "The server address is: ", address
   leave = True
   print dir(robotConnect)
   while leave :
      try:
         control = getch() 
         if control == "s":
            print "stop"
            robotConnect.stop()
         elif control == "d":
            print "right"
            robotConnect.right()
         elif control == "a":
            print "left"
            robotConnect.left()
         elif control == "w":
            print "fullfw"
            robotConnect.fullfw()
         elif control == "x":
            print "back"
            robotConnect.back()
         elif control == "t":
            print "test"
            robotConnect.test()			
         elif control =="q":
            print "bye-bye"
            leave = False
         else:
            print "Not control command"
      except Exception as e:
         print e

