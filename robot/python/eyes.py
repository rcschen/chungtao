import cv2
import urllib
import numpy as np

class Eyes:
      def __init__(self, videoUrl):
          self._video = urllib.urlopen(videoUrl)
          self._bytes = ''
          self.frameSize = 1024

      def run(self):
          pass

      def getFrame(self):
          _bytes = ''
          while True:
               _bytes += self._video.read(self.frameSize)
               startAnchor = _bytes.find('\xff\xd8')
               endAnchor = _bytes.find('\xff\xd9')
               if startAnchor != -1 and endAnchor != -1:
                  jpg = _bytes[startAnchor: endAnchor+2]
                  frame = cv2.imdecode(np.fromstring(jpg, dtype = np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
                  return Frame(frame)
import time

class Frame:
      def __init__(self, frame):
          self.timeStamp = time.time()
          self.frame = frame
