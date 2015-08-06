import cv2
import urllib
import numpy as np
import threading
import time
import imgprocess

class Eyes(threading.Thread):
      def __init__(self, videoUrl, debug):
          super(Eyes,  self ).__init__(name = "Eyes")
          try:
            self._video = urllib.urlopen(videoUrl)
          except Exception as e:
            print 'Can not connect to video url: ', e
          self._bytes = ''
          self.frameSize = 1024
          self.frameQueue = None
          self._needReset = False
          self._closeEyes = False
          self._stop_capture = False
          self._debug = debug

      def setFrameQueue(self, frameQueue):
          self.frameQueue = frameQueue

      def run(self):
          while not self._debug:
              if not self._needReset or not self._closeEyes:
                 self._collectFrames()

      def closeEyes(self):
          self.resetQueue()
          self._closeEyes = True

      def openEyes(self):
          self.resetQueue()
          self._closeEyes = False

      def resetQueue(self):
          self._needReset = True
          while not self.frameQueue.isEmpty():
             self.frameQueue.get()
          self._needReset = False

      def _collectFrames(self):
          frame = self._captureFrame()
          if not self.frameQueue.isFull() and frame:
             #print "<<<<<",frame
             self.frameQueue.put( frame )

      def _captureFrame(self):
          #_bytes = ''
         
          while True:
               try:
                  self._bytes += self._video.read(self.frameSize)
                  startAnchor = self._bytes.find('\xff\xd8')
                  endAnchor = self._bytes.find('\xff\xd9')
                  if startAnchor != -1 and endAnchor != -1:
                     jpg = self._bytes[startAnchor: endAnchor+2]
                     self._bytes = self._bytes[endAnchor+3:]
                     frame = cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
                     return Frame(frame)
               except Exception as e:
                  print 'Can not capture frame: ',e
                  return None

class Frame:
      def __init__(self, frame):
          self.timeStamp = time.time()
          self.frame = frame

      def showFrame(self):
          cv2.imshow( 'i', self.frame )
          if cv2.waitKey(1) == 27:
                   exit(0)
    
      def applyProcessToFrame(self, *par ):
          processName = par.__getitem__(0)
          if not processName in dir(imgprocess):
             print "Selected process is not found: ", processName
          tmp_par = list(par)
          tmp_par[0] = self.frame
          par = tuple(tmp_par)
          try:
             feature = getattr(imgprocess, processName)(*par)
             return Frame( feature )

          except Exception as e:
             print "Run image process error:", e
             return None         
        
          
