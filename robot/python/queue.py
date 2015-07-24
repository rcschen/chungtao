import Queue


class QueueFactory(object):
      def getQueue(self, type = 'simple', size = 10):
         if type == 'simple':
            return SimpleQueue(size)


class SimpleQueue:
      def __init__(self, size = 10):
          self._q = Queue.Queue(size)

      def put(self, data):
          if not self._q.full():
             self._q.put(data)
          else:
             #print "queue is full"
             pass
 
      def get(self):
          if not self._q.empty():
             return self._q.get()
          else:
             return None

      def isFull(self):
          return self._q.full()
        
      def isEmpty(self):
          return self._q.empty()

      def qsize(self):
          return self._q.qsize() 
