
# -*- coding: utf-8 -*-
import logging
logging_report = logging.getLogger('main.runtest')
import casetemplate
import os,time
from PyQt4.QtCore import QThread,pyqtSignal
from FUC.report import *
import sys
sys.path.append(os.curdir)
sys.path.append('C:\\Python27\\lib')
class autotest(QThread):
    #当前运行的index
    sinOut1 = pyqtSignal(int)
    #运行结果
    sinOut2 = pyqtSignal(int,int)
    #强制停止的序号
    sinOut3 = pyqtSignal(int)
    #结果
    sinOut4 = pyqtSignal(list)
    sinOut5 = pyqtSignal(str)
        
    def __init__(self,parent=None):
        super(autotest, self).__init__(parent)
        self.bStoped = True
        self.bPaused = False
        
    
    def pause(self,bvalue):
        self.bPaused = bvalue
    
    def stop(self):
        self.bStoped = True
        
    def runTest(self,casepathlist,paramFileName):
        self.casepathlist = casepathlist
        self.paramFileName = paramFileName
        self.start()
        
    def run(self):
        through = 0
        failure = 0
        error = 0
        self.bStoped = False 
        myreport.makeNewReport()       
        self.sinOut5.emit(myreport.strfilename)        
        report("The_Test_Report\n",False)        
        caseTemp = open('caserunner.txt').read()
        count = 0        
        for filepath in self.casepathlist:      
            self.sinOut1.emit(count)
            caseData = caseTemp.replace('CASEPATH',filepath).replace('SimuParam',self.paramFileName)      
            filename = os.path.basename(filepath)
            print 'filename:',filename
            
            with open(filename,'w') as f:
                f.write(caseData)
            modelname = filename.replace('.py','')
            print 'modelname:',modelname
            try:
                exec('import %s'%modelname)    
                t = eval('%s.case()'%modelname)
            
                a = t.start(filename)    
            except Exception,e:
                a = -1
                logging_report.exception(str(e))
            os.remove(filename)
            if os.path.exists('./'+filename+'c'):
                os.remove(filename+'c')
            if int(a) == 1:
                through += 1
            elif int(a) == 2:
                failure += 1
            else:
                error += 1 
            t = None
            self.sinOut2.emit(count,int(a))
            time.sleep(1)
            while self.bPaused:
                time.sleep(1)                
                if self.bStoped:
                    self.sinOut3.emit(count)
                    break
            if self.bStoped:
                self.sinOut3.emit(count)
                break            
            count += 1
        self.sinOut4.emit([through,failure,error])
        if count == len(self.casepathlist):
            report("All_Case_Complete.",False)
        report("Total_Case_Num:%d (through/failure/error)=(%d / %d / %d)"%(len(self.casepathlist),through,failure,error),False)
        self.bStoped = True
        
def getTestList(casePath ,filenames):       
    namePathlist = []
    for filename in filenames:
        if filename[0] == 't'and filename[-1:] == 'y':
            namePath= os.path.join(casePath,filename).replace('\\','/')
            namePathlist.append(namePath)
    return namePathlist

