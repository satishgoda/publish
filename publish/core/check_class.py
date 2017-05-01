# -*- coding:utf-8 -*-
#######################
# Author: wang bin
# Date:2017
########################


import sys
import time
sys.path.append("..")
from ui.head import *

def my_import(name):
    m = __import__(name)
    for n in name.split(".")[1:]:
        m = getattr(m, n)
    return m


class check_class(QWidget):

    def __init__(self, parent,module_step, tab_name, check_type, check_name, allow_skip):
        super(check_class, self).__init__(parent)
        # Include the module path so we can the check
        #sys.path.append(module_dir)

        # Reload the module every time to make the change work without reopenning Maya
        self.tab_name = tab_name
        self.module_type = check_type
        self.module_name = check_name
        self.module_step=module_step
        chk_module = my_import(module_step+'.'+check_type + '.' + check_name)
        reload(chk_module)
        self.check = chk_module.master_check()

        self.parent = parent
        self.check_name = self.check.get_check_name()
        self.description = self.check.get_description()
        self.allow_skip = {'true':True, 'false':False}[allow_skip]
        self.auto_fix = self.check.get_auto_fix()

        self.setupUi()

        self.setupConnections()

        return


    def setupUi(self ):
        self.mainHboxLayout = QHBoxLayout(self)
        self.check_QLabel=QLabel()
        self.chect_ok=QPixmap(r'D:\git_work\publish\publish\resources/check_ok.png')
        self.check_QLabel.setPixmap(self.chect_ok)
        self.skip_checkbox = QCheckBox()
        self.skip_checkbox.setCheckState(Qt.Checked)
        if not self.allow_skip:
            self.skip_checkbox.setEnabled(False)
        self.check_button = QPushButton()
        self.check_button.setText( self.check_name)

        self.fix_button = QPushButton()
        self.fix_button.setText(u"自动修复")
        self.fix_button.setEnabled(False)

        self.descript_button = QPushButton( self.parent)
        self.descript_button.setText("?")
        self.mainHboxLayout.addWidget(self.check_QLabel)
        self.mainHboxLayout.addWidget(self.skip_checkbox)
        self.mainHboxLayout.addWidget(self.check_button)
        self.mainHboxLayout.addWidget(self.descript_button)
        if self.auto_fix:
            print "hahaah"
            self.mainHboxLayout.addWidget(self.fix_button)



    def setupConnections(self):
        self.check_button.clicked.connect(self.run_check)
        if self.auto_fix:
            self.fix_button.clicked.connect(self.run_fix)
        self.descript_button.clicked.connect(self.show_description)


    def run_check(self):
        t = time.time()
        result = self.check.run_check()
        if result == '':
            self.valid = True
            self.check_button.setStyleSheet('QPushButton {color: rgb(160, 180, 255)}')
            self.check_button.repaint()
            self.dialog.print_log( self.module_name+ u' 检查通过\n')

        else:
            self.valid = False
            self.check_button.setStyleSheet('QPushButton {color: rgb(255, 140, 140)}')
            if isinstance(result, str):
                result = result.decode('utf-8')
            if self.auto_fix:
                #self.dialog.print_log( u"请先试用 自动修复 功能。\n", txt_color = QtGui.QColor(255, 160, 50))
                self.fix_button.setEnabled(True)

        return


    def run_fix(self):

        result = self.check.run_fix()
        if result == '':
            print "自动修复 完成"
        else:
            print "无法修复"

        self.fix_button.setEnabled(False)
        return


    def show_description(self):
        QMessageBox.about(self.parent, u"描述", self.module_type+ '.' + self.module_name + ":<br>"+self.description)
        return


    def clear_result(self):
        self.label.setText("")
        self.valid = False
        return


    def get_module_name(self):
        return self.module_name

    def get_valid(self):
        return self.valid


    def get_output(self):
        return self.check.get_output()


    def get_skip_chk(self):
        return self.skip_checkbox.checkState()


    def enable(self):

        if self.allow_skip:
            self.skip_checkbox.setEnabled(True)

        self.check_button.setEnabled(True)
        self.check_button.setStyleSheet('QPushButton {color: rgb(200, 200, 200)}')

        if self.auto_fix:
            self.fix_button.setEnabled(False)

        self.descript_button.setEnabled(True)
        return


    def disable(self):
        self.skip_checkbox.setEnabled(False)

        self.check_button.setEnabled(False)
        self.check_button.setStyleSheet('QPushButton {color: rgb(140, 140, 140)}')

        if self.auto_fix:
            self.fix_button.setEnabled(False)

        self.descript_button.setEnabled(False)


if __name__ == "__main__":
    import sys


    app = QApplication(sys.argv)
    parent=QWidget()
    tab_name="tab_name1"
    check_type="gen"
    check_name="version_name"
    allow_skip="true"
    module_step="publish_check"
    ui = check_class( parent,module_step, tab_name, check_type, check_name, allow_skip)
    parent.show()
    #ui.show()
    sys.exit(app.exec_())

