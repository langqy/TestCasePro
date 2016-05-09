import os
CASEDIR = './CASE/'
from FUC.function import *

class autotest(): 
    def __init__(self,PATH):
        self.PATH = PATH
        
    def getDirList(self):   
        filenames = os.listdir(self.PATH)
        return filenames
    
    def getTestList(self,filenames):       
        namelist = []
        for filename in filenames:
            if filename[0] == 't'and filename[-1:] == 'y':
                fileanally = filename.split('.')
                namelist.append(fileanally[0])
        return namelist
    
    def creatInit(self,namelist):
        data = ''
        try:            
            for i in namelist:
                txt = 'from %s import * \n'%i
                data = data + txt
            with open('%s__init__.py'%self.PATH,'w+') as f:                    
                f.write(data)    
            return True
        except Exception,e:
            print e
            return False
        
    def runTest(self):
        through = 0
        failure = 0
        error = 0
        filenames = self.getDirList()
        namelist = self.getTestList(filenames)
        self.creatInit(namelist)      
        import CASE
        
        writeToTxt_no_time("The_Test_Report\n")
        for i in namelist:
            casename = i[5:]
            print i
            t = eval('CASE.%s.%s()'%(i,casename))
            a = t.start()


            if int(a) == 1:
                through += 1
            elif int(a) == 2:
                failure += 1
            else:
                error += 1
                    
        #error = len(namelist) - through - failure
                
        writeToTxt_no_time("All_Case_Complete.")
        writeToTxt_no_time("Total_Case_Num:%d (through/failure/error)=(%d / %d / %d)"%(len(namelist),through,failure,error))
a = autotest(CASEDIR)  
a.runTest()
