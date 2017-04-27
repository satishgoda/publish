#!/usr/bin/python
#-*- coding=utf-8 -*-
import os
import sys
sys.path.append("..")
from ui.head import *
from ui.ui_main_window import ui_main_window
class Response(QMainWindow):
    def __init__(self, parent = None):
        super(Response,self).__init__(parent)
        #self.setWindowTitle(_fromUtf8("发布工具"))
        self.setupUi()
        self.getElems()
        self.setDefault()
        self.setupConnections()
        #self.setDefault()
    def setupUi(self):
        self.ui_main_window=ui_main_window()
        self.setCentralWidget(self.ui_main_window)
    def getElems(self):
        pass
    def setDefault(self):
        pass
    def setupConnections(self):
        pass
    def on_Treewidgetbel_drop(self,*args):
        pass
if __name__ == "__main__":
    import sys
    
    app = QApplication(sys.argv)
    #app.setStyle('windows')
    app.setStyleSheet('QMainWindow{border:1px solid rgb(45,45,45); background:rgb(45,45,45);}\
                    QMessageBox{background:rgb(45,45,45);}\
                    QLabel{color:rgb(200, 200, 200)}    \
                    QPushButton{background:rgb(90, 0, 0);color:rgb(100, 100, 100); width:49px; height:30px} \
                    QComboBox{border:3px solid rgb(45, 45, 45);background:rgb(50, 50, 50); color:rgb(180,180,180)}\
                    QListWidget{border:1px solid rgb(45,45,45); background:transparent}\
                    #QTreeWidget{border:1px solid rgb(30,30,30); background:transparent}\
                    QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
                    #QTreeWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(0,0,0); padding:15px} \
                    QListWidget::item{border:3px solid rgb(45, 45, 45); background:rgb(50, 50, 50); color:rgb(180,180,180); padding:15px}  \
                    QListWidget::item:hover{border:3px solid rgb(80, 80, 80); background:rgb(120, 120, 120); color:rgb(45,45,45); padding:15px} \
                    QListWidget::item:selected{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:15px}\
                    QListView::item:selected:active{border:3px solid rgb(106, 93, 111); background:rgb(68, 56, 66); color:rgb(220,220,220); padding:12px} \
                    QScrollBar:vertical {border: 2px solid rgb(80, 80, 80);background:rgb(50, 50, 50); width:20px; margin: 22px 0 22px 0;} \
                    QScrollBar::handle:vertical {background:rgb(95, 95, 95); min-height: 20px;}\
                    QScrollBar::add-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
                                                    subcontrol-position: bottom;subcontrol-origin: margin;}\
                    QScrollBar::sub-line:vertical {border: 2px solid rgb(80, 80, 80); background:rgb(95, 95, 95) ;height:20px; \
                                                    subcontrol-position: top;subcontrol-origin: margin;}\
                    QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {border: 1px solid rgb(80, 80, 80); \
                                                    width:4px; height:4px; background:rgb(50, 50, 50);}\
                    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}\
                    ')
    ui = Response()
    ui.show()
    sys.exit(app.exec_())