# -*- coding: utf8 -*- 
from sys import path  #增加新的PATH
path.append(r"..\\")

import time
import datetime,string

from PAR import parm
from FUC import ads


#信息写入函数
def timeSign():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

#报告名
def filename():
    return time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) 

IP = parm.Constant.IP
PATH =r'%s\%s.txt'%(parm.Constant.PATH,filename() ) 
   
def writeToTxt(var):
    try:
        #以在结尾写入模式打开文件    
        fp = open(PATH,'a')
        #数据整合 时间戳+3个空格+入参+回车

        if var[:5] == 'ERROR' or var[:5] == 'Error' or var[:5] == 'error': # 
            data ='   '+'!!!'+timeSign() + '   ' + var + '!!!\n' 
        else:
            data ='      '+timeSign() + '   ' + var + '\n' 
            
        #写入数据 
        fp.write(data)  
    except Exception,e:
        print e 

def writeToTxt_no_time(var):
    try:    
        #以在结尾写入模式打开文件    
        fp = open(PATH,'a')
        #数据整合 时间戳+3个空格+入参+回车
        data =var + '\n' 
        #写入数据 
        fp.write(data)  
    except Exception,e:
        print e     
        
#写入报告    
def report(data):  
    print data
    writeToTxt(data)
    

#自定义unittest 修改断言内容
class assertFun():
    #----------------------------------------------------------------------
    def isTrue(self,data,readtype = 1):
        is_true = False    #判断输入值是否为true的返回值  is_true=true为输入值是true
        temp = ads.read(data,readtype) #读取数值
        #判断
        if temp == 1: #满足条件           
            is_true = True  
        return is_true    
    
    def checkTrue(self,data,readtype = 1):
        is_true = False
        temp = ads.read(data,readtype) #读取数值
        #print data,temp
        #判断
        if temp == 1: #满足条件
            data = '     PASS:IS True , ' + data   #格式 5个空格+PASS:IS True+1个空格+data   
            is_true = True
        elif temp == 0:#不满足条件
            data = 'ERROR:IS not True , ' + data 
        else:#数值不满足查看条件，需要查看数值类型
            data = 'ERROR True:please check data type,%s'%data
        #数值写入
        report(data)
        return is_true   
    
    #查看数值是否为False并写入报告
    def isFalse(self,data,readtype = 1):
        temp = ads.read(data,readtype) #读取数值
        is_false = False
        #判断
        if temp == 0: #满足条件           
            is_false = True       
        return is_false        
    
    def checkFalse(self,data,readtype = 1):
        is_false = False
        temp = ads.read(data,readtype) #读取数值

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
    def isEqual(self,data_1,data_2,readtype = 1):
        temp_1 = ads.read(data_1,readtype) #读取数值
        
        
        if str(data_2)[0] == '.':
            temp_2 =ads.read(data_2,readtype) 
        else:
            temp_2 = data_2
    
        temp_2 = type(temp_1)(temp_2)
        #判断
        if temp_1 == temp_2: #满足条件
            return True
        else :
            return False
    
    def checkEqual(self,data_1,data_2,readtype = 1):
        is_equal = False
        temp_1 = ads.read(data_1,readtype) #读取数值
                
        if str(data_2)[0] == '.':
            temp_2 =ads.read(data_2,readtype) 
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
    def isGreater(self,data_1,data_2, readtype = 1):
        temp_1 = ads.read(data_1,readtype) #读取数值
        is_greater = False
        if type(data_2) == str:
            temp_2 = ads.read(data_2,readtype) #读取数值
        else:
            temp_2 = data_2
        temp_2 = type(temp_1)(temp_2)   
        #判断
        if temp_1 >  temp_2: #满足条件           
            is_greater = True
        return is_greater
    
    def checkGreater(self,data_1,data_2, readtype = 1): 
        temp_1 = ads.read(data_1,readtype) #读取数值
        is_greater = False
        if type(data_2) == str:
            temp_2 = ads.read(data_2,readtype) #读取数值
        else:
            temp_2 = data_2                   
        temp_2 = type(temp_1)(temp_2)
        if temp_1 >  temp_2: #满足条件
            data = '     PASS:IS Greater , %s(%s) > %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
            is_greater = True
        else :
            data = 'ERROR:IS not Greater , %s(%s) < %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
        #数值写入
        report(data)  
        return is_greater

    #查看数值1是否小于数值2
    def isLess(self,data_1,data_2, readtype = 1):
        is_less = False
        temp_1 = ads.read(data_1,readtype) #读取数值

        if type(data_2) == str:
            temp_2 = ads.read(data_2,readtype) #读取数值
        else: 
            temp_2 = data_2
        temp_2 = type(temp_1)(temp_2)              
        #判断
        if temp_1 <  temp_2: #满足条件           
            is_less = True   
        return is_less


    def checkLess(self,data_1,data_2, readtype = 1):
        is_less = False
        temp_1 = ads.read(data_1,readtype) #读取数值

        if type(data_2) == str:
            temp_2 = ads.read(data_2,readtype) #读取数值
        else: 
            temp_2 = data_2
        temp_2 = type(temp_1)(temp_2)   
        if temp_1 <  temp_2: #满足条件
            data = '     PASS:IS Less , %s(%s) < %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))    
            is_less = True
        else :
            data = 'ERROR:IS not Less , %s(%s) > %s(%s)'%(data_1,str(temp_1),str(data_2),str(temp_2))
        #数值写入
        report(data)
        return is_less
    
