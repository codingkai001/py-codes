import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWidget(QMainWindow, QDialog):  # QMainWindow类基于QWidget类，因此本类直接继承QMainWindow即可
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.center()
        self.resize(800, 600)  # 窗口大小
        self.setWindowIcon(QIcon(r"C:\Users\Coding-Kai\Pictures\Saved Pictures\方块.png"))  # 窗口图标
        self.setWindowTitle("APP")  # 窗口标题
        self.setToolTip("看什么看 ^_^")  # # 鼠标停留在窗口一会儿会弹出提示信息
        QToolTip.setFont(QFont("楷体", 20))  # 设置提示信息的字体和大小

        # 菜单栏
        menu_control = self.menuBar().addMenu("Control")
        act_quit = menu_control.addAction("Exit")
        act_quit.triggered.connect(self.close)  # 信号-槽机制连接

        menu_help = self.menuBar().addMenu("Help")
        act_about = menu_help.addAction("About")
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction("About Qt")
        act_aboutqt.triggered.connect(self.aboutqt)

        # 状态栏
        self.statusBar().showMessage("程序已就绪...")  # 程序状态提示
        self.show()

    def about(self):
        QMessageBox.about(self, "about APP", "Wise System")

    def aboutqt(self):
        QMessageBox.aboutQt(self)

    def closeEvent(self, event):  # 重载父类的closeEvent
        """ 关闭窗口时弹出对话框 """
        reply = QMessageBox.question(self, "提示", "你确定要退出吗？", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    """窗口居中"""

    def center(self):
        screen = QDesktopWidget().screenGeometry()  # 返回屏幕的宽度和高度的像素
        # print(screen.width(), screen.height())    # 1920*1080
        size = self.geometry()  # 返回窗口的宽度和高度
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)  # 任何窗口程序都需要创建一个 QApplication 类的实例
    mywidget = MyWidget()
    mywidget.show()
    sys.exit(myapp.exec_())

"""
    import sys
    from PyQt5.QtWidgets import QHBoxLayout, QSlider, QSpinBox, QApplication, QWidget
    from PyQt5.QtCore import Qt

    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(800, 600)
    window.setWindowTitle("enter your age")
    spinBox = QSpinBox()
    slider = QSlider(Qt.Horizontal)
    spinBox.setRange(0, 130)
    slider.setRange(0, 130)
    spinBox.valueChanged.connect(slider.setValue)
    slider.valueChanged.connect(spinBox.setValue)
    spinBox.setValue(35)
    layout = QHBoxLayout()
    layout.addWidget(spinBox)
    layout.addWidget(slider)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
    """
