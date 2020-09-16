import sys
import threading

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class Toast(QtWidgets.QWidget):
    background_color = QtGui.QColor("#778899")
    text_color = QtCore.Qt.black
    font = QtGui.QFont('Simsun', 10)
    text = ''
    times = 3
    parent = None
    min_height = 10
    min_width = 10
    pos = QtCore.QPointF(0, 0)

    def __init__(self, parent=None, ):
        super(Toast, self).__init__(parent)
        self.parent = parent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def init_UI(self):
        # 计算气泡长宽及移动气泡到指定位置
        self.height = self.get_font_size() * 2
        self.width = len(self.text) * self.height * 0.8
        if self.height < self.min_height:
            self.height = self.min_height
        # else:
        #     self.height = self.min_height * 2
        if self.width < self.min_width:
            self.width = self.min_width
        self.resize(int(self.width),int(self.height))
        if self.pos.x() != 0 or self.pos.y() != 0:
            self.move(int(self.pos.x() - self.width / 2),int(self.pos.y() - self.height / 2))

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.TextAntialiasing)
        rect_line_path = QtGui.QPainterPath()
        rectangle = QtCore.QRectF(0, 0, self.width, self.height)
        rect_line_path.addRoundedRect(rectangle, self.height / 2, self.height / 2, QtCore.Qt.AbsoluteSize)
        painter.fillPath(rect_line_path, QtGui.QColor(self.background_color))

        pen = QtGui.QPen(QtGui.QColor(self.text_color))
        painter.setPen(pen)
        painter.setFont(self.font)
        self.draw_text(painter)

    def get_font_size(self):
        return self.font.pointSizeF()

    def draw_text(self, painter):
        painter.drawText(QtCore.QRectF(0, 0, self.width, self.height),
                         QtCore.Qt.AlignCenter, self.text)

    def make_text(self, pos, text, times=None, background_color=None):
        if pos:
            self.pos = pos
        if text:
            self.text = text
        if times:
            self.times = times
        if background_color:
            self.background_color = background_color
        self.init_UI()
        self.repaint()
        self.show()

        toast_timer = threading.Timer(self.times, self.toast_timeout)
        toast_timer.start()

    def toast_timeout(self):
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    toast = Toast()
    toast.make_text(QtCore.QPointF(1000, 1000), "hahahaha", 5)
    sys.exit(app.exec_())
