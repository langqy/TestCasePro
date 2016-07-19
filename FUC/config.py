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
    

IP = getConfig('IP')
PORT = getConfig('PORT')
METHOD = getConfig('method')
PLATFORM = getConfig('platForm')
NI_IP = getConfig('NI_IP')
NI_PORT = getConfig('NI_PORT')