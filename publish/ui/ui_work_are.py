#!/usr/bin/python
#-*- coding=utf-8 -*-
#creat by wangbin
import sys
sys.path.append("D:\work\Qt")
import Qt
import re
#from Qt import 
from Qt.QtWidgets import *
from Qt.QtGui import *

class ui_work_are(QWidget):#总框架的第一行widget(tile wideget)
    def __init__(self,parent=None):
        super(ui_work_are,self).__init__(parent)
        self.setupUI()
        #self.getElems()
        #self.setupConnections()
    def setupUI(self):
        self.info_Vboxlayout=QVBoxLayout(self)

    def getElems(self):
        pass
    def setupConnections(self):
        pass
    def dropEvent(self, event):
        pass
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ui_work_are()
    ui.show()
    sys.exit(app.exec_())