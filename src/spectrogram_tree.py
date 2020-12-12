import sys
import pydub
import numpy as np
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
        self.w_tree.tree.doubleClicked.connect(self.item_double_cliced)
        self.w_plot.p_signal.scene().sigMouseClicked.connect(
                                        self.clicked_window)
        self.w_plot.p_spec.scene().sigMouseClicked.connect(
                                        self.clicked_window)

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

    def item_double_cliced(self, index):
        '''
        music player に音声データをセット。
        グラフを更新。
        '''
        path = index.model().filePath(index)

        # import librosa
        # data, sr = librosa.load(path, sr=None)

        # if '.wav' in path:
        # elif '.mp3' in path:
        #     a = pydub.AudioSegment.from_mp3(path)
        ext = path.split('.')[-1]
        a = pydub.AudioSegment.from_file(path, format=ext)
        sr = a.frame_rate
        data = np.array(a.get_array_of_samples()[::a.channels])
        data = data/data.max()
        data = data if data.ndim == 1 else data.mean(axis=1)
        self.w_plot.set_signal(data, sr)
        self.w_mp.set_contents(path)

    def clicked_window(self, event):
        self.w_mp.pause_handler()
        pos = event.scenePos()
        mousePoint = self.w_plot.p_signal.vb.mapSceneToView(pos)
        self.bar_0.setPos(mousePoint.x())
        self.w_mp.play_handler()


def main():
    app = QW.QApplication(sys.argv)

    w = SpectrogramTree()
    w.move(300, 300)

    # w.w_plot.set_signal(data, sr)
    # w.w_mp.set_contents(filename)

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
