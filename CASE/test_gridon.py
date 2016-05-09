# -*- coding: utf8 -*- 
import time
from  PAR.parm import * 
from FUC import *
from casetemplate import *
class gridon(CaseTemplate):

    def getRecordeList(self):
        self.varlist = [Variable.data_Time,Variable.gen_speedPDM1,
                        Variable.gen_power,Variable.pitch,Variable.pitch_set,
                        Variable.operation_mode,Variable.gen_torque_set,Variable.bp_level]
    def case(self):
        OVER_TIME_LIMIT = 600
        setWindValue = 15
        print ("change wind")
        self.write(Simu.simu_windspeed, setWindValue)
        self.write(Variable.bp_50,1)
        time.sleep(2)
        self.write(Variable.bp_50,0)
        isGridOnTimeOut = check_timeout(Variable.operation_mode,Constant.GOP,1,OVER_TIME_LIMIT)
        if not isGridOnTimeOut:
            ass.checkEqual(Variable.operation_mode, Constant.GOP)
            return False
        else:
            time.sleep(10)
            if ass.checkEqual(Variable.operation_mode, Constant.GOP) and ass.checkGreater(Variable.gen_power, 20):
                return True 
            else:
                return False
        
        
    def setUp(self):
        #toolbox.reset(Variable.softSafetyChain_Tripped)
        toolbox.reset(Variable.safety_chain_reset)
       
        time.sleep(0.5)
         #刹车等级 查看，等待风机刹车等级为0
        isBreakTimeOut = toolbox.check_timeout(Variable.bp_level,Constant.NO_BP)
        if not isBreakTimeOut:
            report("")
            return False
        return True