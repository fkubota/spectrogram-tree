import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtCore as QC


class WidgetTree(QW.QWidget):
    def __init__(self):
        super().__init__()

        self.model = QW.QFileSystemModel()
        self.tree = QW.QTreeView()

        self.init_ui()
        self.init_method()
        self.init_event()

    def init_ui(self):
        self.tree.sortByColumn(0, QC.Qt.AscendingOrder)

        # layout
        self.tree.resize(640, 480)
        vhox0 = QW.QVBoxLayout()
        vhox0.addWidget(self.tree)
        self.setLayout(vhox0)

    def init_method(self):
        self.model.setRootPath('')
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QC.QDir.homePath()))
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setColumnWidth(0, 300)

    def init_event(self):
        pass


def main():
    app = QW.QApplication(sys.argv)

    w = WidgetTree()
    w.move(600, 500)
    w.resize(500, 500)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
