# -*- coding: utf8 -*- 
import time,os
from FUC import config
import logging
logging_report = logging.getLogger('main.report')
PATH = '.\Reports'

def timeSign(signal = 1):
    
    """
    时间戳
    1为报告中时间戳格式
    2为文件名
    """
    if signal == 1:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    elif signal == 2:        
        return time.strftime("%Y%m%d_%H-%M-%S", time.localtime()) 

strfilename = r"Reports/%s.txt"%timeSign(2)

    
def writeToTxt(var, withTime = True):
    try:
        #以在结尾写入模式打开文件    
        
        #数据整合 时间戳+3个空格+入参+回车
        if withTime:
            if var[:5] == 'ERROR' or var[:5] == 'Error' or var[:5] == 'error': # 
                data ='   '+'!!!'+timeSign() + '   ' + var + '!!!\n' 
            else:
                data ='      '+timeSign() + '   ' + var + '\n' 
        else:
            data =var + '\n' 


        #写入数据 
        with open(strfilename,'a') as fp:
            fp.write(data)  
            
    except Exception,e:
        logging_report.exception(str(e))
  
        
#写入报告    
def report(data, withTime = True):  
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    #logging_report.info(data)
    print data
    writeToTxt(data,withTime)