# -*- coding: utf-8 -*-

"""
Module implementing TestCasePro.
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSignature,QDir,Qt,QTextCodec

from Ui_TestCase import Ui_TestCasePro
import os
from FUC import config

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
        self.treeWidget_caseTree.itemChanged.connect(self.treehandleChanged)
        #设置table的列宽
        self.tableWidget.setColumnWidth(0,40)
        self.tableWidget.setColumnWidth(1,180)
        self.tableWidget.setColumnWidth(2,70)
        self.tableWidget_caseList.setColumnWidth(0,150)        
    
    @pyqtSignature("")
    def on_pushButton_getConfig_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_saveConfig_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_getCase_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_pause_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_report_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_back_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_next_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_getconfig_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_saveconfig_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_close_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_Version_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_log_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_action_cleanlog_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
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
                print "add : " ,casepath
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
                    print "remove : ", casepath
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
            print 'utf8 to gbk'
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
        """移除路径"""
        self.treeWidget_caseTree.clear()
        self.selectedCaseList = []
    
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
                '''
                此处还需增加对用例文件的限定判断
                '''
                all_files.extend(next_level_files)  
            else:
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
    
    @pyqtSignature("int")
    def on_tabWidget_caseSelect_currentChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    

