import configWindowUI
from tubeqt import MainCode
from PyQt5 import QtWidgets


class ConfigCode(configWindowUI.Ui_Configuration):
    def setupUi(self, configWin):
        super().setupUi(configWin)
        self.comboDefaultPreset.addItems(MainCode.comboItems)
        MainCode.config_ini.read(MainCode.config_dir + '/config.ini')
        self.lineDownloadDir.setText(MainCode.config_ini.get('setup', 'download_dir'))
        self.lineCustomPreset.setText(MainCode.config_ini.get('setup', 'custom'))
        self.comboDefaultPreset.setCurrentIndex(MainCode.config_ini.getint('setup', 'default_preset'))
        self.buttonDownloadDir.clicked.connect(self.f_buttonDownloadDir)
        self.buttonOkCancel.accepted.connect(self.f_OK)

    def f_buttonDownloadDir(self):
        self.lineDownloadDir.setText(str(QtWidgets.QFileDialog.getExistingDirectory(None, "Select directory")))

    def f_OK(self):
        confirmbox = QtWidgets.QMessageBox()
        confirmbox.setText('Really Save?')
        confirmbox.setIcon(QtWidgets.QMessageBox.Warning)
        confirmbox.setWindowTitle("Confirm")
        confirmbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = confirmbox.exec_()
        if ret == QtWidgets.QMessageBox.Ok:
            MainCode.config_ini.set('setup', 'download_dir', self.lineDownloadDir.text())
            MainCode.config_ini.set('setup', 'custom', self.lineCustomPreset.text())
            MainCode.config_ini.set('setup', 'default_preset', str(self.comboDefaultPreset.currentIndex()))
            with open(MainCode.home_dir + "/.config/tubeqt/config.ini", 'w') as configfile:
                MainCode.config_ini.write(configfile)


def configMain():
    configWin = QtWidgets.QDialog()
    ui = ConfigCode()
    ui.setupUi(configWin)
    configWin.exec_()
