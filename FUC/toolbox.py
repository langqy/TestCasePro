# -*- coding: utf8 -*- 
from FUC.report import report
from FUC.error_messages import *
from FUC.communication import ads
from FUC.assertFuc import *
import time,string
import re


box = assertFun()

#截止印记  ,入参为开始时间，截止时间
def end_stamp(start,end):
    try: 
        usetime = end - start
    except:
        report("end_stamp:"+ERROR_3)#错误信息：格式错误
    try:
        data = 'use time:'+ str(usetime)  #格式整理
        report(data,False) #打印至文件
        #print "end_stamp:ok"
    except:
        report("end_stamp:"+ERROR_2) #打印错误至报告:文件查找错误


#等待延时，入参1,2 当1=2时，返回True,默认时间30S,默认步长0.5s
#check_type:1 = ,2 >,3 < 默认模式为等于
def check_timeout(data_1,data_2,check_type = 1,time_limit = 30,time_step = 0.5):
    try:
        start = time.time()
        while(time_limit>0): #循环，时长由time_limit确定
            if (check_type == 1):
                if (box.isEqual(data_1, data_2)): #判断是否符合条件
                    return True   
            elif(check_type == 2):
                if(box.isGreater(data_1, data_2)):
                    return True
            elif(check_type == 3):
                if(box.isLess(data_1, data_2)):
                    return True  
            else:
                report("check_timeout:"+ERROR_4) #数据值错误，无该判断类型
                return False
            time.sleep(time_step)#延时
            time_limit -= (time.time()-start)#降低时长
            start = time.time()
        report("check_timeout Time out")
        return  False
    except:
        report("check_timeout"+ERROR_99)#未知错误

#手动复位.
def reset(name):
    try:
        start = ads.read(name) #存储初值
        if start == "1" or start == 1:#取反值
            end = 0
        else:
            end = 1;
        ads.write(name, end) #复位动作
        time.sleep(0.5)
        ads.write(name,start)
        time.sleep(0.5)
        ads.write(name, end)
        time.sleep(0.5)
        ads.write(name, start) #数据还原
    except:
        report("reset:"+name+"   "+ERROR_1)#复位失败，通信错误.
    

def EA_Get_ID(data):
    try:
        ID = re.findall(ID_rule,data)
        return ID[0]
    except:
        return False

def EA_Get_State(data):
    try:
        name = re.findall('[S|O][\S]{5,}',data)
        return name[0]
    except:
        return False    