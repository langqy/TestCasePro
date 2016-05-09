#!Python
#coding=gbk
__version__ = "$Id$"
from sys import path  #�����µ�PATH
path.append(r"..\\")
import os,time
from PAR import parm
from ctypes import *
IP = parm.Constant.IP
NIIP = parm.Constant.NiIP
#path =  os.getcwd()
PATH = './/DLL'
#dll =CDLL('./DLL/x_ide_for_python.dll')


#��ö�Ӧ��������     
def adsGetType(name):
    try:
        cmd_path = 'cmd /k cd /d %s' %PATH        
        
        info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe /t %s %s' %(PATH,IP,name)).read()          
        info =info.replace('\n','\t')
        data = info.split('\t')               
        return data[2]
    except Exception,e:
        print e
        return False
    
#��ȡ��Ҫд���ֵת��Ϊ������Ӧ������
def adsTurnType(name,data):    
    try:
        vartype = adsGetType(name)
        #print vartype
        if vartype[-3:] == "INT":       #int��
            data = int(data)
        elif vartype[-4:] == "REAL":    #real��Ӧfloat��
            
            data = float(data)
            #data = '%.3f'%data   #С��λ���3λ
        elif vartype == "BOOL":         #Bool��
            data = bool(int(data))
            #print "it is a bool"
        else:  
            data = str(data)            #�ַ�����������
        return data
    except Exception,e:
        print e,"turn type",name
        return data
    
#adsͨ����ȡ
def adsRead(name):
    try:
        cmd_path = 'cmd /k cd /d %s' %PATH        
        info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe /r %s %s' %(PATH,IP,name)).read()
        #print 'INFO',info,cmd_path,name
        info =info.replace('\n','\t')
        data = info.split('\t')
        #print data
        #print 'DATA',len(data),data    
        ver = data[2]
        return adsTurnType(name,ver)   #��ȡ���ݺ�Ҫ�޸���������
    except Exception,e:
        print e,";the connection is time out",name
        return False
    
#adsͨ��д�����
def adsWrite(name,var,sign = "/nocheck /nomsgbox"):
    try:
        adsTurnType(name,var)   #д��ǰ��ת����������
        #print name,var,sign
        cmd_path = 'cmd /k cd /d %s' %PATH
        Tab ='     '
        info = os.popen('cd "%s" & cmd /k Envision.Tools.TcAds.VariableCmd.exe %s /w %s %s %s' %(PATH,sign,IP,name,var)).read()
        time.sleep(0.01)
    except Exception,e:
        print name
        print e,";the connection is time out",name
        


        

##��NI��ȡ����ֵ������        
#def niReadVarAndType(name):
    #try:
        
        #t = dll.Get_Data
        #t.restype = c_char_p
        #a = t(IP,name)
        #print a
        #datalist = a.split(',')
        #return datalist
    #except Exception,e:
        #print e
        #return ''
def niReadVarAndType(name):
    try:
        
        name = "\""+name +"\""     
        cmd_path = 'cmd /k cd /d %s' %PATH        
        info = os.popen('cd "%s" & cmd /k XIDE.exe 0 %s %s' %(PATH,NIIP,name)).read()
        info  = info.replace('\n',' ')
        data = info.split(' ')
        return data[:2]
    except Exception,e:
        print e    
    
#NIͨ������ת������  
def niTurnType(data,datatype):
    try:
        if datatype == "boolean":
            print datatype
            return bool(int(float(data)))
        elif datatype == "double":
            
            print datatype
            return float(data)
        else:
            print "Unknow Type"           
    except Exception,e:
        print e            
        
#NIͨ����ȡ����
def niRead(name):
    try:
        info = niReadVarAndType(name)
        print info
        if len(info):
            datatype,data = info
            print data,datatype
            data = niTurnType(data,datatype)
            return data
        print "conncet Faild" 
    except Exception,e:
        print e

#��NI��ȡ����ֵ������#NIͨ��д�뺯��        
#def niWrite(name,data):      
    #try:
        
        #t = dll.Set_Data
        #a = t(IP,name,str(data))
        #return a
    #except Exception,e:
        #print "ERROR:",e      
def niWrite(name,data):          
    try:
        cmd_path = 'cmd /k cd /d %s' %PATH   
        name = "\""+name +"\""
        info = os.popen('cd "%s" & cmd /k XIDE.exe 1 %s %s %s' %(PATH,NIIP,name,data)).read()
        info  = info.replace('\n',' ')
        data = info.split(' ')
        print info
    except Exception,e:
        print e      
        
        
def read(name,readtype = 1):
    if readtype:
        return adsRead(name)
    elif not readtype:
        return niRead(name)
    else:
        print "ERROR: WRONG INPUT TPYE! PLEASE CHECK THE SECOND ARG"
        return None
    
def write(name,var,writetype  = 1):
    if writetype:
        adsWrite(name,var)
    elif not writetype:
        niWrite(name,var)
    else:
        print "ERROR: WRONG INPUT TPYE! PLEASE CHECK THE THIRD ARG"
            
    
if __name__ == '__main__' :
    IP = '172.16.43.188.1.1:801'
    name = 'PRG_SC04_02_143.fbPowerUpReset.ET'
    for i in (1,10000):
        
        write('.grParameterEnvision_12', 200)
        write('.grParameterEnvision_13', 300)
        write('.grParameterEnvision_14', 800)
        write('.grParameterEnvision_15', 1000)
        write('.grParameterEnvision_16', 0)
        write('.grParameterEnvision_17', -2)
        write('.grParameterEnvision_18', -2)
        write('.grParameterEnvision_19', -2)
        
        write('.grParameterEnvision_26',  0)
        write('.grParameterEnvision_27',  0)
        write('.grParameterEnvision_28',  0)
        write('.grParameterEnvision_29',  1)
        write('.grParameterEnvision_30',  1)
        
        write('.grParameterEnvision_32',  1)
        write('.grParameterEnvision_33',  1)
        write('.grParameterEnvision_34',  1)
        write('.grParameterEnvision_35',  1)
        write('.grParameterEnvision_36',  1)
        
        write('.grParameterEnvision_37',  1)
        write('.grParameterEnvision_38',  2.5)
        
        write('.grParameterEnvision_47',  1)
        write('.grParameterEnvision_48',  0)
        write('.grParameterEnvision_49',  1)
        write('.grParameterEnvision_50',  0)


           
            
