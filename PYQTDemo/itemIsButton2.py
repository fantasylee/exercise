import sys
from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex, QVariant)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QItemDelegate, QPushButton, QTableView, QWidget)

class MainWindow(QWidget, Ui_MainFrom):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # #去掉标题头
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.m_flag = False
        self.Button = QPushButton(self)
        self.Button.setGeometry(QtCore.QRect(880, 80, 93, 41))
        # 列表显示
        self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(('视频网站','视频标题','播放地址','下载进度','操作',))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
        # 取数据库数据 输出来是个列表
        sortInfo = [('1', 1, 1,),('2', 1, 1, ),('3', 1, 1,)]
        # 动态渲染数据
        for row, row_data in enumerate(sortInfo):
            self.tableWidget.insertRow(row)         # 插入行
            for column in range(len(row_data)+2):   # 需要多插入2列
                # 如果遍历数小于需要插入的函数，就显示空
                if column < len(row_data):
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(row_data[column])))
                # 如果遍历数等于需要插入的函数
                if column == len(row_data):
                    # 传入当前id
                    print("row_data[0]",row+1)
                    # 添加两列 进度条 按钮
                    self.tableWidget.setCellWidget(row, column, self.ProgressBar(str(row_data[0])))
                    self.tableWidget.setCellWidget(row, column+1, self.buttonForRow(str(row_data[0])))


    # 进度条
    def ProgressBar(self, id):
        widget = QWidget()
        # 进度条
        statusBar = QProgressBar()
        statusBar.setStyleSheet(''' text-align : center;
                                                   background-color : LightCoral;
                                                   height : 30px;
                                                    ''')
        hLayout = QHBoxLayout()
        hLayout.addWidget(statusBar)
        widget.setLayout(hLayout)
        return widget




    # 列表内添加按钮
    def buttonForRow(self,id):
        widget = QWidget()
        # 路径
        downloadPath = QPushButton('路径')
        downloadPath.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')

        # 槽函数
        downloadPath.clicked.connect(lambda:downloadPath_action.downloadPath((id)))

        # 下载
        downLoad = QPushButton('下载')
        downLoad.setStyleSheet(''' text-align : center;
                                  background-color : DarkSeaGreen;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')



        # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')


        hLayout = QHBoxLayout()
        hLayout.addWidget(downloadPath)
        hLayout.addWidget(downLoad)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)

        return widget





def main():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()