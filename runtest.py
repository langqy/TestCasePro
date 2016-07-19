
# -*- coding: utf-8 -*-
import logging 
import logging.config
import sys
LOG_FILE = 'tst.log'
#输出到屏幕   
ch = logging.StreamHandler() 
#写入文件实例化
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
fmt = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter
logger_main = logging.getLogger('main')    # 获取名为tst的logger
logger_main.addHandler(handler)           # 为logger添加handler
#logger_main.addHandler(ch)
logger_main.setLevel(logging.DEBUG)
import casetemplate
import os
CASEDIR = './CASE/'
from FUC.report import *

def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是
    # 编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

class autotest(): 
    def __init__(self,PATH):
        self.PATH = PATH
        sys.path.append(os.path.split(self.PATH)[0])
        
    
    def getTestList(self,filenames):       
        namelist = []
        for filename in filenames:
            if filename[0] == 't'and filename[-1:] == 'y':
                namelist.append(filename)
        return namelist
    
  
    def runTest(self):
        through = 0
        failure = 0
        error = 0
        filenames = os.listdir(self.PATH)
        namelist = self.getTestList(filenames)         
        report("The_Test_Report\n",False)
        caseTemp = open('caserunner.txt').read()
        for filename in namelist:
            caseData = caseTemp.replace('CASEPATH',filename)           
            print 'filename:',filename
            with open(filename,'w') as f:
                f.write(caseData)
            modelname = filename.replace('.py','')
            print 'modelname:',modelname
            exec('import %s'%modelname)    
            t = eval('%s.case()'%modelname)
            a = t.start(filename)           
            #os.remove(filename)
            if int(a) == 1:
                through += 1
            elif int(a) == 2:
                failure += 1
            else:
                error += 1
            t = None
            time.sleep(1)
        #error = len(namelist) - through - failure
                
        report("All_Case_Complete.",False)
        report("Total_Case_Num:%d (through/failure/error)=(%d / %d / %d)"%(len(namelist),through,failure,error),False)


try:
    CASEPath = open('temp.txt').readline().replace('\\','/')
    print CASEPath
    a = autotest(CASEPath) 
    logger_main.info('\n'+'-'*50+timeSign()+'-'*50)
    a.runTest()
    logger_main.info('\n'+'-'*50+timeSign()+'-'*50)
    b = raw_input()
except Exception,e:
    logger_main.exception(str(e))