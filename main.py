from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

from pytube import YouTube

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("MainUI.ui", self)

        self.pushButton.clicked.connect(self.DownloadVideo)

    def DownloadVideo(self):
        if self.radioButton.isChecked() == True:
            url = self.lineEdit.text()
            exit_path = self.lineEdit_2.text()
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            stream.download(output_path = exit_path)
        if self.radioButton_2.isChecked() == True:
            url = self.lineEdit.text()
            exit_path = self.lineEdit_2.text()
            video = YouTube(url)
            stream = video.streams.get_audio_only()
            stream.download(output_path = exit_path)
        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()