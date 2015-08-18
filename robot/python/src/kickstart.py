import configer as cfg
from importlib import import_module

boolTrans = {'True': True, 'False':False}

class KickStart:
      def __init__(self):
          cfg.initConfig()
          self.robotIP = cfg.getVal('ROBOTINFO','IP')
          self.streamAddress = 'http://%s:%s%s' %(self.robotIP,  
                                                  cfg.getVal('ROBOTINFO','STREAMPORT'),
                                                  cfg.getVal('ROBOTINFO','STREAMNAME'))
          self.shouldCollectFrame = boolTrans.get(cfg.getVal('ROBOTMODE','COLLECTFRAME'),True)
          self.shouldRunFeet      = boolTrans.get(cfg.getVal('ROBOTMODE','RUNFEET'), True)
          self.manualMode         = boolTrans.get(cfg.getVal('ROBOTMODE','MANUAL'), False)
          self.shouldShowContour  = boolTrans.get(cfg.getVal('ROBOTMODE','SHOWCONTOUR'), False)
          self.blinkTime          = float( cfg.getVal('DURATION' ,'BLINKTIME')) 
          movingModule            = cfg.getVal('MOVINGALG', 'MODULE')
          movingClass             = cfg.getVal('MOVINGALG', 'CLASS')
          self.movingAlg          = getattr(import_module(movingModule), movingClass)
          self.showInfo()

      def showInfo(self):
          print "-----------robot-----------"
          print 'Robot address:            ', self.robotIP 
          print 'Robot Video Stream Url:   ', self.streamAddress
          print 'Eye should collect frame: ', self.shouldCollectFrame
          print 'Feet should be executed:  ', self.shouldRunFeet
          print 'Manual mode:              ', self.manualMode
          print 'Contour should be shown:  ', self.shouldShowContour
          print 'blinkTime:                ', self.blinkTime
