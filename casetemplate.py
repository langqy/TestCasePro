
# -*- coding: utf8 -*- 
import inspect,time
from FUC.record import * 
from FUC.assertFuc import *
from FUC  import toolbox
from FUC.toolbox import *
import logging
logger_casetemplate = logging.getLogger('main.casetemplate')
#实例化断言
ass = assertFun()
def get_current_function_name():
    return inspect.stack()[1][3]
########################################################################
##测试用例模板，对外提供case、setUp、tearDown、getRecordeList接口
##启动用例使用start方法
##Ver 1.0
##Last Edited By lianjun.yao 
##Time: 2014.11.5 14:00
########################################################################
class  CaseTemplate():
    """"""

    #----------------------------------------------------------------------
    #初始化
    def __init__(self):
        
        self.backUpDic = {}                                 #初始化备份字典        
        self.varlist = []                                   #初始化录播变量        
        self.startTime = time.time()                        #记录开始时间
        self.sign = 0
        #if parm.Constant.PARMTYPE == "SC1":
            #ads.write(parm.Variable.SCADA_active,1)             #激活SCADA
    
    #改写write功能，增加判断是否第一次写入，是记录至备份词典
    def write(self,ver,data):        
        if not ver in self.backUpDic:                       #判断是否在词典中           
            backdata = ads.read(ver)                        #读取原始值            
            self.backUpDic[ver] = backdata                  #写入备份词典
       
        ads.write(ver,data)                                 #写入值        
        #time.sleep(0.1)       
        #if not ass.checkEqual(ver,data):                    #判断是否写入成功            
        #    raise DivisionException(ver,data)               #写入不成功则表明用例错误或通讯错误，则抛除异常
        
        
    #数据还原    
    def tunBack(self):            
        if len(self.backUpDic) > 0:                         #判断备份词典中是否存在值
            for i in self.backUpDic:    
                if ads.platForm == 2 and i[:7] == 'Targets':
                    ads.unlock(i)
                else:
                    ads.write(i,self.backUpDic[i])              #逐条写入原始值 还原
                time.sleep(0.1)
                
    #启动数据记录功能， 输入为 用例名    
    def runRecorder(self, casename):
        print 'Start record'          
        self.recorder = RecordThread( self.varlist, casename,'Recorder Thread')
        self.recorder.start()                                    #数据记录线程启动       
        if self.recorder.isAlive:                                #确认线程启动
            print 'Recorder thread is running'
        else:
            print "ERROR: The recorder thread is not running"

    #封装运行时间
    def runTime(self):        
        toolbox.end_stamp(self.startTime,time.time())               #计算总运行时间并写入报告
        report("END\n",False)
    
    #运行脚本用例程序   
    def runCase(self):
        self.sign = 0
        try:
            report("START:%s"%self.casename,False)
            report("%s, Start running"%self.casename)            
            setUpOK = self.setUp()                          #准备工作            
            if not setUpOK :                                #若返回false 则退出当前用例执行
                report("%s ----Failed---setUp"%self.casename)
                self.sign = 2
                return False            
            ok = self.case()                                #执行用例主体   
            if ok:                
                report("%s ---- Passed"%self.casename)      #通过测试
                self.sign = 1
            else:    
                report("      CASE_FAILED:%s"%self.casename,False) #未通过测试，更改用例失败时的报告输出*（by feng.liu）
                #report("%s ====Faild"%self.casename)    
                self.sign = 2
        except Exception,e:
            logger_casetemplate.exception(str(e))
        finally:           
            self.tearDown()                                 #还原动作            
            self.stopRecord()                                #停止录播           
            self.tunBack()                                  #还原改写参数            
            self.runTime()                                  #记录运行时间
    
    #提供准备操作的API，用于改写                   
    def setUp(self):
        return True
    
    #具体执行用例，改写该API
    def case(self):
        return True
        
    #提供还原操作的API，用于改写         
    def tearDown(self):        
        return False
    
    #若需要启用录数据功能，改写该API
    def getRecordeList(self):   
        self.varlist =[]
    
    def stopRecord(self):
        if len(self.varlist)> 0:
            stopRecord()
            
    #启动用例主体函数 不可修改
    def start(self,casename):
        
        self.casename = casename             #获取当前用例名       
        self.getRecordeList()                               #获取记录数据的列表
        #print len(self.verlist)
        if len(self.varlist)> 0:                            #如果录数据列表不为空则启动录数据
            self.runRecorder(self.casename)
        self.runCase()
        return self.sign
    


