import sys
import PyQt5.QtWidgets as QW
from widget_tree import WidgetTree
from widget_plot import WidgetPlot
from widget_music_player import WidgetMusicPlayer


class WidgetMain(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = QW.QWidget()
        self.w_tree = WidgetTree()
        self.w_plot = WidgetPlot()
        self.w_mp = WidgetMusicPlayer()
        self.splitter = QW.QSplitter()

        self.init_ui()
        self.init_event()
        self.init_method()

    def init_ui(self):
        # self.setCentralWidget(self.w)

        # layout
        hbox0 = QW.QVBoxLayout()
        hbox0.addWidget(self.w_plot)
        hbox0.addWidget(self.w_mp)
        self.w.setLayout(hbox0)
        self.splitter.addWidget(self.w_tree)
        self.splitter.addWidget(self.w)

        self.setCentralWidget(self.splitter)

    def init_event(self):
        pass

    def init_method(self):
        pass


def main():
    app = QW.QApplication(sys.argv)

    # sr, data = wavfile.read(path)

    w = WidgetMain()
    w.w_tree.tree.setRootIndex(w.w_tree.model.index('../data/'))
    # w.w_plot.set_signal(signal, sr)

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
