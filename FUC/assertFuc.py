# -*- coding: utf8 -*- 
from FUC.communication import ads
from FUC.report import report
import logging

logging_assert = logging.getLogger('main.config')
    

#自定义unittest 修改断言内容
class assertFun():
    #----------------------------------------------------------------------
    def isTrue(self,data,port = ""):
        is_true = False    #判断输入值是否为true的返回值  is_true=true为输入值是true
        if port == '':
            temp = bool(ads.read(data)) #读取数值
        else:
            temp = bool(ads.read(data,port))
        #判断
        if temp == 1: #满足条件           
            is_true = True  
        return is_true    
    
    def checkTrue(self,data,port = ""):
        is_true = False

        if port == '':
            temp = bool(ads.read(data)) #读取数值
        else:
            temp = bool(ads.read(data,port))

        #print data,temp
        #判断
        if temp == 1: #满足条件
            data = '     PASS:IS True , %s(%s)'%(data,str(temp))   #格式 5个空格+PASS:IS True+1个空格+data   
            is_true = True
        elif temp == 0:#不满足条件
            data = 'ERROR:IS not True , %s(%s)'%(data,str(temp))
        else:#数值不满足查看条件，需要查看数值类型
            data = 'ERROR True:please check data type,%s'%(data)
        #数值写入
        report(data)
        return is_true   
    
    #查看数值是否为False并写入报告
    def isFalse(self,data,port = ""):
        if port == '':
            temp = bool(ads.read(data)) #读取数值
        else:
            temp = bool(ads.read(data,port))
        is_false = False
        #判断
        if temp == 0: #满足条件           
            is_false = True       
        return is_false        
    
    def checkFalse(self,data,port = ""):
        is_false = False
        if port == '':
            temp = bool(ads.read(data)) #读取数值
        else:
            temp = bool(ads.read(data,port))

        #判断
        if temp == 0: #满足条件
            data = '     PASS:IS False , %s(%s) '%(data,str(temp))  
            is_false = True
        elif temp == 1:#不满足条件
            data = 'ERROR:IS not False , %s(%s) '%(data,str(temp))
            
        else:#数值不满足查看条件，需要查看数值类型
            data = 'ERROR False:please check data type,%s'%data
            
        #数值写入
        report(data) 
        return is_false
    
    #判断是否相同
    def isEqual(self,data_1,data_2):
        temp_1 = ads.read(data_1) #读取数值
        
        
        if str(data_2)[0] == '.':
            temp_2 =ads.read(data_2) 
        else:
            temp_2 = data_2
    
        temp_2 = type(temp_1)(temp_2)
        #判断
        if temp_1 == temp_2: #满足条件
            return True
        else :
            return False
    
    def checkEqual(self,data_1,data_2):
        is_equal = False
        temp_1 = ads.read(data_1) #读取数值
                
        if str(data_2)[0] == '.':
            temp_2 =ads.read(data_2) 
        else:
            temp_2 = data_2    
        temp_2 = type(temp_1)(temp_2)           
        #判断
        if temp_1 == temp_2: #满足条件            
            data = '     PASS:IS Equal , %s(%s) = %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
            is_equal = True
        else :
            data = 'ERROR:IS not Equal , %s(%s) != %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
        #数值写入
        report(data) 
        return is_equal
        
    #查看数值1是否大于数值2        
    def isGreater(self,data_1,data_2):
        temp_1 = ads.read(data_1) #读取数值
        is_greater = False
        if type(data_2) == str:
            temp_2 = ads.read(data_2) #读取数值
        else:
            temp_2 = data_2
        #判断
        if float(temp_1) >  float(temp_2): #满足条件           
            is_greater = True
        return is_greater
    
    def checkGreater(self,data_1,data_2): 
        temp_1 = ads.read(data_1) #读取数值
        is_greater = False
        if type(data_2) == str:
            temp_2 = ads.read(data_2) #读取数值
        else:
            temp_2 = data_2                   
        if float(temp_1) >  float(temp_2): #满足条件
            data = '     PASS:IS Greater , %s(%s) > %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
            is_greater = True
        else :
            data = 'ERROR:IS not Greater , %s(%s) < %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
        #数值写入
        report(data)  
        return is_greater

    #查看数值1是否小于数值2
    def isLess(self,data_1,data_2):
        is_less = False
        temp_1 = ads.read(data_1) #读取数值

        if type(data_2) == str:
            temp_2 = ads.read(data_2) #读取数值
        else: 
            temp_2 = data_2                      
        #判断
        if float(temp_1) <  float(temp_2): #满足条件           
            is_less = True   
        return is_less


    def checkLess(self,data_1,data_2):
        is_less = False
        temp_1 = ads.read(data_1) #读取数值

        if type(data_2) == str:
            temp_2 = ads.read(data_2) #读取数值
        else: 
            temp_2 = data_2
        if float(temp_1) <  float(temp_2): #满足条件
            data = '     PASS:IS Less , %s(%s) < %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))    
            is_less = True
        else :
            data = 'ERROR:IS not Less , %s(%s) > %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
        #数值写入
        report(data)
        return is_less

#实例化断言
ass = assertFun()