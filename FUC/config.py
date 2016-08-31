# -*- coding: utf-8 -*-
import ConfigParser,re,logging
logger_config = logging.getLogger('main.config')

cf = ConfigParser.ConfigParser()
configFile = '.\config.ini'
cf.read(configFile)



def getTemp(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('TEMP', option)
        data = unicode(data,'gbk')
    except Exception,e:
        logger_config.warn(str(e))
        data = ''
    return data


def saveTemp(option,value):
    try:
        cf.read(configFile)
        section = 'TEMP'
        cf.set(section, option,str(value))
        cf.write(open(configFile,'w')) 
    except Exception,e:
        logger_config.warn(str(e))   
        
def getConfig(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('CONFIG', option)
        data = unicode(data,'gbk')
    except Exception,e:
        logger_config.warn(str(e))
        data = ''
    return data    

def saveConfig(option,value):
    try:
        cf.read(configFile)
        section = 'CONFIG'
        cf.set(section, option,str(value))
        cf.write(open(configFile,'w')) 
    except Exception,e:
        logger_config.warn(str(e))
    
def reflashConfig():
    global PLC_IP,PLC_PORT,METHOD,PLATFORM,NI_IP,NI_PORT,PARAMDIR
    PLC_IP = getConfig('PLC_IP')
    PLC_PORT = getConfig('PLC_PORT')
    METHOD = int(getConfig('method'))
    PLATFORM = int(getConfig('platForm'))
    NI_IP = getConfig('NI_IP')
    NI_PORT = getConfig('NI_PORT')
    PARAMDIR = getConfig('PARAMDIR')
    
    
def saveCurrentConfig():
    global PLC_IP,PLC_PORT,METHOD,PLATFORM,NI_IP,NI_PORT,PARAMDIR
    saveConfig('PLC_IP',PLC_IP)
    saveConfig('PLC_PORT',PLC_PORT)
    saveConfig('platForm',PLATFORM)
    saveConfig('NI_IP',NI_IP)
    saveConfig('NI_PORT',NI_PORT)
    saveConfig('PARAMDIR',PARAMDIR)
    
reflashConfig()