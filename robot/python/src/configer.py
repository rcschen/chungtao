import os, ConfigParser

HOMEPATH = os.path.abspath(os.pardir)
CONFIGPATH = os.path.join(HOMEPATH, 'config', 'kickstart.cfg')

def fileLoad(type):
    def lbd(func):
        def runFunc(*par):
            cfg=ConfigParser.ConfigParser()
            cfg.read( CONFIGPATH )
            par = (cfg,) + par
            val = func(*par)
            if type == 'rw':
               cfg.write( open(CONFIGPATH,'wb') )  
            return val
        return runFunc
    return lbd
    

@fileLoad('rw')
def initConfig(cfg):
    print cfg
    if os.path.exists( CONFIGPATH ):
       return

    if not cfg.has_section('ROBOTINFO'):
       cfg.add_section('ROBOTINFO')
    cfg.set('ROBOTINFO', 'IP', '192.168.1.1')
    cfg.set('ROBOTINFO', 'STREAMPORT', '8080')
    cfg.set('ROBOTINFO', 'STREAMNAME', '/?action=stream')

    if not cfg.has_section('ROBOTMODE'):
       cfg.add_section('ROBOTMODE')
    cfg.set('ROBOTMODE', 'COLLECTFRAME', 'True')
    cfg.set('ROBOTMODE', 'RUNFEET', 'True')
    cfg.set('ROBOTMODE', 'MANUAL', 'False')
    cfg.set('ROBOTMODE', 'SHOWCONTOUR', 'True')

    if not cfg.has_section('DURATION'):
       cfg.add_section('DURATION')
    cfg.set('DURATION', 'BLINKTIME', '1')

    if not cfg.has_section('MOVINGALG'):
       cfg.add_section('MOVINGALG')
    cfg.set('MOVINGALG', 'MODULE', 'contours')
    cfg.set('MOVINGALG', 'CLASS', 'ContoursFarthest')

    if not cfg.has_section('CONSTANTS'):
       cfg.add_section('CONSTANTS')
    cfg.set('CONSTANTS', 'TIME_UNIT', '1.7062')
    cfg.set('CONSTANTS', 'FORWARD_MARGIN', '5')
    cfg.set('CONSTANTS', 'CENTRAL_MARGIN', '100000')
    cfg.set('CONSTANTS', 'SAVE_MARGIN_PERCENT', '0.1')
    cfg.set('CONSTANTS', 'TURN_STEP_TIME', '2')
    cfg.set('CONSTANTS', 'HIGH_VARIANCE_MARGIN_PERCENT', '0.1')
    cfg.set('CONSTANTS', 'STEP_TURN_MARGIN_PERCENT', '0.85')




@fileLoad('r')
def getVal(cfg, sec, opt):
    try:
       val = cfg.get(sec, opt)
       return val
    except Exception as e:
       print "get value from config error %s" %e
       return None



