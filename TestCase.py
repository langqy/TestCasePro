# -*- coding: utf-8 -*-

"""
Module implementing TestCasePro.
"""
import logging 
import logging.config
import sys
LOG_FILE = './testCase.log'
#输出到屏幕   
ch = logging.StreamHandler() 
#写入文件实例化
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
fmt = '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'

formatter = logging.Formatter(fmt)   # 实例化formatter
handler.setFormatter(formatter)      # 为handler添加formatter
logger_main = logging.getLogger('main')    # 获取名为tst的logger
logger_main.addHandler(handler)           # 为logger添加handler
#logger_main.addHandler(ch)
logger_main.setLevel(logging.DEBUG)

from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature,QDir,Qt,QTextCodec

from Ui_TestCase import Ui_TestCasePro
import os
from FUC import config,report
import workThread

class TestCasePro(QMainWindow, Ui_TestCasePro):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QTextCodec.setCodecForCStrings(QTextCodec.codecForName('gbk'))
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.caseDir = ''
        self.selectedCaseList = []
        self.caselist = []
        self.paramlist = []
        self.bcasePause = False
        self.idoneCaseIndex = -1
        self.idoneCaseIndex = 0
        self.reportFileName = ''
        self.treeWidget_caseTree.itemChanged.connect(self.treehandleChanged)
        #设置table的列宽
        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1,70)
        self.tableWidget_caseList.setColumnWidth(0,150)  
        self.getCommunicationConfig()
        self.casethread = workThread.autotest()
        self.casethread.sinOut1.connect(self.currentRunIndex)
        self.casethread.sinOut2.connect(self.process)
        self.casethread.sinOut3.connect(self.stopIndex)
        self.casethread.sinOut4.connect(self.endResult)
        self.casethread.sinOut5.connect(self.getReportFile)
        
        self.pushButton_start.setEnabled(False)
        self.pushButton_pause.setEnabled(False)
        try: 
            self.caseDir = config.getTemp('caseDir')
            
            if self.caseDir != '':
                self.updateTree(self.caseDir)

        except Exception,e:
            print e
            
        
    def getCommunicationConfig(self):
        config.reflashConfig()
        self.lineEdit_PLCIP.setText(config.PLC_IP)
        self.lineEdit_PLCPORT.setText(config.PLC_PORT)
        self.lineEdit_NIIP.setText(config.NI_IP)
        self.lineEdit_NIPORT.setText(config.NI_PORT)
        
        if config.PLATFORM == 1:
            self.radioButton_SIL.setChecked(True)
        elif config.PLATFORM == 2:
            self.radioButton_HIL.setChecked(True)
        currentDir = unicode(QDir.currentPath(),'gbk')
        PARAMDIR = os.path.join(currentDir,config.PARAMDIR)
        templist = os.listdir(PARAMDIR)
        paramlist = []
        for param in  templist:
            if param[-3:] == '.py' and 'PARAM'  in param.upper():
                paramlist.append(param)
        print paramlist
        if len(paramlist) != 0:
            self.comboBox_paramName.clear()
            self.paramlist = paramlist
            self.comboBox_paramName.addItems(paramlist)
            paramFileName = config.getTemp('paramSelect')
            if paramFileName != '':
                fileName = paramFileName + '.py'
                if fileName in  self.paramlist:
                    index = self.paramlist.index(fileName)
                    self.comboBox_paramName.setCurrentIndex(index)
            
    def saveCommunicationConfig(self):
        config.NI_IP = self.lineEdit_NIIP.text()
        config.NI_PORT = self.lineEdit_NIPORT.text()
        config.PLC_IP = self.lineEdit_PLCIP.text()
        config.PLC_PORT = self.lineEdit_PLCPORT.text()
        if self.radioButton_SIL.isChecked() :
            config.PLATFORM = 1
        elif self.radioButton_HIL.isChecked():
            config.PLATFORM = 2
        paramName =  str(self.comboBox_paramName.currentText()).replace('.py','')
        config.saveTemp('paramselect', paramName)
        config.saveCurrentConfig()
    
    @pyqtSignature("")
    def on_radioButton_HIL_clicked(self):
        config.PLATFORM = 2
        self.lineEdit_NIIP.setEnabled(True)
        self.lineEdit_NIPORT.setEnabled(True)        
    
    @pyqtSignature("")
    def on_radioButton_SIL_clicked(self):
        """
        Slot documentation goes here.
        """
        config.PLATFORM = 1  
        self.lineEdit_NIIP.setEnabled(False)
        self.lineEdit_NIPORT.setEnabled(False)
    
    
    @pyqtSignature("")
    def on_pushButton_getConfig_clicked(self):
        self.getCommunicationConfig()
    
    @pyqtSignature("")
    def on_pushButton_saveConfig_clicked(self):
        self.saveCommunicationConfig()
    
    @pyqtSignature("")
    def on_pushButton_getCase_clicked(self):
        """
        获取用例
        """
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        caseCount = len(self.caselist)
        self.label_totalCaseCount.setText(u'共计 %s 个用例 '%caseCount)
        if  caseCount == 0:
            return
        for casepath in self.caselist:
            currentRow = self.tableWidget.rowCount()
            casename = os.path.basename(casepath)            
            self.tableWidget.insertRow(currentRow)
            self.tableWidget.setItem(currentRow  ,0, QTableWidgetItem(casename))
            self.tableWidget.setItem(currentRow  ,1, QTableWidgetItem(u'未执行'))
            self.tableWidget.setItem(currentRow  ,2, QTableWidgetItem(casepath))
        self.pushButton_start.setEnabled(True)   
            
    @pyqtSignature("")
    def on_pushButton_start_clicked(self):
        """
        用例运行接口
        """
        self.currentIndex = 0
        paramFileName = str(self.comboBox_paramName.currentText()).replace('.py','')
        config.saveTemp('paramSelect', paramFileName)
        self.casethread.runTest(self.caselist,paramFileName)
        self.pushButton_pause.setEnabled(True)
        self.pushButton_stop.setEnabled(True)
        self.pushButton_getCase.setEnabled(False)
        self.pushButton_start.setEnabled(False)

    
    @pyqtSignature("")
    def on_pushButton_stop_clicked(self):
        """
        停止
        """
        self.casethread.stop()
        self.currentIndex = 0
        #self.pushButton_pause.setEnabled(False)
        #self.pushButton_start.setEnabled(True)
        #self.pushButton_getCase.setEnabled(True)
    
    @pyqtSignature("")
    def on_pushButton_pause_clicked(self):
        """
        暂停与继续
        """
        self.bcasePause = not self.bcasePause    
        self.casethread.pause(self.bcasePause) 
        if  self.bcasePause:
            self.pushButton_pause.setText(u'继续')
            self.tableWidget.setItem(self.currentIndex + 1  ,1, QTableWidgetItem(u'暂停'))
            self.setRowColor(self.currentIndex + 1,QColor(187,112,112))
        else:
            self.pushButton_pause.setText(u'暂停')
            self.setRowColor(self.currentIndex + 1,QColor(255,255,255))        
        print self.bcasePause
        #self.currentRunIndex(self.currentIndex+1)

    @pyqtSignature("")
    def on_pushButton_report_clicked(self):
        """
        打开报告
        """
        if os.path.exists(self.reportFileName):
            os.popen("start %s" % self.reportFileName).read()        
    
    def currentRunIndex(self,index):
        self.currentIndex = index
        self.tableWidget.setItem(index  ,1, QTableWidgetItem(u'正在执行'))
        self.setRowColor(index, QColor(185,185,255))
    
    def process(self, index , result):
        if result == 1:
            data = u'通过'     
            color = QColor(204,255,128)
        elif result == 2:
            data = u'失败'
            color = QColor(255,45,45)
        else:
            data = u'异常'
            color = QColor(255,255,170)
        self.tableWidget.setItem(index,1, QTableWidgetItem(data))
        self.idoneCaseIndex = index
        self.setRowColor(index,color)
        self.label_progress.setText('%d/%d'%(index+1,len(self.caselist)))
    
    def stopIndex(self,index):
        self.setRowColor(index, QColor(255,0,0))
    
    def endResult(self,resultList):
        through,failure,error = resultList
        self.label_faild.setText(str(failure))
        self.label_pass.setText(str(through))        
        un = len(self.caselist) - int(through + failure)
        print un
        self.label_unexecuted.setText(str(un))
        self.pushButton_start.setEnabled(True)
        self.pushButton_getCase.setEnabled(True)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_stop.setEnabled(False)
        
        
    def setRowColor(self,row,color):
        for col in xrange(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row,col)
            item.setBackgroundColor(color)
    
    def getReportFile(self,filename):
        self.reportFileName = unicode(filename,'gbk')
        print "get report file name", self.reportFileName
        
    @pyqtSignature("")
    def on_pushButton_back_clicked(self):
        """
        上一页
        """
        self.tabWidget_caseSelect.setCurrentIndex(0)
    
    @pyqtSignature("")
    def on_pushButton_next_clicked(self):
        """
        下一页
        """
        self.tabWidget_caseSelect.setCurrentIndex(1)
    
    @pyqtSignature("")
    def on_action_getconfig_triggered(self):
        """
        读取配置
        """
        self.getCommunicationConfig()
    
    @pyqtSignature("")
    def on_action_saveconfig_triggered(self):
        """
        保存配置
        """
        self.saveCommunicationConfig()
    
    @pyqtSignature("")
    def on_action_close_triggered(self):
        """
        Slot documentation goes here.
        """
        if not self.casethread.bStoped:
            ret = QMessageBox.warning(self,u'警告',u'用例正在执行中，请确认是否关闭本程序',QMessageBox.Yes, QMessageBox.No)
            if ret == QMessageBox.No:
                return 
            else:
                self.casethread.stop()
        self.close()
    
    @pyqtSignature("")
    def on_action_Version_triggered(self):
        """
        版本信息.
        """
        QMessageBox.information(self,'VERSION',"Version: %s\nEdited by lianjun.yao\n2016.07.29"%config.getConfig('VERSION'))
    
    @pyqtSignature("")
    def on_action_log_triggered(self):
        """
        Slot documentation goes here.
        """
        if os.path.exists(LOG_FILE):
            open('log.txt','w').write(open(LOG_FILE,'r').read())
            print os.popen("start log.txt" ).read() 
    
    @pyqtSignature("")
    def on_action_cleanlog_triggered(self):
        """
        Slot documentation goes here.
        """
        with open(LOG_FILE,'w') as f:
            f.write('')
            
    
    
    @pyqtSignature("int")
    def on_tabWidget_caseSelect_currentChanged(self, index):
        """
        上一步下一步的使能
        """
        if index == 0:
            self.pushButton_back.setEnabled(False)
            self.pushButton_next.setEnabled(True)
        elif index == 1:
            self.pushButton_back.setEnabled(True)
            self.pushButton_next.setEnabled(False)
    
#############################################
##        tableWidget_caseList操作         ##
#############################################
        
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        + 将选择的case名移到表格
        """
        for casepath in self.selectedCaseList:
            if casepath not in self.caselist:
                self.caselist.append(casepath)
        self.tableWidget_caseList_update()
                
            
        #self.tableWidget_caseList.update()
    
    @pyqtSignature("")
    def on_pushButton_removeOne_clicked(self):
        """
        - 删除单行case列表
        """        
        selectedItems =  self.tableWidget_caseList.selectedItems()
        if len(selectedItems) != 0:
            for item in selectedItems:
                if item.column() == 1:
                    casepath = unicode(item.text(),'gbk')
                    self.caselist.remove(casepath)
        self.tableWidget_caseList_update()
    
    @pyqtSignature("")
    def on_pushButton_removeAll_clicked(self):
        """
        清空case列表
        """
        self.tableWidget_caseList.clearContents()
        self.caselist = []
        
    @pyqtSignature("")
    def on_pushButton_up_clicked(self):
        """
        选中用例顺序往上移
        """
        selectedlist = []
        selectedItems =  self.tableWidget_caseList.selectedItems()
        if len(selectedItems) != 0:
            for item in selectedItems:
                if item.column() == 1:
                    casepath = unicode(item.text(),'gbk')
                    caseindex = self.caselist.index(casepath)
                    selectedlist.append(caseindex)
                    if caseindex == 0:
                        continue
                    self.caselist.pop(caseindex)
                    self.caselist.insert(caseindex - 1, casepath)

        self.tableWidget_caseList_update()
        #之前选中的仍然选中，但对选中多行的只能选中最后一行 待后续解决
        for row in selectedlist:
            if row == 0:
                selectrow = row
            else:
                selectrow = row - 1
            self.tableWidget_caseList.selectRow(selectrow)        

    @pyqtSignature("")
    def on_pushButton_down_clicked(self):
        """
        选中用例顺序往下移
        """
        selectedItems =  self.tableWidget_caseList.selectedItems()
        selectedlist = []
        if len(selectedItems) != 0:
            for item in selectedItems:
                if item.column() == 1:
                    casepath = unicode(item.text(),'gbk')
                    caseindex = self.caselist.index(casepath)
                    selectedlist.append(caseindex)
                    if caseindex == len(self.caselist) - 1 :
                        continue
                    self.caselist.pop(caseindex)
                    self.caselist.insert(caseindex + 1, casepath)
                    
        self.tableWidget_caseList_update()
        for row in selectedlist:
            if row == len(self.caselist) - 1:
                selectrow = row
            else:
                selectrow = row + 1
            self.tableWidget_caseList.selectRow(selectrow)
    
    @pyqtSignature("QModelIndex")
    def on_tableWidget_caseList_clicked(self, index):
        """
        将选择的用例地址显示到lineEdit_casePath
        """
        casePath = self.tableWidget_caseList.item(index.row(),1).text()
        self.lineEdit_casePath.setText(casePath)
        
    @pyqtSignature("QModelIndex")
    def on_tableWidget_caseList_doubleClicked(self, index):
        """
        双击后将文件打开至textBrowser_caseShow
        """
        self.textBrowser_caseShow.clear()
        casePath = self.tableWidget_caseList.item(index.row(),1).text()
        casePath = unicode(casePath,'gbk')
        caseData =  open(casePath,'r').read()
        try:
            caseData = caseData.decode('utf-8').encode('gbk')
        except:
            caseData =caseData
        self.textBrowser_caseShow.setText(caseData)
   
    def tableWidget_caseList_update(self):
        """
        更新选择CASE表格
        """        
        self.tableWidget_caseList.clearContents()
        self.tableWidget_caseList.setRowCount(0)
        if len(self.caselist) == 0:
            return
        for casepath in self.caselist:
            currentRow = self.tableWidget_caseList.rowCount()
            casename = os.path.basename(casepath)            
            self.tableWidget_caseList.insertRow(currentRow)
            self.tableWidget_caseList.setItem(currentRow  ,0, QTableWidgetItem(casename))
            self.tableWidget_caseList.setItem(currentRow  ,1, QTableWidgetItem(casepath))            
        
        

##################################
##        QtreeWidget操作       ##
##################################
    
    @pyqtSignature("")
    def on_pushButton_importDir_clicked(self):
        """
        获取case路径        
        """        
        caseDir = self.caseDir
        if caseDir.strip == '':
            lastDir = QString()
        else:
            lastDir = caseDir        
        caseDir = QFileDialog.getExistingDirectory(self,self.tr('GET CASE Dir'),lastDir)
        if caseDir == '':
            return False
        self.caseDir = unicode(caseDir,'gbk')
        self.updateTree(self.caseDir)    
        config.saveTemp('caseDir',self.caseDir)
            
    @pyqtSignature("")
    def on_pushButton_cellectCancel_clicked(self):
        """
        取消全选  
        """            
        self.dir_item.setCheckState(0,Qt.Unchecked)
        self.selectedCaseList = []

    @pyqtSignature("")
    def on_pushButton_selectAll_clicked(self):
        """
        全选    
        """            
        self.dir_item.setCheckState(0,Qt.Checked)   
        
    @pyqtSignature("")
    def on_pushButton_expandTree_clicked(self):
        """
        展开
        """
        self.treeWidget_caseTree.expandAll()
    
    @pyqtSignature("")
    def on_pushButton_retractTree_clicked(self):
        """
        收起
        """
        self.treeWidget_caseTree.collapseAll()

    @pyqtSignature("")
    def on_pushButton_removeDir_clicked(self):
        """刷新路径"""
        self.updateTree(self.caseDir)
    
    def updateTree(self,casepath):
        column = 0
        self.treeWidget_caseTree.clear()
        self.selectedCaseList = []
        self.dir_item = self.addTreeParent(self.treeWidget_caseTree.invisibleRootItem(), column, casepath, casepath)
        self.get_file_list_tree(self.dir_item,casepath,column)



    #获取文件路径下的所有文件，展现在treeWidget上
    def get_file_list_tree(self,item,path,column = 0):
        parentitem = item
        current_files = os.listdir(path)
        all_files = []
        for file_name in current_files:
            full_file_name = os.path.join(path, file_name)
            all_files.append(full_file_name)            
            if os.path.isdir(full_file_name):
                childitem = self.addTreeParent(parentitem,column,file_name,full_file_name)
                next_level_files = self.get_file_list_tree(childitem,full_file_name,column)
                all_files.extend(next_level_files)  
            else:
                '''
                此处还需增加对用例文件的限定判断
                '''   
                if file_name[-3:] == '.py' or file_name[-4:] =='.txt':
                    childitem = self.addTreeChild(parentitem,column,file_name,full_file_name)
        return all_files         
   
    
    def treehandleChanged(self,item,column = 0):
        if item.checkState(column) == Qt.Checked :
            count = item.childCount()
            if count > 0 :
                for i in xrange(0,count):
                    childItem = item.child(i)
                    childItem.setCheckState(0,Qt.Checked)
                self.treeWidget_caseTree.expandItem(item)

            else:
                casepath = unicode(item.text(1),'gbk')
                if casepath != '' :
                    self.selectedCaseList.append(casepath)
        if item.checkState(column) == Qt.Unchecked :
            count = item.childCount()
            if count > 0 :
                for i in xrange(count):
                    item.child(i).setCheckState(0,Qt.Unchecked)
                    casepath = unicode(item.child(i).text(1),'gbk')
                    if  casepath  in self.selectedCaseList:
                        self.selectedCaseList.remove(casepath)
            else:
                casepath = unicode(item.text(1),'gbk')
                if  casepath in self.selectedCaseList:
                    self.selectedCaseList.remove(casepath)

        
    def addTreeParent(self, parent, column, title, data):
        """
        添加父节点
        """        
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)        
        item.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
        item.setCheckState (column, Qt.Unchecked)
        icon = QIcon()
        icon.addPixmap(QPixmap("./ICO/fileclose.ico"), QIcon.Normal, QIcon.Off)
        icon.addPixmap(QPixmap("./ICO/fileopen.ico"), QIcon.Normal, QIcon.On)  
        item.setIcon(column,icon)
        item.setExpanded (True)
        return item

    def addTreeChild(self, parent, column, title, data = ''):
        """
        添加子节点
        """
        item = QTreeWidgetItem(parent, [title])
        item.setData(column, Qt.UserRole, data)
        item.setText(1,data)
        item.setCheckState (column, Qt.Unchecked)
        icon = QIcon()
        icon.addPixmap(QPixmap("./ICO/file.ico"), QIcon.Normal, QIcon.On) 
        item.setIcon(column,icon)
        
        return item      
    

if __name__ == '__main__':
    try:
        import sys
        app=QApplication(sys.argv) 
        testwin=TestCasePro()
        testwin.show()
        sys.exit(app.exec_())
        
    except Exception,e:
        
        print e    
    


    
   