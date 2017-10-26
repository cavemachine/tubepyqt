# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(567, 160)
        self.buttonOkCancel = QtWidgets.QDialogButtonBox(Configuration)
        self.buttonOkCancel.setGeometry(QtCore.QRect(220, 120, 341, 32))
        self.buttonOkCancel.setOrientation(QtCore.Qt.Horizontal)
        self.buttonOkCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonOkCancel.setObjectName("buttonOkCancel")
        self.gridLayoutWidget = QtWidgets.QWidget(Configuration)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelCustomPreset = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelCustomPreset.setObjectName("labelCustomPreset")
        self.gridLayout.addWidget(self.labelCustomPreset, 1, 0, 1, 1)
        self.lineDownloadDir = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineDownloadDir.setObjectName("lineDownloadDir")
        self.gridLayout.addWidget(self.lineDownloadDir, 0, 1, 1, 1)
        self.labelDownloadDir = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDownloadDir.setObjectName("labelDownloadDir")
        self.gridLayout.addWidget(self.labelDownloadDir, 0, 0, 1, 1)
        self.labelDefaultPreset = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelDefaultPreset.setObjectName("labelDefaultPreset")
        self.gridLayout.addWidget(self.labelDefaultPreset, 2, 0, 1, 1)
        self.buttonDownloadDir = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.buttonDownloadDir.setObjectName("buttonDownloadDir")
        self.gridLayout.addWidget(self.buttonDownloadDir, 0, 2, 1, 1)
        self.lineCustomPreset = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineCustomPreset.setObjectName("lineCustomPreset")
        self.gridLayout.addWidget(self.lineCustomPreset, 1, 1, 1, 2)
        self.comboDefaultPreset = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboDefaultPreset.sizePolicy().hasHeightForWidth())
        self.comboDefaultPreset.setSizePolicy(sizePolicy)
        self.comboDefaultPreset.setObjectName("comboDefaultPreset")
        self.gridLayout.addWidget(self.comboDefaultPreset, 2, 1, 1, 2)

        self.retranslateUi(Configuration)
        self.buttonOkCancel.accepted.connect(Configuration.accept)
        self.buttonOkCancel.rejected.connect(Configuration.reject)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Configuration"))
        self.labelCustomPreset.setText(_translate("Configuration", "Custom preset:"))
        self.labelDownloadDir.setText(_translate("Configuration", "Download/conversion dir:"))
        self.labelDefaultPreset.setText(_translate("Configuration", "Default Preset:"))
        self.buttonDownloadDir.setText(_translate("Configuration", "..."))

