import sys
import os
import getpass
from mainUI import Ui_mainUI
import configWindow
from urllib.request import urlopen
from html.parser import HTMLParser
from configparser import ConfigParser
from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess


class MainCode(Ui_mainUI):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.configCheck()
        self.menuCreate()
        self.buttonAdd.clicked.connect(self.f_buttonAdd)
        self.buttonDelete.clicked.connect(self.f_buttonDelete)
        self.buttonDeleteAll.clicked.connect(self.f_buttonDeleteAll)
        self.buttonSaveList.clicked.connect(self.f_buttonSaveList)
        self.buttonLoadList.clicked.connect(self.f_buttonLoadList)
        self.buttonDownload.clicked.connect(self.f_buttonDownload)
        self.buttonStop.clicked.connect(self.f_buttonStop)
        self.comboPreset.addItems(self.comboItems)
        self.comboPreset.currentIndexChanged.connect(self.f_comboChanged)
        self.comboPreset.setCurrentIndex(self.config_ini.getint('setup', 'default_preset'))
        self.f_comboChanged()

    def configCheck(self):
        if not os.path.exists(self.home_dir + "/.config/tubeqt/config.ini"):
            if not os.path.exists(self.home_dir + "/.config/tubeqt"):
                os.makedirs(self.config_dir)
            self.config_ini = ConfigParser()
            self.config_ini.add_section('setup')
            self.config_ini.set('setup', 'download_dir', self.home_dir + "/Music")
            self.config_ini.set('setup', 'default_preset', '1')
            self.config_ini.set('setup', 'custom', "-f bestvideo" )
            with open(self.home_dir + "/.config/tubeqt/config.ini", 'w+') as configfile:
                self.config_ini.write(configfile)
        else:
            self.config_ini.read(self.config_dir + '/config.ini')

    def menuCreate(self):
        self.menuFileExit = QtWidgets.QAction("&Exit")
        self.menuFileExit.triggered.connect(sys.exit)
        self.menuFileConfig = QtWidgets.QAction("&Config")
        self.menuFileConfig.triggered.connect(configWindow.configMain)
        self.menuFile = self.menubar.addMenu('&File')
        self.menuFile.addAction(self.menuFileConfig)
        self.menubar.addSeparator()
        self.menuFile.addAction(self.menuFileExit)

    def f_buttonAdd(self):
        if self.lineURL.text() != "": 
            url = self.lineURL.text().lstrip()
        if 'http://' not in url and 'https://' not in url:
            url = 'http://' + url
        try:
            html_string = urlopen(url).read().decode('utf_8')
        except:
            self.statusbar.showMessage('[ERROR] URL invalid or not found: \"' + url + '\"' ,4000)
        else:
            parser = self.HtmlTitle()
            parser.feed(html_string)
            itemText = url + "  (" + parser.title.rstrip('- YouTube') + ")"
            self.listURL.addItem(itemText)
            self.lineURL.setFocus()
            self.lineURL.clear()
            print(itemText.split('  ', 1)[0])

    def f_buttonDelete(self):
        self.listURL.takeItem(self.listURL.currentRow())

    def f_buttonDeleteAll(self):
        confirmbox = QtWidgets.QMessageBox()
        confirmbox.setText('Really clear list?')
        confirmbox.setIcon(QtWidgets.QMessageBox.Warning)
        confirmbox.setWindowTitle("Confirm")
        confirmbox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        ret = confirmbox.exec_()
        if ret == QtWidgets.QMessageBox.Ok:
            self.listURL.clear()

    def f_buttonSaveList(self):
        list_save_name = QtWidgets.QFileDialog.getSaveFileName(
                            None, 'Save video list', self.home_dir,
                            "tubeqt video list files (*.tqt)")
        if '.tqt' in list_save_name[0]:
            save_dialog = open(list_save_name[0], 'w')
        else:
            save_dialog = open(list_save_name[0] + '.tqt', 'w')

        for i in range(0, self.listURL.count()):
            save_dialog.write(self.listURL.item(i).text() + "\n")
        save_dialog.close()

    def f_buttonLoadList(self):
        list_load_name = QtWidgets.QFileDialog.getOpenFileName(
                            None, 'Load video list', self.home_dir, 
                            "tubeqt video list files (*.tqt)") 
        if list_load_name[0]:
            load_dialog = open(list_load_name[0], 'r').read().splitlines()
            self.listURL.clear()
            self.listURL.addItems(load_dialog)

    def f_buttonDownload(self):
        os.system("killall youtube-dl")
        video_list = self.config_dir + "/videos.tqt"
        txt = open(video_list, "w")
        for i in range(0, self.listURL.count()):
            txt.write(self.listURL.item(i).text().split('  ', 1)[0] + "\n")
        txt.close()
        comm = ("xterm -e bash -c \"youtube-dl -a " + video_list + " " 
                + self.linePreset.text() + " -o \'" 
                + self.config_ini.get('setup', 'download_dir') 
                + "/%(title)s.%(ext)s\' ;read -p [Press_ENTER]\"")
        process = QProcess()
        process.startDetached(comm)
        

    def f_buttonStop(self):
        os.system("killall youtube-dl")

    def f_comboChanged(self):
        if self.comboPreset.currentText() == "mp3 128k":
            self.linePreset.setText("-ciwx --audio-format mp3 --audio-quality 128k")
        if self.comboPreset.currentText() == "mp3 64k":
            self.linePreset.setText("-ciwx --audio-format mp3 --audio-quality 64k")
        if self.comboPreset.currentText() == "mp3 32k":
            self.linePreset.setText("-ciwx --audio-format mp3 --audio-quality 32k")
        if self.comboPreset.currentText() == "Custom":
            self.linePreset.setText(self.config_ini.get('setup', 'custom'))

    class HtmlTitle(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.match = False
            self.title = ''

        def handle_starttag(self, tag, attributes):
            self.match = True if tag == 'title' else False

        def handle_data(self, data):
            if self.match:
                self.title = data
                self.match = False

    comboItems = ["mp3 128k", "mp3 64k", 
                  "mp3 32k", "mp3 32k(mono)", 
                  "Download video(best)", "Download video(medium)",
                  "Download video(low)", "Custom"]
    user_name = getpass.getuser()
    config_dir = "/home/" + user_name + "/.config/tubeqt"
    home_dir = "/home/" + user_name
    config_ini = ConfigParser()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = MainCode()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
