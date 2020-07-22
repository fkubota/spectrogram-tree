import sys
import librosa
import PyQt5.QtWidgets as QW
import PyQt5.QtMultimedia as QM
import PyQt5.QtCore as QC


class WidgetMusicPlayer(QW.QWidget):
    def __init__(self):
        super().__init__()

        self.player = QM.QMediaPlayer()
        self.btn_play = QW.QPushButton('Play')
        self.btn_pause = QW.QPushButton('Pause')

        # init method
        self.init_ui()
        self.init_event()

    def init_ui(self):
        self.btn_play.setFixedWidth(100)
        self.btn_pause.setFixedWidth(100)

        # layout
        hbox0 = QW.QHBoxLayout()
        hbox0.addWidget(self.btn_play)
        hbox0.addWidget(self.btn_pause)
        hbox0.addStretch()
        self.setLayout(hbox0)

    def init_event(self):
        self.btn_play.clicked.connect(self.play_handler)
        self.btn_pause.clicked.connect(self.pause_handler)

    def play_handler(self):
        self.player.play()

    def pause_handler(self):
        self.player.pause()

    def set_contents(self, file_path):
        self.player.setMedia(
            QM.QMediaContent(QC.QUrl.fromLocalFile(file_path))
            )


def main():
    app = QW.QApplication(sys.argv)

    file_path = librosa.util.example_audio_file()

    w = WidgetMusicPlayer()
    w.move(600, 500)
    w.set_contents(file_path)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
