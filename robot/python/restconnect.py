import httplib


class RestClient:
      def __init__(self, restServerAddr = 'arduino.chuntao'):
          self._connection = None
          self.changeRestServer( restServerAddr )

      def changeRestServer(self, changedAddr ):
          self._connection = httplib.HTTPConnection( changedAddr )
          return self

      def sendResponse(self, restUrl ):
          #print "action is ", restUrl 
          self._connection.putrequest("GET", restUrl)
          self._connection.endheaders()
          try:
             response = self._connection.getresponse()
             return response
          except Exception as e:
             print e

