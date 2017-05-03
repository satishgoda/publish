# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_turn_table_widget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_turm_table_tool_qwidget(object):
    def setupUi(self, turm_table_tool_qwidget):
        turm_table_tool_qwidget.setObjectName("turm_table_tool_qwidget")
        turm_table_tool_qwidget.resize(175, 444)
        self.verticalLayout = QtWidgets.QVBoxLayout(turm_table_tool_qwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.moring_toolButton = QtWidgets.QToolButton(turm_table_tool_qwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/morning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.moring_toolButton.setIcon(icon)
        self.moring_toolButton.setIconSize(QtCore.QSize(150, 80))
        self.moring_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.moring_toolButton.setObjectName("moring_toolButton")
        self.verticalLayout.addWidget(self.moring_toolButton)
        self.noon_toolButton = QtWidgets.QToolButton(turm_table_tool_qwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/resources/noon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.noon_toolButton.setIcon(icon1)
        self.noon_toolButton.setIconSize(QtCore.QSize(150, 80))
        self.noon_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.noon_toolButton.setObjectName("noon_toolButton")
        self.verticalLayout.addWidget(self.noon_toolButton)
        self.nightfall_toolButton = QtWidgets.QToolButton(turm_table_tool_qwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/resources/nightfall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nightfall_toolButton.setIcon(icon2)
        self.nightfall_toolButton.setIconSize(QtCore.QSize(150, 80))
        self.nightfall_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.nightfall_toolButton.setObjectName("nightfall_toolButton")
        self.verticalLayout.addWidget(self.nightfall_toolButton)
        self.night_toolButton = QtWidgets.QToolButton(turm_table_tool_qwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/resources/night.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.night_toolButton.setIcon(icon3)
        self.night_toolButton.setIconSize(QtCore.QSize(150, 80))
        self.night_toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.night_toolButton.setObjectName("night_toolButton")
        self.verticalLayout.addWidget(self.night_toolButton)

        self.retranslateUi(turm_table_tool_qwidget)
        QtCore.QMetaObject.connectSlotsByName(turm_table_tool_qwidget)

    def retranslateUi(self, turm_table_tool_qwidget):
        _translate = QtCore.QCoreApplication.translate
        turm_table_tool_qwidget.setWindowTitle(_translate("turm_table_tool_qwidget", "Form"))
        self.moring_toolButton.setText(_translate("turm_table_tool_qwidget", "morning 早上"))
        self.noon_toolButton.setText(_translate("turm_table_tool_qwidget", "noon 下午"))
        self.nightfall_toolButton.setText(_translate("turm_table_tool_qwidget", "nightfall 傍晚"))
        self.night_toolButton.setText(_translate("turm_table_tool_qwidget", "night 晚上"))

import turn_table_tooll_qrc_rc
