import sys
import librosa
import PyQt5.QtWidgets as QW
import PyQt5.QtMultimedia as QM
import pyqtgraph as pg
from widget_main import WidgetMain


class SpectrogramTree(WidgetMain):
    def __init__(self):
        super().__init__()

        # bar
        self.bar_0 = pg.InfiniteLine(
                        pen='#FAF032AA', hoverPen='#FAF032FF', movable=True)
        self.bar_1 = pg.InfiniteLine(
                        pen='#FAF032AA', hoverPen='#FAF032FF', movable=True)

        # init method
        self.init_method_()
        self.init_event_()

    def init_method_(self):
        self.w_mp.player.positionChanged.connect(self.player_position_changed)
        self.bar_0.setZValue(20)
        self.bar_1.setZValue(20)
        self.bar_0.addMarker('v', position=1, size=10)
        self.bar_0.addMarker('^', position=0, size=10)
        self.bar_1.addMarker('v', position=1, size=10)
        self.bar_1.addMarker('^', position=0, size=10)
        self.w_plot.p_signal.addItem(self.bar_0)
        self.w_plot.p_spec.addItem(self.bar_1)

    def init_event_(self):
        self.w_mp.player.positionChanged.connect(self.player_position_changed)
        self.bar_0.sigPositionChanged.connect(self.update_bar_pos)
        self.bar_1.sigPositionChanged.connect(self.update_bar_pos)

    def player_position_changed(self, pos, senderType=False):
        '''
        music player の時間に変更があったら動く関数
        '''
        pos_sec = pos/1000
        self.bar_0.setPos(pos_sec)
        self.bar_1.setPos(pos_sec)

    def update_bar_pos(self):
        sender = self.sender()
        pos = sender.getPos()[0]
        # bar を連動させる
        if sender == self.bar_0:
            self.bar_1.setPos(pos)
        elif sender == self.bar_1:
            self.bar_0.setPos(pos)

        if self.w_mp.player.state() != QM.QMediaPlayer.PlayingState:
            # musicplayerの再生位置の調整
            self.w_mp.player.setPosition(pos*1000)  # ms 単位で渡す


def main():
    app = QW.QApplication(sys.argv)

    w = SpectrogramTree()

    filename = librosa.util.example_audio_file()
    data, sr = librosa.load(filename, sr=None)
    w.w_plot.set_signal(data, sr)
    w.w_mp.set_contents(filename)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
