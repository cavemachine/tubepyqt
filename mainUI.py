# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainUI(object):
    def setupUi(self, mainUI):
        mainUI.setObjectName("mainUI")
        mainUI.resize(522, 456)
        self.widgetCentral = QtWidgets.QWidget(mainUI)
        self.widgetCentral.setAutoFillBackground(True)
        self.widgetCentral.setObjectName("widgetCentral")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widgetCentral)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 521, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layoutMain = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layoutMain.setContentsMargins(0, 0, 0, 0)
        self.layoutMain.setObjectName("layoutMain")
        self.widgetTab = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.widgetTab.setTabPosition(QtWidgets.QTabWidget.South)
        self.widgetTab.setDocumentMode(True)
        self.widgetTab.setObjectName("widgetTab")
        self.tubeTab = QtWidgets.QWidget()
        self.tubeTab.setAutoFillBackground(True)
        self.tubeTab.setObjectName("tubeTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tubeTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 521, 301))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.tubeLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.tubeLayout.setContentsMargins(2, 2, 2, 2)
        self.tubeLayout.setObjectName("tubeLayout")
        self.buttonSaveList = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.buttonSaveList.setObjectName("buttonSaveList")
        self.tubeLayout.addWidget(self.buttonSaveList, 2, 2, 1, 1)
        self.buttonAdd = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.buttonAdd.setObjectName("buttonAdd")
        self.tubeLayout.addWidget(self.buttonAdd, 0, 3, 1, 1)
        self.buttonDeleteAll = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.buttonDeleteAll.setObjectName("buttonDeleteAll")
        self.tubeLayout.addWidget(self.buttonDeleteAll, 2, 1, 1, 1)
        self.buttonDelete = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.buttonDelete.setObjectName("buttonDelete")
        self.tubeLayout.addWidget(self.buttonDelete, 2, 0, 1, 1)
        self.buttonLoadList = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.buttonLoadList.setObjectName("buttonLoadList")
        self.tubeLayout.addWidget(self.buttonLoadList, 2, 3, 1, 1)
        self.listURL = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listURL.setObjectName("listURL")
        self.tubeLayout.addWidget(self.listURL, 1, 0, 1, 4)
        self.linePreset = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.linePreset.setObjectName("linePreset")
        self.tubeLayout.addWidget(self.linePreset, 4, 0, 1, 4)
        self.lineURL = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineURL.setObjectName("lineURL")
        self.tubeLayout.addWidget(self.lineURL, 0, 0, 1, 3)
        self.comboPreset = QtWidgets.QComboBox(self.tubeTab)
        self.comboPreset.setGeometry(QtCore.QRect(0, 300, 191, 25))
        self.comboPreset.setObjectName("comboPreset")
        self.buttonDownload = QtWidgets.QPushButton(self.tubeTab)
        self.buttonDownload.setGeometry(QtCore.QRect(380, 300, 140, 51))
        self.buttonDownload.setObjectName("buttonDownload")
        self.buttonStop = QtWidgets.QPushButton(self.tubeTab)
        self.buttonStop.setGeometry(QtCore.QRect(380, 350, 140, 27))
        self.buttonStop.setObjectName("buttonStop")
        self.widgetTab.addTab(self.tubeTab, "")
        self.ffmpegTab = QtWidgets.QWidget()
        self.ffmpegTab.setAutoFillBackground(True)
        self.ffmpegTab.setObjectName("ffmpegTab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.ffmpegTab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(90, 30, 401, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.ffmpegLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.ffmpegLayout.setContentsMargins(0, 0, 0, 0)
        self.ffmpegLayout.setObjectName("ffmpegLayout")
        self.ffmpegLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.ffmpegLabel.setObjectName("ffmpegLabel")
        self.ffmpegLayout.addWidget(self.ffmpegLabel, 0, 0, 1, 1)
        self.widgetTab.addTab(self.ffmpegTab, "")
        self.layoutMain.addWidget(self.widgetTab, 2, 0, 1, 1)
        mainUI.setCentralWidget(self.widgetCentral)
        self.menubar = QtWidgets.QMenuBar(mainUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 23))
        self.menubar.setObjectName("menubar")
        mainUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainUI)
        self.statusbar.setObjectName("statusbar")
        mainUI.setStatusBar(self.statusbar)

        self.retranslateUi(mainUI)
        self.widgetTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainUI)

    def retranslateUi(self, mainUI):
        _translate = QtCore.QCoreApplication.translate
        mainUI.setWindowTitle(_translate("mainUI", "tubeqt"))
        self.buttonSaveList.setText(_translate("mainUI", "Save list"))
        self.buttonAdd.setText(_translate("mainUI", "Add"))
        self.buttonDeleteAll.setText(_translate("mainUI", "Delete All"))
        self.buttonDelete.setText(_translate("mainUI", "Delete"))
        self.buttonLoadList.setText(_translate("mainUI", "Load list"))
        self.buttonDownload.setText(_translate("mainUI", "Download"))
        self.buttonStop.setText(_translate("mainUI", "Stop"))
        self.widgetTab.setTabText(self.widgetTab.indexOf(self.tubeTab), _translate("mainUI", "youtube-dl"))
        self.ffmpegLabel.setText(_translate("mainUI", "TextLabel"))
        self.widgetTab.setTabText(self.widgetTab.indexOf(self.ffmpegTab), _translate("mainUI", "ffmpeg"))

