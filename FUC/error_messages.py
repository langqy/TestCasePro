# -*- coding: utf8 -*- 
from __future__ import division
from sys import path  #增加新的PATH
path.append(r"..\\")
from FUC.function import *


class DivisionException(Exception):
      def __init__(self, ver,data):
            Exception.__init__ (self,ver,data)       #调用基类的__init__进行初始化
            print "writer fail"
            report("ERROR:"+str(ver)+"__writer__"+str(data)+"__fail")

#通讯中断
ERROR_1 = "communication is broken"
#文件查找错误
ERROR_2 = "File lookup failure"
#数据格式错误
ERROR_3 = "Error data type"
#数据值错误
ERROR_4 = "Error data var"
#未知错误
ERROR_99 = "Error ,but I don't know why Error"