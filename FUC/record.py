# -*- coding: utf8 -*- 

from sys import path  #增加新的PATH
path.append(r"..\\")
import os,time,threading
from FUC import config
import logging
logging_recorder = logging.getLogger('main.recorder')

PATH = './DLL'

#报告名
def filename():
    return time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) 

def writeVariableList(verlist):
    try:
        VARLIST_TXT_PATH = PATH + "/ADS_VariableList.txt"
        with open(VARLIST_TXT_PATH,'w') as f:
            for i in verlist:
                f.write("%s\n"%i)   
    except Exception, e:
        logging_recorder.exception(str(e))
        
            
def startRecord(verlist,casename,internal = 10, times = 300000):
    try:
        reload(config)
        writeVariableList(verlist)
        #cmd_path = 'cmd /k cd /d %s' %PATH    
        msg = "%s recording is started "%casename
        logging_recorder.info(msg)
        if not os.path.exists('Recording'):
            os.mkdir('Recording')
        os.popen('cd "%s" & cmd /k AdsRecorder.exe  %s.1.1:%s ADS_VariableList.txt ../Recording/%s-%s.txt /interval %s /record %s ' %(PATH, config.PLC_IP,config.PLC_PORT, casename,filename(), internal, times)).read()          
        
        return True
    except Exception,e:
        logging_recorder.exception(str(e))
        return False
    
def stopRecord():
    """
    停止录播
    """
    try:   
        os.popen('cd "%s" & cmd /k del *.ctrl'%(PATH)).read()          
        msg = "recording  is stoped "
        logging_recorder.info(msg)
    except Exception,e:
        logging_recorder.exception(str(e))
        return False        
    
class RecordThread(threading.Thread):
    """
    启动录播线程
    """
    def __init__(self,  verlist, casename , threadname = "" ):
        """
        threadname 为线程名
        varlist 为需要录播的名字
        casename 为用例名
        """
        self.verlist = verlist
        self.casename = casename
        #调用启动录播函数
        threading.Thread.__init__(self,name=threadname)
    
    def run(self):
        msg = "%s recording thread is started "%self.casename
        logging_recorder.info(msg)
        startRecord(self.verlist, self.casename)
        msg = '%s recording  thread is dead '%self.casename
        logging_recorder.info(msg)
        return 


    
    
if __name__ == '__main__' :
    ver = ['.grsimu_setWindSpeed_1','.grGenSpeedForProcess']
    t1 = RecordThread('t1',ver,'testcase2')
    t1.start()
    print "fun1 start"
    #startRecord(ver,'runtest1')
    count = 10
    while count > 1:
        count = count -1
        time.sleep(1)
        print count
    stopRecord()