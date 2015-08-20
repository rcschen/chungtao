import configer

class Singleton(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

class Constants(Singleton):
   def __init__(self):
       configer.initConfig()
       self.TIME_UNIT = float( configer.getVal('CONSTANTS', 'TIME_UNIT'))
       self.FORWARD_MARGIN = int( configer.getVal('CONSTANTS', 'FORWARD_MARGIN'))
       self.MOVEON_MARGIN = int( configer.getVal('CONSTANTS', 'MOVEON_MARGIN'))

       self.CENTRAL_MARGIN = int( configer.getVal('CONSTANTS', 'CENTRAL_MARGIN'))
       self.SAVE_MARGIN_PERCENT = float(configer.getVal('CONSTANTS','SAVE_MARGIN_PERCENT'))
       self.TURN_STEP_TIME = int(configer.getVal('CONSTANTS','TURN_STEP_TIME'))
       self.HIGH_VARIANCE_MARGIN_PERCENT = float(configer.getVal('CONSTANTS','HIGH_VARIANCE_MARGIN_PERCENT'))
       self.STEP_TURN_MARGIN_PERCENT = float(configer.getVal('CONSTANTS','STEP_TURN_MARGIN_PERCENT'))
       
c = Constants()
