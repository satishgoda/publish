#!/usr/bin/python
#-*- coding=utf-8 -*-
#creat by wangbin
import sys
import re
#from Qt import 
from head import *


class ui_info(QWidget):#总框架的第一行widget(tile wideget)
    def __init__(self,parent=None):
        super(ui_info,self).__init__(parent)
        self.setupUI()
        #self.getElems()
        #self.setupConnections()
    def setupUI(self):
        self.info_Hboxlayout=QHBoxLayout(self)
        self.testbutton=QPushButton()
        self.testbutton2=QPushButton()
        self.info_Hboxlayout.addWidget(self.testbutton)
        self.info_Hboxlayout.addWidget(self.testbutton2)
    def getElems(self):
        self.ui_info=self.ui_info
    def setupConnections(self):
        pass
    def dropEvent(self, event):
        pass
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ui_info()
    ui.show()
    sys.exit(app.exec_())