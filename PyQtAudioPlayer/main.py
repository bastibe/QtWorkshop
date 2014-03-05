import sys
from PyQt5 import QtGui, QtQml, QtQuick, QtCore
from PyQt5.QtCore import pyqtProperty
from autoProperty import autoProperty
from pysoundfile import SoundFile
from pysoundcard import Stream, default_output_device
import re

class AudioThread(QtCore.QThread):

    frameChanged = QtCore.pyqtSignal(float)

    def __init__(self, soundFile, parent=None):
        super(self.__class__, self).__init__(parent)
        self.soundFile = soundFile

    def run(self):
        with Stream() as s:
            while self.soundFile.seek(0) < len(self.soundFile):
                s.write(self.soundFile.read(1024))
                self.frameChanged.emit(self.soundFile.seek(0))
            self.frameChanged.emit(0)

class Player(QtCore.QObject):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self._filename = ""
        self._isPlaying = False
        self._progress = 0
        self._waveform = []
        self._length = 0
        self.filename_changed.connect(self.open_file)
        self.soundFile = None
        self.isPlaying_changed.connect(self.play_pause)
        self.player = False

    def open_file(self, file_url):
        # convert file:///Z:/some/path to Z:/some/path and
        #         file:///some/path to /some/path
        path = re.sub(r'file://(/(?=[A-Z]:))', '', file_url)
        self.soundFile = SoundFile(path)
        self._waveform = []
        frames = len(self.soundFile)
        block_len = int(frames/1000)
        while self.soundFile.seek(0) < frames:
            block = self.soundFile.read(block_len)
            self._waveform.append(QtGui.QVector2D(block.min(), block.max()))
        self.waveform_changed.emit(self._waveform)
        self._length = len(self.soundFile)/self.soundFile.sample_rate
        self.length_changed.emit(self._length)

    def play_pause(self, play):
        if play:
            self.soundFile.seek_absolute(int(self.progress*self.soundFile.sample_rate))
            self.player = AudioThread(self.soundFile)
            def setProgress(frame):
                self.progress = frame/self.soundFile.sample_rate
            self.player.frameChanged.connect(setProgress)
            def finishedPlaying():
                self.isPlaying = False
            self.player.finished.connect(finishedPlaying)
            self.player.start()
        else:
            if self.player.isRunning():
                self.player.terminate()

    @QtCore.pyqtSlot(float)
    def scrub(self, where):
        if self.isPlaying:
            self.isPlaying = False
            self.progress = where
            self.isPlaying = True
        else:
            self.progress = where

    filename_changed, filename = autoProperty(str, 'filename')
    isPlaying_changed, isPlaying = autoProperty(bool, 'isPlaying')
    progress_changed, progress = autoProperty(float, 'progress')
    waveform_changed, waveform = autoProperty(QtCore.QVariant, 'waveform', readonly=True)
    length_changed, length = autoProperty(float, 'length', readonly=True)


if __name__ == "__main__":
    if not QtGui.QGuiApplication.instance():
        app = QtGui.QGuiApplication(sys.argv)
    QtQml.qmlRegisterType(Player, 'Player', 1, 0, 'Player')
    engine = QtQml.QQmlApplicationEngine('main.qml')
    if len(engine.rootObjects()) > 0:
        mainWindow = engine.rootObjects()[0]
        mainWindow.setVisible(True)
    app.exec()
