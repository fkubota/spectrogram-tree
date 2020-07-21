import sys
import PyQt5.QtWidgets as QW


class WidgetTree(QW.QWidget):
    def __init__(self):
        super().__init__()
        self.pbar = QW.QProgressBar()
        self.lbl = QW.QLabel()

        self.init_ui()
        self.init_method()

    def init_ui(self):
        self.resize(300, 80)
        self.move(500, 500)

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.lbl)
        vbox0.addWidget(self.pbar)
        self.setLayout(vbox0)

    def init_method(self):
        self.lbl.setText('no message')


def main():
    app = QW.QApplication(sys.argv)

    w = WidgetProgressBar()
    w.move(600, 500)
    w.pbar.setMaximum(100)
    w.pbar.setValue(30)
    w.show()

    import time
    for i in range(1, 101):
        QW.QApplication.processEvents()
        w.pbar.setValue(i)
        time.sleep(0.05)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
