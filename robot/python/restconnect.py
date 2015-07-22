import httplib


class RestClient:
      def __init__(self, restServerAddr = 'arduino.chuntao'):
          self._connection = None
          self.changeRestServer( restServerAddr )

      def changeRestServer(self, changedAddr ):
          self._connection = httplib.HTTPConnection( changedAddr )
          return self

      def sendResponse( restUrl ):
          print "action is ", restUrl 
          self.connection.putrequest("GET", restUrl)
          self.connection.endheaders()
          try:
             response = self.connection.getresponse()
             return response
          except Exception as e:
             print e

