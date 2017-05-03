#!/usr/bin/python
#-*- coding=utf-8 -*-
import os
import sys
#r"D:\work\ple" in sys.path or sys.path.append(r"D:\work\ple")
from turn_table_tooll.ui.head import *
from turn_table_tooll.ui.ui_main_window import ui_main_window
import work_response as wr
reload(wr)
class Response(QMainWindow):
    def __init__(self, parent = None):
        super(Response,self).__init__(parent)
        #self.setWindowTitle(_fromUtf8("发布工具"))
        self.setWindowTitle("turn_table_tool")
        self.setupUi()
        self.getElems()
        self.setDefault()
        self.setupConnections()
        #self.setDefault()
    def setupUi(self):
        self.ui_main_window=ui_main_window()
        self.setCentralWidget(self.ui_main_window)
    def getElems(self):
        self.moring_toolButton_bel=self.ui_main_window.ui_turn_table_widget.main_Widget.moring_toolButton
        self.noon_toolButton_bel = self.ui_main_window.ui_turn_table_widget.main_Widget.noon_toolButton
        self.nightfall_toolButton_bel = self.ui_main_window.ui_turn_table_widget.main_Widget.nightfall_toolButton
        self.night_toolButton_bel = self.ui_main_window.ui_turn_table_widget.main_Widget.night_toolButton
        pass
    def setDefault(self):
        pass
    def setupConnections(self):
        self.moring_toolButton_bel.clicked.connect(self.on_moring_toolButton_clicked)
        self.noon_toolButton_bel.clicked.connect(self.on_noon_toolButton_clicked)
        self.nightfall_toolButton_bel.clicked.connect(self.nightfall_toolButton_clicked)
        self.night_toolButton_bel.clicked.connect(self.night_toolButton_clicked)
    def on_moring_toolButton_clicked(self):
        wr.import_turntable_template("morning")
        print "on_moring_toolButton_clicked"
    def on_noon_toolButton_clicked(self):
        wr.import_turntable_template("noon")
        print "on_noon_toolButton_clicked"
    def nightfall_toolButton_clicked(self):
        print "start "
        wr.import_turntable_template("nightfall")
        print "nightfall_toolButton_clicked"
    def night_toolButton_clicked(self):
        wr.import_turntable_template("night")
        print "night_toolButton_clicked"
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