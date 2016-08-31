# -*- coding: utf-8 -*-
from ctypes import *
import os,time
import logging
logger_ads = logging.getLogger('main.ads')
from FUC import config
import platform
from  PyQt4.QtGui import QMessageBox

########################################################################

class adsClass:
    """ads通讯库"""

    #----------------------------------------------------------------------
    def __init__(self):
        """
        通讯库初始化        
        """
        self.PATH = './/DLL'
        self.setup_ok = False
        
    def setup(self, IP = '',PORT = "", method = 1 , platForm = 1, NI_IP ='',NI_PORT = 0, readFromIni = False):
        """
        ams_id 被测PLC ip地址
        method 通讯方式 1 为 CMD ，2 为 DLL
        platform 测试平台  1 为 SIL，2 为 HIL
        ni_ip NI台架IP， 仅在platform = 2 情况下生效      
	readFromIni  是否从config.ini文件读取配置信息 True 为读取 False 为不读取
        """
	if readFromIni:
	    self.PLC_IP = str(config.PLC_IP)
	    self.PLC_PORT = str(config.PLC_PORT)
	    self.method = int(config.METHOD)
	    self.platForm = int(config.PLATFORM)
	    self.NI_IP = str(config.NI_IP)  
	    self.NI_PORT = int(config.NI_PORT)  
	else:
	    self.PLC_IP = IP
	    self.method = method
	    self.platForm = platForm
	    self.NI_IP = NI_IP
	    self.NI_PORT = NI_PORT  

	windowsType = platform.architecture()
	WinBit = windowsType[0]		
	print WinBit	
	try:
	    if self.method == 2:

		if WinBit == '32bit':
		    self.DLLDIR ='./Dll/x32/TESTDLL.dll' 
		    logger_ads.info(u"读取32位版本DLL")
		else:
		    self.DLLDIR ='./Dll/x64/TESTDLL.dll'
		    logger_ads.info(u"读取64位版本DLL")
	    if self.platForm == 2:
		if WinBit == '32bit':
		    self.NIDLLDIR ='./Dll/x32/HiLab.DataManager_x32.dll'
		    logger_ads.info(u"读取32位NI版本DLL")
		else:
		    self.NIDLLDIR ='./Dll/x64/HiLab.DataManager_x64.dll'
		    logger_ads.info(u"读取64位NI版本DLL")		

	    self.setup_ok = True
	except Exception,e:
	    print e
	    logger_ads.exception(str(e))
	    self.setup_ok = False
	    
    def read(self,name,port = ""):
	if port  == "":
	    self.AMS_ID = "%s.1.1:%s"%(self.PLC_IP,self.PLC_PORT)
	else:
	    self.AMS_ID = "%s.1.1:%s"%(self.PLC_IP,port)	    
	name = str(name).strip()
	if name == '':
	    print 'the value is None' 
	    return None	
	if self.platForm == 1:	   
	    if self.method == 1:
		data = self.adsReadCmd(name)
		logger_ads.info("ADS CMD read '%s':%s"%(name,str(data)))
	    elif self.method == 2:
		data = self.adsReadDll(name)
		logger_ads.info("ADS DLL read '%s':%s"%(name,str(data)))
	    else:
		#print 'ads communication method did not set currect.'
		strword =  'ads communication method did not set currect.'
		logger_ads.exception(strword)		
		return None	    
	elif self.platForm == 2:
	    if  name[:7] == 'Targets'  : #暂定以NI为开头 且无‘.'符号为仿真变量
		data = self.niRead(name,1)
		logger_ads.info("ADS NI read '%s':%s"%(name,str(data)))
	    elif name[:3] == 'hil' :
		data = self.niRead(name,2)
		logger_ads.info("ADS NI read '%s':%s"%(name,str(data)))		
	    else:
		if self.method == 1:
		    data = self.adsReadCmd(name)
		    logger_ads.info("ADS CMD read '%s':%s"%(name,str(data)))
		elif self.method == 2:
		    data = self.adsReadDll(name)
		    logger_ads.info("ADS DLL read '%s':%s"%(name,str(data)))
		else:
		    #print 'ads communication method did not set currect.'
		    strword =  'ads communication method did not set currect.'
		    logger_ads.exception(strword)		    
		    return None	    
	
	return data	
    
    def write(self,name,data,port = ""):
	if port  == "":
	    self.AMS_ID = "%s.1.1:%s"%(self.PLC_IP,self.PLC_PORT)	
	else:
	    self.AMS_ID = "%s.1.1:%s"%(self.PLC_IP,port)
	ret = False
	name = str(name).strip()
	if name == '':
	    print 'the value is None' 
	    return ret	
	if self.platForm == 1:	   
	    if self.method == 1:
		ret = self.adsWriteCmd(name,data)
		logger_ads.info("ADS CMD write '%s':%s"%(name,str(data)))
	    elif self.method == 2:
		ret = self.adsWriteDll(name,data)
		logger_ads.info("ADS DLL write '%s':%s"%(name,str(data)))
	    else:
		strword =  'ads communication method did not set currect.'
		logger_ads.exception(strword)
		return False
	elif self.platForm == 2:
	    
	    if  name[:7] == 'Targets'  : #暂定以NI为开头 且无‘.'符号为仿真变量
		ret = self.niWrite(name,data,1)
		logger_ads.info("ADS NI write '%s':%s"%(name,str(data)))
		return ret
	    elif name[:3] == 'hil' :
		ret = self.niWrite(name,data,2)
		logger_ads.info("ADS NI write '%s':%s"%(name,str(data)))
		return ret	    
	    else:
		if self.method == 1:
		    ret = self.adsWriteCmd(name,data)
		    logger_ads.info("ADS CMD write '%s':%s"%(name,str(data)))
		elif self.method == 2:
		    ret = self.adsWriteDll(name,data)
		    logger_ads.info("ADS DLL write '%s':%s"%(name,str(data)))
		else:
		    strword =  'ads communication method did not set currect.'
		    logger_ads.exception(strword)			    
	return ret

        
    def adsReadCmd(self,name):
        """CMD方式读取变量值"""
        try:
            if self.setup_ok:
                info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe /r %s %s' %(self.PATH,self.AMS_ID,name)).read()
                info =info.replace('\n','\t')
                data = info.split('\t')
                ver = data[2]
                return self.adsTurnTypeCmd(name,ver)   #读取数据后要修改数据类型
            else:
                strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
		
                return None
        except Exception,e:
	    logger_ads.exception(str(e))
            print e,";the connection is time out",name
        return None        
    
        
    def adsGetTypeCmd(self,name):
        """CMD方式获取变量类型"""
        try:
            if self.setup_ok:           
                info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe /t %s %s' %(self.PATH,self.AMS_ID,name)).read()          
                info =info.replace('\n','\t')
                data = info.split('\t')               
                return data[2]
            else:
		strword =  'IP and method did not be set.'
		logger_ads.exception(strword)	
                return False
        except Exception,e:
            print e
	    logger_ads.exception(str(e))
            return False        
        
    def adsTurnTypeCmd(self,name,data):
        """根据变量原始类型进行数据类型转换"""
        try:
            if self.setup_ok: 
                vartype = self.adsGetTypeCmd(name)          
                if vartype[-3:] == "INT":       #int型
                    data = int(data)
                elif vartype[-4:] == "REAL":    #real对应float型
                    
                    data = float(data)
                    data = '%.4f'%data   #小数位最多3位
                elif vartype == "BOOL":         #Bool型
                    data = bool(int(data))
    
                else:  
                    data = str(data)            #字符串或者其他
                return data
            else:
                strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
                return data                
            
        except Exception,e:
            print e
	    logger_ads.exception(str(e))
            return None        
    
    def adsWriteCmd(self,name,data,sign = "/nocheck /nomsgbox"):
        """CMD方式写变量值"""
        try:
            if self.setup_ok:   
		
                info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe %s /w %s %s %s' %(self.PATH,sign,self.AMS_ID,name,data)).read()
                time.sleep(0.01)
                return True
            else:
                strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
                return False
        except Exception,e:
            print e
	    logger_ads.exception(str(e))
            return False            
        
    def adsReadDll(self,name):
        """DLL方式读取变量值"""
        try:
            if self.setup_ok:           
                dll = cdll.LoadLibrary(self.DLLDIR)
                dll.AdsSingleRead.restype = c_char_p               
                name = name.strip()
                ret = dll.AdsSingleRead(self.AMS_ID,name)  
                dll = None
                if ret == ";" or ret == '':
		    strword =  'Can not read %s.'%name
                    logger_ads.error(strword)
                    return None
                else:
                    dataAndType = ret.split(';')
                    datatype = dataAndType[1]
                    recdata = dataAndType[0]
                    data = self.adsturnTypeDll(recdata,datatype)
                    return data
            else:
                strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
                return None
        except Exception,e:
            print e
	    logger_ads.exception(str(e))
            return None     
	
    def adsGetTypeDll(self,name):
	"""DLL方式读取变量类型"""
	try:
	    if self.setup_ok:           
		dll = cdll.LoadLibrary(self.DLLDIR)
		dll.AdsSingleRead.restype = c_char_p               
		name = name.strip()        
		ret = dll.AdsSingleRead(self.AMS_ID,name)  
		if ret == ";" or ret == '':            
		    return None
		else:
		    dataAndType = ret.split(';')
		    datatype = dataAndType[1]
		    return datatype
	    else:
		strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
		return None
	except Exception,e:
	    print e
	    logger_ads.exception(str(e))
	    return None                   
        
    def adsWriteDll(self,name,data):
        """DLL方式写变量值"""
        try:
            if self.setup_ok:           
                dll = cdll.LoadLibrary(self.DLLDIR)
		dll.AdsSingleRead.restype = c_char_p                 
		name = name.strip()
		ret = dll.AdsSingleWrite(self.AMS_ID,name,str(data)) 
		dll = None
		if ret == "-1":
		    return False
		return True
            else:
                strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
                return False
        except Exception,e:
            print e
	    logger_ads.exception(str(e))
            return False    	
	
    def adsturnTypeDll(self,name,datatype):
	"""类型转换"""
	if datatype[0] == "I" or datatype[0] == "U" or datatype[0] == "T" or datatype[0] == "B":
	    name = int(name)
	elif datatype[0] == "F" or datatype[0] == "D":
	    name = float(name)
	    name = round(name,3)
	elif datatype[0] == "B":
	    name = bool(name)
	elif datatype[0] == "S":
	    name = str(name)
	else: 
	    print "The type is not available"
	return name    
    
    def niReadVarAndType(self,name):
	'''NI台架通讯 读取变量值及类型'''
	try:
	    if self.setup_ok:  
		dll = cdll.LoadLibrary(self.NIDLLDIR)		
		t = dll.Get_Data
		t.restype = c_char_p
		a = t(self.NI_IP,name)
		datalist = a.split(',')
		return datalist
	    else:
		strword =  'IP and method did not be set.'
		logger_ads.exception(strword)
		return ''		
	except Exception,e:
	    print e
	    logger_ads.exception(str(e))
	    return ''	
	
    def niTurnType(self,data,datatype):
	'''NI台架通讯 类型转换'''
	try:
	    if datatype == "boolean":
		return bool(int(float(data)))
	    elif datatype == "double":
		return float(data)
	    else:
		print "Unknow Type"           
	except Exception,e:
	    print e	
	    logger_ads.exception(str(e))
	    
    def niRead(self,name,nitype,modelName = ''):
	'''NI台架通讯 读取变量值''' 
	try:
	    value = c_char_p(' ')
	    dll = cdll.LoadLibrary(self.NIDLLDIR)
	    if nitype ==1 :        
		a = dll.HiLab_GetData(self.NI_IP,self.NI_PORT,name,value)
	    elif nitype == 2:
		if modelName == '':
		    modelname = self.getModelName(name)
		else:
		    modelname = modelName
		a = dll.Model_GetParameter(self.NI_IP,self.NI_PORT,modelname,name,value)
	    dll = None
	    if a == 0:
		return value.value 
	    else:
		return None
	    
	except Exception,e:
	    print e
	    logger_ads.exception(str(e))
	    return None

    def niWrite(self,name,data,nitype,modelName = ''):  
	'''NI台架通讯 写入变量值'''
	try:    
	    if self.setup_ok:  
		dll = cdll.LoadLibrary(self.NIDLLDIR)
		if nitype ==1 :
		    setData = dll.HiLab_SetData		    
		    setData(self.NI_IP,self.NI_PORT,name,0,str(data))
		    return True
		if nitype == 2:
		    setData = dll.Model_SetParameter
		    if modelName == '':
			modelname = self.getModelName(name)
		    else:
			modelname = modelName
		    setData(self.NI_IP,self.NI_PORT,modelname,name,str(data)) 
		    return True	
	    else:
		strword =  'Please setup the ni_ip.'
		logger_ads.exception(strword)		
		return  False    
	except Exception,e:
	    print e  
	    logger_ads.exception(str(e))
	return False
    
    def getModelName(self,name):
	modelName = ''
	name = str(name)
	if name != '':
	    modelName = name.split('/')[1]
	return modelName
    
    def unlock(self,name):
	try: 
	    if self.setup_ok:  
		dll = cdll.LoadLibrary(self.NIDLLDIR)		   
		t = dll.HiLab_ClearDataHandle
		t(self.NI_IP,self.NI_PORT,name)	
	    else:
		strword =  'Please setup the ni_ip.'
		logger_ads.exception(strword)		
		return  False  	
	except Exception,e: 
	    print 'err'
	    logger_ads.exception(str(e))	
	
ads = adsClass()
ads.setup(readFromIni= True)

    
if __name__ == '__main__':

    
    #comm = adsClass()
    AMS_ID = "172.16.43.185.1.1:801"
    method=2
    platform=1
    #comm.setup(AMS_ID)
    name = '.gsControlCodeBuildNo'
    ##log.logger_main.info('read %s'%name)
    #a=  comm.read(name)
    #print a
    ##data = 'SC1_2016A.2205.SiteTest1'
    
    ##log.logger_main.info('write %s %s'%(name,data))
    ##a= comm.write(name, data)
    #print a
    #print comm.read(name)
    #DLLDIR = '../Dll/x64/TESTDLL.dll'
    #dll = cdll.LoadLibrary(DLLDIR)
    #dll.AdsSingleRead.restype = c_char_p    
    #a = dll.AdsSingleRead(AMS_ID,name)
    ads = adsClass()
    ads.AMS_ID = AMS_ID
    ads.method = 2
    ads.platForm = 1
    ads.setup_ok = True
    ads.DLLDIR = '../Dll/x64/TESTDLL.dll'
    a = ads.read(name)
    print a