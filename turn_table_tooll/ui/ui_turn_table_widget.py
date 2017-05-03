# -*- coding: utf-8 -*-
#by wangbin 852854910
import sys
import os
import inspect 
from turn_table_tooll.ui.head import *
#sys.path.append("..")
#sys.path.append(r"D:\work\ple")
import turn_table_tooll.resources.turn_table_tooll_qrc
class ui_turn_table_widget(QWidget):
    def __init__(self, parent = None):
        super(ui_turn_table_widget,self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.mainVboxLayout=QVBoxLayout(self)
        path=self.current_path()
        self.main_Widget = self.loadUiWidget(os.path.join(path,"ui_turn_table_widget.ui"))
        self.mainVboxLayout.addWidget(self.main_Widget)
        #print dir(self.main_Widget)
        return self.main_Widget
    def current_path(self):
        path=os.path.realpath(sys.path[0])  
        if os.path.isfile(path):  
            path=os.path.dirname(path)  
            return os.path.abspath(path)  
        else:  
            caller_file=inspect.stack()[1][1]  
            return os.path.abspath(os.path.dirname(caller_file))  
    def loadUiWidget(self,uifilename, parent=None):
        ui = QtCompat.load_ui(uifilename)
        return ui
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = ui_turn_table_widget()
    MainWindow.show()
    sys.exit(app.exec_())
