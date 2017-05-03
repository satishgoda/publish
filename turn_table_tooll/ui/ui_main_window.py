#!/usr/bin/python
#-*- coding=utf-8 -*-
# Author: wangbin
#from head import *
from turn_table_tooll.ui.head import *
import ui_turn_table_widget
reload(ui_turn_table_widget)
from ui_turn_table_widget import ui_turn_table_widget
class ui_main_window(QWidget):
    def __init__(self,parent=None):
        super(ui_main_window,self).__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.ui_turn_table_widget=ui_turn_table_widget()
        QWidgetvboxLayout = QVBoxLayout(self)#建立竖向的layout
        QWidgetvboxLayout.addWidget(self.ui_turn_table_widget)
        QWidgetvboxLayout.setContentsMargins(0, 0, 0, 0)#mainVboxLayout
        
        #mainWindow.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ui_main_window()
    ui.show()
    sys.exit(app.exec_())