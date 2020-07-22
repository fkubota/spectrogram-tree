import sys
import PyQt5.QtWidgets as QW


class WidgetTree(QW.QWidget):
    def __init__(self):
        super().__init__()

        self.model = QW.QFileSystemModel()
        self.tree = QW.QTreeView()

        self.init_ui()
        self.init_method()

    def init_ui(self):
        self.tree.resize(640, 480)
        vhox0 = QW.QVBoxLayout()
        vhox0.addWidget(self.tree)
        self.setLayout(vhox0)

    def init_method(self):
        self.model.setRootPath('')
        # self.model.setRootPath(QW.QDir.rootPath())
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setModel(self.model)


def main():
    app = QW.QApplication(sys.argv)

    w = WidgetTree()
    w.tree.setRootIndex(w.model.index("../data/"))
    w.move(600, 500)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
