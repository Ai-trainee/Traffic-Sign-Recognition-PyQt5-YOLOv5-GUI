# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1443, 794)
        mainWindow.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon/人工智能机器人＊.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("#mainWindow{border:none;}\n"
"QMainWindow {\n"
"    border: 1px solid #3d8ec9;\n"
"    border-radius: 10px;\n"
"    background-color: #f0f0f0;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 45))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 45))
        self.groupBox.setStyleSheet("#groupBox{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
";\n"
"border-radius:0px;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(25, 25))
        self.label_7.setMaximumSize(QtCore.QSize(27, 27))
        self.label_7.setStyleSheet("image: url(:/img/icon/29道路.png);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 24px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(59,59,59, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minButton = QtWidgets.QPushButton(self.groupBox)
        self.minButton.setMinimumSize(QtCore.QSize(50, 28))
        self.minButton.setMaximumSize(QtCore.QSize(50, 28))
        self.minButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.minButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icon/最小化 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minButton.setIcon(icon1)
        self.minButton.setIconSize(QtCore.QSize(44, 44))
        self.minButton.setObjectName("minButton")
        self.horizontalLayout_5.addWidget(self.minButton)
        self.maxButton = QtWidgets.QPushButton(self.groupBox)
        self.maxButton.setMinimumSize(QtCore.QSize(50, 28))
        self.maxButton.setMaximumSize(QtCore.QSize(50, 28))
        self.maxButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.maxButton.setLocale(QtCore.QLocale(QtCore.QLocale.Chuvash, QtCore.QLocale.Russia))
        self.maxButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icon/全屏 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maxButton.setIcon(icon2)
        self.maxButton.setCheckable(True)
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout_5.addWidget(self.maxButton)
        self.closeButton = QtWidgets.QPushButton(self.groupBox)
        self.closeButton.setMinimumSize(QtCore.QSize(50, 28))
        self.closeButton.setMaximumSize(QtCore.QSize(50, 28))
        self.closeButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.closeButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icon/关闭 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_5.addWidget(self.closeButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addWidget(self.groupBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("\n"
"QGroupBox {\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-right: 1px solid #3b3b3b;\n"
"  padding: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  color: white;\n"
"  font-family: \"Arial\";\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 10px;\n"
"  top: -12px;\n"
"  padding: 0 5px;\n"
"  background-color: #333333;\n"
"  border-top: 1px solid #3b3b3b;\n"
"  border-right: 1px solid #3b3b3b;\n"
"  border-bottom: 1px solid #3b3b3b;\n"
"  border-top-left-radius: 5px;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  width: 0;\n"
"  height: 0;\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  border: none;\n"
"}\n"
"\n"
"QGroupBox::label {\n"
"  border: none;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setContentsMargins(10, 0, -1, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, 22)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setStyleSheet("image: url(:/img/icon/yjtp-modified.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_16.addWidget(self.label_6)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setStyleSheet("image: url(:/img/icon/圆形选中.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem2)
        self.verticalLayout_16.setStretch(0, 12)
        self.verticalLayout_16.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.verticalLayout_16)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setContentsMargins(0, 0, 13, 0)
        self.verticalLayout_13.setSpacing(50)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"  color: #ffffff; /* 文本颜色 */\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 222, 170), stop:1 rgba(5, 115, 217,0.4)); /* 悬停时的背景渐变 */\n"
"  border: none; /* 去除边框 */\n"
"  border-radius: 5px; /* 圆角半径 */\n"
"  font-size: 14px; /* 文本字号 */\n"
"  font-weight: bold; /* 文本加粗 */\n"
"  padding: 5px; /* 按钮内边距 */\n"
"  min-width: 80px; /* 最小宽度 */\n"
"  min-height: 30px; /* 最小高度 */\n"
"  font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(3, 85, 160), stop:1 rgba(3, 85, 160,0.3)); /* 按钮背景渐变 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_13.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  color: #ffffff; /* 文本颜色 */\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 222, 170), stop:1 rgba(5, 115, 217,0.4)); /* 悬停时的背景渐变 */\n"
"  border: none; /* 去除边框 */\n"
"  border-radius: 5px; /* 圆角半径 */\n"
"  font-size: 14px; /* 文本字号 */\n"
"  font-weight: bold; /* 文本加粗 */\n"
"  padding: 5px; /* 按钮内边距 */\n"
"  min-width: 80px; /* 最小宽度 */\n"
"  min-height: 30px; /* 最小高度 */\n"
"  font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(3, 85, 160), stop:1 rgba(3, 85, 160,0.3)); /* 按钮背景渐变 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_13.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  color: #ffffff; /* 文本颜色 */\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 222, 170), stop:1 rgba(5, 115, 217,0.4)); /* 悬停时的背景渐变 */\n"
"  border: none; /* 去除边框 */\n"
"  border-radius: 5px; /* 圆角半径 */\n"
"  font-size: 14px; /* 文本字号 */\n"
"  font-weight: bold; /* 文本加粗 */\n"
"  padding: 5px; /* 按钮内边距 */\n"
"  min-width: 80px; /* 最小宽度 */\n"
"  min-height: 30px; /* 最小高度 */\n"
"  font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(3, 85, 160), stop:1 rgba(3, 85, 160,0.3)); /* 按钮背景渐变 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_13.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  color: #ffffff; /* 文本颜色 */\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 222, 170), stop:1 rgba(5, 115, 217,0.4)); /* 悬停时的背景渐变 */\n"
"  border: none; /* 去除边框 */\n"
"  border-radius: 5px; /* 圆角半径 */\n"
"  font-size: 14px; /* 文本字号 */\n"
"  font-weight: bold; /* 文本加粗 */\n"
"  padding: 5px; /* 按钮内边距 */\n"
"  min-width: 80px; /* 最小宽度 */\n"
"  min-height: 30px; /* 最小高度 */\n"
"  font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(3, 85, 160), stop:1 rgba(3, 85, 160,0.3)); /* 按钮背景渐变 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_13.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  color: #ffffff; /* 文本颜色 */\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(38, 222, 170), stop:1 rgba(5, 115, 217,0.4)); /* 悬停时的背景渐变 */\n"
"  border: none; /* 去除边框 */\n"
"  border-radius: 5px; /* 圆角半径 */\n"
"  font-size: 14px; /* 文本字号 */\n"
"  font-weight: bold; /* 文本加粗 */\n"
"  padding: 5px; /* 按钮内边距 */\n"
"  min-width: 80px; /* 最小宽度 */\n"
"  min-height: 30px; /* 最小高度 */\n"
"  font-family: \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(3, 85, 160), stop:1 rgba(3, 85, 160,0.3)); /* 按钮背景渐变 */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_13.addWidget(self.pushButton_3)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 7)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.tableView = QtWidgets.QTableView(self.page)
        self.tableView.setStyleSheet("QTableView {\n"
"    background-color: rgba(0, 0, 0, 255);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    gridline-color: rgba(128, 128, 128, 128);\n"
"    alternate-background-color: rgba(30, 30, 30, 255);\n"
"    selection-background-color: rgba(24, 170, 198, 255);\n"
"    selection-color: rgba(0, 0, 0, 255);\n"
"    font: 10pt \"Roboto\";\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32));\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32));\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"    padding-left: 4px;\n"
"    border: 1px solid rgba(13, 206, 197, 255);\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_18.addWidget(self.tableView)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.refreshButton_2 = QtWidgets.QPushButton(self.page)
        self.refreshButton_2.setStyleSheet("QPushButton {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.refreshButton_2.setObjectName("refreshButton_2")
        self.verticalLayout_9.addWidget(self.refreshButton_2)
        self.refreshButton = QtWidgets.QPushButton(self.page)
        self.refreshButton.setStyleSheet("QPushButton {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.refreshButton.setObjectName("refreshButton")
        self.verticalLayout_9.addWidget(self.refreshButton)
        self.insertButton_2 = QtWidgets.QPushButton(self.page)
        self.insertButton_2.setStyleSheet("QPushButton {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.insertButton_2.setObjectName("insertButton_2")
        self.verticalLayout_9.addWidget(self.insertButton_2)
        self.deleteButton_2 = QtWidgets.QPushButton(self.page)
        self.deleteButton_2.setStyleSheet("QPushButton {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.deleteButton_2.setObjectName("deleteButton_2")
        self.verticalLayout_9.addWidget(self.deleteButton_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.filterButton_3 = QtWidgets.QPushButton(self.page)
        self.filterButton_3.setStyleSheet("QPushButton {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.filterButton_3.setObjectName("filterButton_3")
        self.horizontalLayout_16.addWidget(self.filterButton_3)
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setStyleSheet("QSpinBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    font: 12pt;\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    width: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: rgba(13, 206, 197, 200);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"}\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_16.addWidget(self.spinBox)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 0, 1, 1)
        self.sortcomboBox_2 = QtWidgets.QComboBox(self.page)
        self.sortcomboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.sortcomboBox_2.setObjectName("sortcomboBox_2")
        self.sortcomboBox_2.addItem("")
        self.sortcomboBox_2.addItem("")
        self.gridLayout.addWidget(self.sortcomboBox_2, 0, 1, 1, 1)
        self.sortcomboBox_3 = QtWidgets.QComboBox(self.page)
        self.sortcomboBox_3.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.sortcomboBox_3.setObjectName("sortcomboBox_3")
        self.sortcomboBox_3.addItem("")
        self.sortcomboBox_3.addItem("")
        self.gridLayout.addWidget(self.sortcomboBox_3, 0, 2, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.verticalLayout_18.addLayout(self.verticalLayout_9)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.graphicsView = QtWidgets.QGraphicsView(self.page_2)
        self.graphicsView.setStyleSheet("QGraphicsView {\n"
"    background-color: rgba(0, 0, 0, 200);\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"}\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_10.addWidget(self.graphicsView)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.analysisComboBox = QtWidgets.QComboBox(self.page_2)
        self.analysisComboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.analysisComboBox.setObjectName("analysisComboBox")
        self.analysisComboBox.addItem("")
        self.analysisComboBox.addItem("")
        self.analysisComboBox.addItem("")
        self.analysisComboBox.addItem("")
        self.horizontalLayout_25.addWidget(self.analysisComboBox)
        self.refreshButton_3 = QtWidgets.QPushButton(self.page_2)
        self.refreshButton_3.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.refreshButton_3.setObjectName("refreshButton_3")
        self.horizontalLayout_25.addWidget(self.refreshButton_3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_25)
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stackedWidgetPage1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_3.setStyleSheet("#groupBox_3{\n"
"    background-color: rgb(59, 59, 59);\n"
"border: 0px solid #42adff;\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, -1, 11, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setMinimumSize(QtCore.QSize(0, 28))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 245, 175, 226), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 28))
        self.comboBox.setStyleSheet("QComboBox QAbstractItemView {\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"background:rgba(200, 200, 200,150);\n"
"selection-background-color: rgba(200, 200, 200,50);\n"
"color: rgb(218, 218, 218);\n"
"outline:none;\n"
"border:none;}\n"
"QComboBox{\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"border-width:0px;\n"
"border-color:white;\n"
"border-style:solid;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QComboBox::drop-down {\n"
"margin-top:8;\n"
"height:20;\n"
"background:rgba(255,255,255,0);\n"
"border-image: url(:/img/icon/下拉_白色.png);\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(11, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_10.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setStyleSheet("#groupBox_5{\n"
"background-color: rgba(48,148,243,0);\n"
"border: 0px solid #42adff;\n"
"border-left: 0px solid #d9d9d9;\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_8.setContentsMargins(13, 0, 13, 0)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.fileButton = QtWidgets.QPushButton(self.groupBox_5)
        self.fileButton.setMinimumSize(QtCore.QSize(55, 28))
        self.fileButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.fileButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(200, 200, 200,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.fileButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icon/文件夹-打开-没文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fileButton.setIcon(icon4)
        self.fileButton.setObjectName("fileButton")
        self.horizontalLayout_8.addWidget(self.fileButton)
        self.cameraButton = QtWidgets.QPushButton(self.groupBox_5)
        self.cameraButton.setMinimumSize(QtCore.QSize(53, 24))
        self.cameraButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.cameraButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.cameraButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/icon/摄像头 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraButton.setIcon(icon5)
        self.cameraButton.setIconSize(QtCore.QSize(24, 24))
        self.cameraButton.setObjectName("cameraButton")
        self.horizontalLayout_8.addWidget(self.cameraButton)
        self.rtspButton = QtWidgets.QPushButton(self.groupBox_5)
        self.rtspButton.setMinimumSize(QtCore.QSize(55, 28))
        self.rtspButton.setMaximumSize(QtCore.QSize(16777215, 28))
        self.rtspButton.setStyleSheet("QPushButton{font-family: \"Microsoft YaHei\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"color:white;\n"
"text-align: center center;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 4px;\n"
"padding-bottom: 4px;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-color: rgba(255, 255, 255, 255);\n"
"border-radius: 3px;\n"
"background-color: rgba(48,148,243,0);}\n"
"\n"
"QPushButton:focus{outline: none;}\n"
"\n"
"QPushButton::pressed{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"\n"
"QPushButton::disabled{font-family: \"Microsoft YaHei\";\n"
"                     font-size: 14px;\n"
"                     font-weight: bold;\n"
"                     color:rgb(200,200,200);\n"
"                     text-align: center center;\n"
"                     padding-left: 5px;\n"
"                     padding-right: 5px;\n"
"                     padding-top: 4px;\n"
"                     padding-bottom: 4px;\n"
"                     border-style: solid;\n"
"                     border-width: 0px;\n"
"                     border-color: rgba(255, 255, 255, 255);\n"
"                     border-radius: 3px;\n"
"                     background-color:  #bf513b;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(48,148,243,80);}")
        self.rtspButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/icon/链接.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rtspButton.setIcon(icon6)
        self.rtspButton.setIconSize(QtCore.QSize(24, 24))
        self.rtspButton.setObjectName("rtspButton")
        self.horizontalLayout_8.addWidget(self.rtspButton)
        self.horizontalLayout_11.addWidget(self.groupBox_5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.iouSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.iouSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.iouSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.iouSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.iouSpinBox.setMaximum(1.0)
        self.iouSpinBox.setSingleStep(0.01)
        self.iouSpinBox.setProperty("value", 0.45)
        self.iouSpinBox.setObjectName("iouSpinBox")
        self.horizontalLayout_4.addWidget(self.iouSpinBox)
        self.iouSlider = QtWidgets.QSlider(self.groupBox_3)
        self.iouSlider.setStyleSheet("QSlider{\n"
"border-color: #fff5eb;\n"
"color:#d9d9d9;\n"
"    \n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     \n"
"    border-image: url(:/img/icon/圆形选中.png);\n"
"     width:20px;\n"
"     margin: -10px -10px -10px -10px;                  \n"
"} \n"
"QSlider::sub-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::add-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.iouSlider.setMaximum(100)
        self.iouSlider.setProperty("value", 45)
        self.iouSlider.setOrientation(QtCore.Qt.Horizontal)
        self.iouSlider.setObjectName("iouSlider")
        self.horizontalLayout_4.addWidget(self.iouSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.confSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.confSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.confSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.confSpinBox.setStyleSheet("QDoubleSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QDoubleSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QDoubleSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QDoubleSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.confSpinBox.setMaximum(1.0)
        self.confSpinBox.setSingleStep(0.01)
        self.confSpinBox.setProperty("value", 0.25)
        self.confSpinBox.setObjectName("confSpinBox")
        self.horizontalLayout_3.addWidget(self.confSpinBox)
        self.confSlider = QtWidgets.QSlider(self.groupBox_3)
        self.confSlider.setStyleSheet("QSlider{\n"
"border-color: #fff5eb;\n"
"color:#d9d9d9;\n"
"    \n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     \n"
"    border-image: url(:/img/icon/圆形选中.png);\n"
"     width:20px;\n"
"     margin: -10px -10px -10px -10px;                  \n"
"} \n"
"QSlider::sub-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::add-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.confSlider.setMaximum(100)
        self.confSlider.setProperty("value", 25)
        self.confSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.confSlider.setObjectName("confSlider")
        self.horizontalLayout_3.addWidget(self.confSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_8.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);;}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_14.addWidget(self.checkBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rateSpinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.rateSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.rateSpinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.rateSpinBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rateSpinBox.setStyleSheet("QSpinBox{\n"
"background:rgba(200, 200, 200,50);\n"
"color:white;\n"
"font-size: 14px;\n"
"font-family: \"Microsoft YaHei UI\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(200, 200, 200,100);\n"
"border-radius: 3px;}\n"
"\n"
"QSpinBox::down-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"QDoubleSpinBox::down-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表展开.png);}\n"
"\n"
"QSpinBox::up-button{\n"
"background:rgba(200, 200, 200,0);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"QSpinBox::up-button::hover{\n"
"background:rgba(200, 200, 200,100);\n"
"border-image: url(:/img/icon/箭头_列表收起.png);}\n"
"")
        self.rateSpinBox.setMinimum(1)
        self.rateSpinBox.setMaximum(20)
        self.rateSpinBox.setSingleStep(1)
        self.rateSpinBox.setProperty("value", 1)
        self.rateSpinBox.setObjectName("rateSpinBox")
        self.horizontalLayout_13.addWidget(self.rateSpinBox)
        self.rateSlider = QtWidgets.QSlider(self.groupBox_3)
        self.rateSlider.setStyleSheet("QSlider{\n"
"border-color: #fff5eb;\n"
"color:#d9d9d9;\n"
"    \n"
"}\n"
"QSlider::groove:horizontal {                                \n"
"     border: 1px solid #999999;                             \n"
"     height: 3px;                                           \n"
"    margin: 0px 0;                                         \n"
"     left: 5px; right: 5px; \n"
" }\n"
"QSlider::handle:horizontal {                               \n"
"     border: 0px ; \n"
"     \n"
"    border-image: url(:/img/icon/圆形选中.png);\n"
"     width:20px;\n"
"     margin: -10px -10px -10px -10px;                  \n"
"} \n"
"QSlider::sub-page:horizontal{\n"
"background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d9d9d9, stop:0.25 #d9d9d9, stop:0.5 #d9d9d9, stop:1 #d9d9d9); \n"
"\n"
"}\n"
"QSlider::add-page:horizontal{                               \n"
" background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #373737, stop:0.25 #373737, stop:0.5 #373737, stop:1 #373737);                     \n"
"}")
        self.rateSlider.setMinimum(1)
        self.rateSlider.setMaximum(20)
        self.rateSlider.setSingleStep(1)
        self.rateSlider.setPageStep(1)
        self.rateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.rateSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.rateSlider.setObjectName("rateSlider")
        self.horizontalLayout_13.addWidget(self.rateSlider)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(67, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.fps_label = QtWidgets.QLabel(self.groupBox_3)
        self.fps_label.setMinimumSize(QtCore.QSize(100, 40))
        self.fps_label.setMaximumSize(QtCore.QSize(100, 40))
        self.fps_label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 20px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.fps_label.setText("")
        self.fps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fps_label.setObjectName("fps_label")
        self.horizontalLayout_6.addWidget(self.fps_label)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.groupBox_201 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_201.setStyleSheet("#groupBox_201{\n"
"\n"
"border: 0px solid #42adff;\n"
"    background-color: rgb(0, 0, 0);\n"
"border-left: 1px solid rgba(200, 200, 200,100);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-radius:0px;}")
        self.groupBox_201.setTitle("")
        self.groupBox_201.setObjectName("groupBox_201")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_201)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(self.groupBox_201)
        self.splitter.setEnabled(True)
        self.splitter.setStyleSheet("#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setLineWidth(10)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setObjectName("splitter")
        self.raw_video = Label_click_Mouse(self.splitter)
        self.raw_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raw_video.sizePolicy().hasHeightForWidth())
        self.raw_video.setSizePolicy(sizePolicy)
        self.raw_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.raw_video.setFont(font)
        self.raw_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.raw_video.setStyleSheet("color: rgb(218, 218, 218);\n"
"")
        self.raw_video.setText("")
        self.raw_video.setScaledContents(False)
        self.raw_video.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_video.setObjectName("raw_video")
        self.out_video = Label_click_Mouse(self.splitter)
        self.out_video.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.out_video.sizePolicy().hasHeightForWidth())
        self.out_video.setSizePolicy(sizePolicy)
        self.out_video.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.out_video.setFont(font)
        self.out_video.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.out_video.setStyleSheet("color: rgb(218, 218, 218);\n"
"")
        self.out_video.setText("")
        self.out_video.setScaledContents(False)
        self.out_video.setAlignment(QtCore.Qt.AlignCenter)
        self.out_video.setObjectName("out_video")
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.runButton = QtWidgets.QPushButton(self.groupBox_201)
        self.runButton.setMinimumSize(QtCore.QSize(40, 40))
        self.runButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.runButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/icon/播放 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runButton.setIcon(icon7)
        self.runButton.setIconSize(QtCore.QSize(30, 30))
        self.runButton.setCheckable(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_12.addWidget(self.runButton)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_201)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    color: rgb(26, 255, 217);\n"
"    font: 12pt;\n"
"    border-radius: 2px;\n"
"    text-align: center;\n"
"    border: none;\n"
"    background-color: rgba(215, 215, 215, 100);\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"    border-radius: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(3, 85, 160, 255), stop:1 rgba(13, 206, 197, 255));\n"
"}\n"
"")
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_12.addWidget(self.progressBar)
        self.stopButton = QtWidgets.QPushButton(self.groupBox_201)
        self.stopButton.setMinimumSize(QtCore.QSize(40, 40))
        self.stopButton.setStyleSheet("QPushButton {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 0);\n"
"}\n"
"QPushButton::focus{outline: none;}\n"
"QPushButton::hover {\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 0px;\n"
"background-color: rgba(223, 223, 223, 150);}")
        self.stopButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/icon/结束.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon8)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_12.addWidget(self.stopButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_4.setStretch(0, 1)
        self.horizontalLayout_15.addWidget(self.groupBox_201)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_9 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_9.setStyleSheet("#groupBox_9{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 0px solid #42adff;\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"border-bottom: 1px solid rgba(200, 200, 200,100);\n"
"border-radius:0px;}")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_38.setContentsMargins(6, 0, 11, 0)
        self.horizontalLayout_38.setSpacing(9)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.groupBox_9)
        self.label_5.setMaximumSize(QtCore.QSize(25, 25))
        self.label_5.setStyleSheet("image: url(:/img/icon/预警信息 (1).png);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_38.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setStyleSheet("QLabel\n"
"\n"
"{\n"
"    font-size: 22px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgba(66, 195, 255, 0);\n"
"    color: rgb(24, 240, 197);\n"
"    \n"
"    \n"
"}\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_38.addWidget(self.label_11)
        spacerItem5 = QtWidgets.QSpacerItem(37, 39, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem5)
        self.verticalLayout_7.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 42))
        self.groupBox_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_10.setStyleSheet("QGroupBox {\n"
"  background-color: #333333;\n"
"  border: none;\n"
"  border-right: 1px solid #3b3b3b;\n"
"  padding: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  color: white;\n"
"  font-family: \"Arial\";\n"
"  font-size: 16px;\n"
"  font-weight: bold;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  left: 10px;\n"
"  top: -12px;\n"
"  padding: 0 5px;\n"
"  background-color: #333333;\n"
"  border-top: 1px solid #3b3b3b;\n"
"  border-right: 1px solid #3b3b3b;\n"
"  border-bottom: 1px solid #3b3b3b;\n"
"  border-top-left-radius: 5px;\n"
"  border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::indicator {\n"
"  width: 0;\n"
"  height: 0;\n"
"  padding: 0;\n"
"  margin: 0;\n"
"  border: none;\n"
"}\n"
"\n"
"QGroupBox::label {\n"
"  border: none;\n"
"}\n"
"")
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_39.setContentsMargins(11, 0, 11, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.resultWidget = QtWidgets.QListWidget(self.groupBox_10)
        self.resultWidget.setStyleSheet("QListWidget{\n"
"background-color: rgba(12, 28, 77, 0);\n"
"\n"
"border-radius:0px;\n"
"font-family: \"Microsoft YaHei\";\n"
"font-size: 16px;\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.resultWidget.setObjectName("resultWidget")
        self.horizontalLayout_39.addWidget(self.resultWidget)
        self.verticalLayout_7.addWidget(self.groupBox_10)
        self.verticalLayout_7.setStretch(1, 1)
        self.horizontalLayout_15.addLayout(self.verticalLayout_7)
        self.horizontalLayout_15.setStretch(0, 6)
        self.horizontalLayout_15.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.groupBox_4 = QtWidgets.QGroupBox(self.stackedWidgetPage1)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.groupBox_4.setStyleSheet("#groupBox_4{\n"
"background-color: rgb(59,59,59);\n"
"\n"
"border-left: 0px solid rgba(29, 83, 185, 255);\n"
"border-right: 0px solid rgba(29, 83, 185, 255);\n"
"border-top: 1px solid rgba(200, 200, 200,100);\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 42))
        self.groupBox_6.setStyleSheet("#groupBox_6{\n"
"    background-color: rgb(59, 59, 59);\n"
"border: 0px solid #42adff;\n"
"border-radius:0px;}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_36.setContentsMargins(0, 0, 11, 0)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.saveCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.saveCheckBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgb(59,59,59);\n"
"\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 245, 175, 226), stop:1 rgba(255, 255, 255, 255));}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.saveCheckBox.setChecked(True)
        self.saveCheckBox.setObjectName("saveCheckBox")
        self.horizontalLayout_36.addWidget(self.saveCheckBox)
        self.SavedatabaseCheckBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.SavedatabaseCheckBox.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgb(59,59,59);\n"
"\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 245, 175, 226), stop:1 rgba(255, 255, 255, 255));}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.SavedatabaseCheckBox.setObjectName("SavedatabaseCheckBox")
        self.horizontalLayout_36.addWidget(self.SavedatabaseCheckBox)
        self.visualize_checkbox1 = QtWidgets.QCheckBox(self.groupBox_6)
        self.visualize_checkbox1.setStyleSheet("\n"
"QCheckBox\n"
"{font-size: 18px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: bold;\n"
"         border-radius:9px;\n"
"        background:rgb(59,59,59);\n"
"\n"
"    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(33, 245, 175, 226), stop:1 rgba(255, 255, 255, 255));}\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/img/icon/button-off.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    \n"
"    \n"
"    image: url(:/img/icon/button-on.png);\n"
"}\n"
"")
        self.visualize_checkbox1.setObjectName("visualize_checkbox1")
        self.horizontalLayout_36.addWidget(self.visualize_checkbox1)
        self.horizontalLayout_10.addWidget(self.groupBox_6)
        self.statistic_label = QtWidgets.QLabel(self.groupBox_4)
        self.statistic_label.setMouseTracking(False)
        self.statistic_label.setStyleSheet("QLabel\n"
"{\n"
"    font-size: 16px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"    font-weight: light;\n"
"    background-color: rgb(0, 0, 0);\n"
"color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.statistic_label.setText("")
        self.statistic_label.setObjectName("statistic_label")
        self.horizontalLayout_10.addWidget(self.statistic_label)
        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 998, 551))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.imageLabel = QtWidgets.QLabel(self.widget)
        self.imageLabel.setStyleSheet("QLabel {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,1), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgba(3, 85, 160, 200), stop: 1 rgba(13, 206, 197, 200));\n"
"}\n"
"\n"
"QLabel::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    image: url(:/icons/your_icon.png);\n"
"    opacity: 0.5;\n"
"    position: absolute;\n"
"    left: 50%;\n"
"    top: 50%;\n"
"    margin-left: -8px;\n"
"    margin-top: -8px;\n"
"}\n"
"")
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_27.addWidget(self.imageLabel)
        self.imageLabel_2 = QtWidgets.QLabel(self.widget)
        self.imageLabel_2.setStyleSheet("QLabel {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QLabel::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    image: url(:/icons/your_icon.png);\n"
"    opacity: 0.5;\n"
"    position: absolute;\n"
"    left: 50%;\n"
"    top: 50%;\n"
"    margin-left: -8px;\n"
"    margin-top: -8px;\n"
"}\n"
"")
        self.imageLabel_2.setText("")
        self.imageLabel_2.setObjectName("imageLabel_2")
        self.horizontalLayout_27.addWidget(self.imageLabel_2)
        self.horizontalLayout_24.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.imageFilterButton = QtWidgets.QPushButton(self.page_3)
        self.imageFilterButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.imageFilterButton.setObjectName("imageFilterButton")
        self.horizontalLayout_28.addWidget(self.imageFilterButton)
        self.imageFilterComboBox = QtWidgets.QComboBox(self.page_3)
        self.imageFilterComboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.imageFilterComboBox.setObjectName("imageFilterComboBox")
        self.imageFilterComboBox.addItem("")
        self.imageFilterComboBox.addItem("")
        self.imageFilterComboBox.addItem("")
        self.horizontalLayout_28.addWidget(self.imageFilterComboBox)
        self.previewFilterButton = QtWidgets.QPushButton(self.page_3)
        self.previewFilterButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.previewFilterButton.setObjectName("previewFilterButton")
        self.horizontalLayout_28.addWidget(self.previewFilterButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_28, 0, 0, 1, 1)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.morphologyButton = QtWidgets.QPushButton(self.page_3)
        self.morphologyButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.morphologyButton.setObjectName("morphologyButton")
        self.horizontalLayout_31.addWidget(self.morphologyButton)
        self.morphologyComboBox = QtWidgets.QComboBox(self.page_3)
        self.morphologyComboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.morphologyComboBox.setObjectName("morphologyComboBox")
        self.morphologyComboBox.addItem("")
        self.morphologyComboBox.addItem("")
        self.morphologyComboBox.addItem("")
        self.morphologyComboBox.addItem("")
        self.horizontalLayout_31.addWidget(self.morphologyComboBox)
        self.previewmorphologyButton = QtWidgets.QPushButton(self.page_3)
        self.previewmorphologyButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.previewmorphologyButton.setObjectName("previewmorphologyButton")
        self.horizontalLayout_31.addWidget(self.previewmorphologyButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_31, 1, 0, 1, 1)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.histogramButton = QtWidgets.QPushButton(self.page_3)
        self.histogramButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.histogramButton.setObjectName("histogramButton")
        self.horizontalLayout_32.addWidget(self.histogramButton)
        self.histogramComboBox = QtWidgets.QComboBox(self.page_3)
        self.histogramComboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.histogramComboBox.setObjectName("histogramComboBox")
        self.histogramComboBox.addItem("")
        self.horizontalLayout_32.addWidget(self.histogramComboBox)
        self.previewhistogramButton = QtWidgets.QPushButton(self.page_3)
        self.previewhistogramButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.previewhistogramButton.setObjectName("previewhistogramButton")
        self.horizontalLayout_32.addWidget(self.previewhistogramButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_32, 2, 0, 1, 1)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.imageEnhanceButton = QtWidgets.QPushButton(self.page_3)
        self.imageEnhanceButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.imageEnhanceButton.setObjectName("imageEnhanceButton")
        self.horizontalLayout_26.addWidget(self.imageEnhanceButton)
        self.imageEnhanceComboBox = QtWidgets.QComboBox(self.page_3)
        self.imageEnhanceComboBox.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    \n"
"    \n"
"    font: 9pt \"Arial\";\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.imageEnhanceComboBox.setObjectName("imageEnhanceComboBox")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.imageEnhanceComboBox.addItem("")
        self.horizontalLayout_26.addWidget(self.imageEnhanceComboBox)
        self.apply_custom_adjustments_imageEnhance = QtWidgets.QPushButton(self.page_3)
        self.apply_custom_adjustments_imageEnhance.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"image: url(:/img/icon/6-医疗-神经网络 (2).png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(3, 85, 160)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.apply_custom_adjustments_imageEnhance.setObjectName("apply_custom_adjustments_imageEnhance")
        self.horizontalLayout_26.addWidget(self.apply_custom_adjustments_imageEnhance)
        self.previewEnhanceButton = QtWidgets.QPushButton(self.page_3)
        self.previewEnhanceButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(13, 206, 197), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.previewEnhanceButton.setObjectName("previewEnhanceButton")
        self.horizontalLayout_26.addWidget(self.previewEnhanceButton)
        self.gridLayout_7.addLayout(self.horizontalLayout_26, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_7, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.loadImageButton = QtWidgets.QPushButton(self.page_3)
        self.loadImageButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.loadImageButton.setObjectName("loadImageButton")
        self.verticalLayout_21.addWidget(self.loadImageButton)
        self.openFolderButton = QtWidgets.QPushButton(self.page_3)
        self.openFolderButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.openFolderButton.setObjectName("openFolderButton")
        self.verticalLayout_21.addWidget(self.openFolderButton)
        self.saveFolderButton = QtWidgets.QPushButton(self.page_3)
        self.saveFolderButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.saveFolderButton.setObjectName("saveFolderButton")
        self.verticalLayout_21.addWidget(self.saveFolderButton)
        self.saveButton = QtWidgets.QPushButton(self.page_3)
        self.saveButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(24, 170, 198), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_21.addWidget(self.saveButton)
        self.gridLayout_4.addLayout(self.verticalLayout_21, 0, 0, 1, 1)
        self.verticalLayout1234124 = QtWidgets.QVBoxLayout()
        self.verticalLayout1234124.setObjectName("verticalLayout1234124")
        self.previewLabel = QtWidgets.QLabel(self.page_3)
        self.previewLabel.setStyleSheet("QLabel {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QLabel::hover {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(0, 211, 0), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QLabel::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    image: url(:/icons/your_icon.png);\n"
"    opacity: 0.5;\n"
"    position: absolute;\n"
"    left: 50%;\n"
"    top: 50%;\n"
"    margin-left: -8px;\n"
"    margin-top: -8px;\n"
"}\n"
"")
        self.previewLabel.setText("")
        self.previewLabel.setObjectName("previewLabel")
        self.verticalLayout1234124.addWidget(self.previewLabel)
        self.gridLayout_4.addLayout(self.verticalLayout1234124, 0, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.rotationSlider = QtWidgets.QSlider(self.page_3)
        self.rotationSlider.setStyleSheet("QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E6E6E6, stop: 1.0 #24c4da);\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop:0 rgb(238, 118, 33), stop:1 rgb(97, 194, 0));\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop:0 rgba(238, 118, 33,0.1), stop:1 rgba(97, 194, 0,0.8));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #3F3F3F;\n"
"}\n"
"")
        self.rotationSlider.setMaximum(360)
        self.rotationSlider.setSingleStep(1)
        self.rotationSlider.setProperty("value", 123)
        self.rotationSlider.setOrientation(QtCore.Qt.Vertical)
        self.rotationSlider.setObjectName("rotationSlider")
        self.gridLayout_6.addWidget(self.rotationSlider, 0, 1, 1, 1)
        self.slider_adjust_contrast = QtWidgets.QSlider(self.page_3)
        self.slider_adjust_contrast.setStyleSheet("QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E6E6E6, stop: 1.0 #24c4da);\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(24, 170, 198), stop: 1 rgb(216, 33, 32));\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(24, 170, 198), stop: 1 rgb(216, 33, 32));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #3F3F3F;\n"
"}\n"
"")
        self.slider_adjust_contrast.setMinimum(-50)
        self.slider_adjust_contrast.setMaximum(50)
        self.slider_adjust_contrast.setPageStep(10)
        self.slider_adjust_contrast.setProperty("value", 35)
        self.slider_adjust_contrast.setOrientation(QtCore.Qt.Vertical)
        self.slider_adjust_contrast.setObjectName("slider_adjust_contrast")
        self.gridLayout_6.addWidget(self.slider_adjust_contrast, 0, 3, 1, 1)
        self.scaleSlider = QtWidgets.QSlider(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleSlider.sizePolicy().hasHeightForWidth())
        self.scaleSlider.setSizePolicy(sizePolicy)
        self.scaleSlider.setStyleSheet("QSlider::groove:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E6E6E6, stop: 1.0 #24c4da);\n"
"    width: 10px;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(5, 170, 198), stop: 1 rgb(116, 13, 92));\n"
"    border: 1px solid #5c5c5c;\n"
"    height: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"   background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgba(4, 170, 98,1.5), stop: 1 rgba(116, 13, 12,4.6));\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #3F3F3F;\n"
"}\n"
"")
        self.scaleSlider.setMinimum(50)
        self.scaleSlider.setMaximum(200)
        self.scaleSlider.setPageStep(0)
        self.scaleSlider.setProperty("value", 150)
        self.scaleSlider.setOrientation(QtCore.Qt.Vertical)
        self.scaleSlider.setObjectName("scaleSlider")
        self.gridLayout_6.addWidget(self.scaleSlider, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.horizontalLayout111111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout111111.setObjectName("horizontalLayout111111")
        self.previousImageButton = QtWidgets.QPushButton(self.page_3)
        self.previousImageButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255,0.8), stop:1 rgba(216, 33, 32,0.3)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.previousImageButton.setObjectName("previousImageButton")
        self.horizontalLayout111111.addWidget(self.previousImageButton)
        self.nextImageButton = QtWidgets.QPushButton(self.page_3)
        self.nextImageButton.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 rgb(38, 222, 170,0.3), stop: 1 rgba(13, 206, 197, 255));\n"
"    border: 1px solid rgba(128, 128, 128, 128);\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 5px rgba(0, 0, 0, 50);\n"
"    color: rgba(255, 255, 255, 255);\n"
"    font: 10pt \"Roboto\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(24, 170, 198,0.2), stop:1 rgb(216, 33, 32)); /* 悬停时的背景渐变 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  color: rgb(3, 85, 160); /* 按下时的文本颜色 */\n"
"  background-color: #767676; /* 按下时的背景色 */\n"
"}\n"
"")
        self.nextImageButton.setObjectName("nextImageButton")
        self.horizontalLayout111111.addWidget(self.nextImageButton)
        self.gridLayout_5.addLayout(self.horizontalLayout111111, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_20.addLayout(self.gridLayout_2)
        self.verticalLayout_20.setStretch(0, 22)
        self.verticalLayout_20.setStretch(1, 1)
        self.horizontalLayout_17.addLayout(self.verticalLayout_20)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.enhanceMethod1Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod1Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod1Checkbox.setChecked(True)
        self.enhanceMethod1Checkbox.setObjectName("enhanceMethod1Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod1Checkbox)
        self.enhanceMethod2Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod2Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod2Checkbox.setChecked(True)
        self.enhanceMethod2Checkbox.setObjectName("enhanceMethod2Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod2Checkbox)
        self.enhanceMethod3Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod3Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod3Checkbox.setChecked(False)
        self.enhanceMethod3Checkbox.setObjectName("enhanceMethod3Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod3Checkbox)
        self.enhanceMethod4Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod4Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod4Checkbox.setChecked(True)
        self.enhanceMethod4Checkbox.setObjectName("enhanceMethod4Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod4Checkbox)
        self.enhanceMethod5Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod5Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod5Checkbox.setObjectName("enhanceMethod5Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod5Checkbox)
        self.enhanceMethod6Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod6Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod6Checkbox.setObjectName("enhanceMethod6Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod6Checkbox)
        self.enhanceMethod7Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod7Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod7Checkbox.setObjectName("enhanceMethod7Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod7Checkbox)
        self.enhanceMethod8Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod8Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod8Checkbox.setChecked(True)
        self.enhanceMethod8Checkbox.setObjectName("enhanceMethod8Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod8Checkbox)
        self.enhanceMethod9Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod9Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod9Checkbox.setChecked(False)
        self.enhanceMethod9Checkbox.setObjectName("enhanceMethod9Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod9Checkbox)
        self.enhanceMethod10Checkbox = QtWidgets.QCheckBox(self.page_3)
        self.enhanceMethod10Checkbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceMethod10Checkbox.setChecked(False)
        self.enhanceMethod10Checkbox.setObjectName("enhanceMethod10Checkbox")
        self.verticalLayout_19.addWidget(self.enhanceMethod10Checkbox)
        self.helpButton = QtWidgets.QPushButton(self.page_3)
        self.helpButton.setStyleSheet("QPushButton {\n"
"\n"
"image: url(:/img/icon/6-医疗-神经网络 (2).png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}")
        self.helpButton.setText("")
        self.helpButton.setObjectName("helpButton")
        self.verticalLayout_19.addWidget(self.helpButton)
        self.advancedSettingsButton = QtWidgets.QPushButton(self.page_3)
        self.advancedSettingsButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}\n"
"")
        self.advancedSettingsButton.setObjectName("advancedSettingsButton")
        self.verticalLayout_19.addWidget(self.advancedSettingsButton)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_19.addItem(spacerItem6)
        self.progressBar_2 = QtWidgets.QProgressBar(self.page_3)
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"  background-color: rgba(255, 255, 255, 0.1);\n"
"  height: 20px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  border-radius: 5px;\n"
"  background-color: QLinearGradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(38, 210, 166, 1), stop:0.5 rgba(38, 210, 166, 1), stop:1 rgba(227, 24, 23,1));\n"
"  width: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"  margin: 0.5px;\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical {\n"
"  margin: 0.5px;\n"
"  transform: rotate(90deg);\n"
"}")
        self.progressBar_2.setProperty("value", 80)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_19.addWidget(self.progressBar_2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.enhanceProbabilityInput = QtWidgets.QLineEdit(self.page_3)
        self.enhanceProbabilityInput.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    color: #FFFFFF;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.enhanceProbabilityInput.setObjectName("enhanceProbabilityInput")
        self.horizontalLayout_29.addWidget(self.enhanceProbabilityInput)
        self.label_18 = QtWidgets.QLabel(self.page_3)
        self.label_18.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_29.addWidget(self.label_18)
        self.verticalLayout_11.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.inputFolderLabel = QtWidgets.QLabel(self.page_3)
        self.inputFolderLabel.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.inputFolderLabel.setText("")
        self.inputFolderLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.inputFolderLabel.setObjectName("inputFolderLabel")
        self.horizontalLayout_30.addWidget(self.inputFolderLabel)
        self.inputFolderButton = QtWidgets.QPushButton(self.page_3)
        self.inputFolderButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}\n"
"")
        self.inputFolderButton.setObjectName("inputFolderButton")
        self.horizontalLayout_30.addWidget(self.inputFolderButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.outputFolderLabel = QtWidgets.QLabel(self.page_3)
        self.outputFolderLabel.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color:rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.outputFolderLabel.setText("")
        self.outputFolderLabel.setObjectName("outputFolderLabel")
        self.horizontalLayout_34.addWidget(self.outputFolderLabel)
        self.outputFolderButton = QtWidgets.QPushButton(self.page_3)
        self.outputFolderButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}\n"
"")
        self.outputFolderButton.setObjectName("outputFolderButton")
        self.horizontalLayout_34.addWidget(self.outputFolderButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_34)
        self.startProcessingButton = QtWidgets.QPushButton(self.page_3)
        self.startProcessingButton.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}\n"
"")
        self.startProcessingButton.setObjectName("startProcessingButton")
        self.verticalLayout_11.addWidget(self.startProcessingButton)
        self.verticalLayout_19.addLayout(self.verticalLayout_11)
        self.horizontalLayout_17.addLayout(self.verticalLayout_19)
        self.horizontalLayout_17.setStretch(0, 100)
        self.horizontalLayout_17.setStretch(1, 1)
        self.gridLayout_8.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.hide_labelscheckbox_5 = QtWidgets.QCheckBox(self.page_4)
        self.hide_labelscheckbox_5.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.hide_labelscheckbox_5.setChecked(True)
        self.hide_labelscheckbox_5.setObjectName("hide_labelscheckbox_5")
        self.verticalLayout_12.addWidget(self.hide_labelscheckbox_5)
        self.save_cropcheckbox_2 = QtWidgets.QCheckBox(self.page_4)
        self.save_cropcheckbox_2.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.save_cropcheckbox_2.setObjectName("save_cropcheckbox_2")
        self.verticalLayout_12.addWidget(self.save_cropcheckbox_2)
        self.agnostic_nmscheckbox_2 = QtWidgets.QCheckBox(self.page_4)
        self.agnostic_nmscheckbox_2.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.agnostic_nmscheckbox_2.setObjectName("agnostic_nmscheckbox_2")
        self.verticalLayout_12.addWidget(self.agnostic_nmscheckbox_2)
        self.halfcheckbox_2 = QtWidgets.QCheckBox(self.page_4)
        self.halfcheckbox_2.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(255, 0, 0, 255), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.halfcheckbox_2.setObjectName("halfcheckbox_2")
        self.verticalLayout_12.addWidget(self.halfcheckbox_2)
        self.agnostic_nmscheckbox = QtWidgets.QCheckBox(self.page_4)
        self.agnostic_nmscheckbox.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.agnostic_nmscheckbox.setObjectName("agnostic_nmscheckbox")
        self.verticalLayout_12.addWidget(self.agnostic_nmscheckbox)
        self.augmentedcheckbox_3 = QtWidgets.QCheckBox(self.page_4)
        self.augmentedcheckbox_3.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.augmentedcheckbox_3.setObjectName("augmentedcheckbox_3")
        self.verticalLayout_12.addWidget(self.augmentedcheckbox_3)
        self.hide_labelscheckbox_4 = QtWidgets.QCheckBox(self.page_4)
        self.hide_labelscheckbox_4.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.hide_labelscheckbox_4.setObjectName("hide_labelscheckbox_4")
        self.verticalLayout_12.addWidget(self.hide_labelscheckbox_4)
        self.hide_confscheckbox_6 = QtWidgets.QCheckBox(self.page_4)
        self.hide_confscheckbox_6.setStyleSheet("QCheckBox {\n"
"    spacing: 5px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(38, 222, 170, 0.1), stop: 1.0 rgba(13, 206, 197, 255));\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    image: url(:/img/icon/checked.png);\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed, QCheckBox::indicator:checked:pressed {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.hide_confscheckbox_6.setObjectName("hide_confscheckbox_6")
        self.verticalLayout_12.addWidget(self.hide_confscheckbox_6)
        self.verticalLayout_17.addLayout(self.verticalLayout_12)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_23.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_4)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    font: 12pt;\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 20px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"    \n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    selection-background-color: rgba(13, 206, 197, 200);\n"
"    selection-color: #FFFFFF;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"    background: rgba(55, 55, 55, 200);\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: rgba(13, 206, 197, 200);\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_23.addWidget(self.comboBox_2)
        self.verticalLayout_14.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_19.addWidget(self.label_12)
        self.imgsz_spinbox12 = QtWidgets.QSpinBox(self.page_4)
        self.imgsz_spinbox12.setStyleSheet("QSpinBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    font: 12pt;\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    width: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: rgba(13, 206, 197, 200);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"}\n"
"")
        self.imgsz_spinbox12.setMinimum(320)
        self.imgsz_spinbox12.setMaximum(10280)
        self.imgsz_spinbox12.setSingleStep(256)
        self.imgsz_spinbox12.setProperty("value", 1028)
        self.imgsz_spinbox12.setObjectName("imgsz_spinbox12")
        self.horizontalLayout_19.addWidget(self.imgsz_spinbox12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_21.addWidget(self.label_14)
        self.line_thickness_spinbox12_2 = QtWidgets.QSpinBox(self.page_4)
        self.line_thickness_spinbox12_2.setStyleSheet("QSpinBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    font: 12pt;\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    width: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: rgba(13, 206, 197, 200);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"}\n"
"")
        self.line_thickness_spinbox12_2.setMinimum(1)
        self.line_thickness_spinbox12_2.setMaximum(20)
        self.line_thickness_spinbox12_2.setSingleStep(1)
        self.line_thickness_spinbox12_2.setProperty("value", 3)
        self.line_thickness_spinbox12_2.setObjectName("line_thickness_spinbox12_2")
        self.horizontalLayout_21.addWidget(self.line_thickness_spinbox12_2)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_22.addWidget(self.label_15)
        self.line_thickness_spinbox12_3 = QtWidgets.QSpinBox(self.page_4)
        self.line_thickness_spinbox12_3.setStyleSheet("QSpinBox {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    color: #FFFFFF;\n"
"    font: 12pt;\n"
"    border: 1px solid #3F3F3F;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    image: url(:/img/icon/人工智能机器人＊.png);\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: rgba(55, 55, 55, 200);\n"
"    width: 20px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: rgba(13, 206, 197, 200);\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    background: rgba(255, 255, 255, 200);\n"
"}\n"
"")
        self.line_thickness_spinbox12_3.setMinimum(100)
        self.line_thickness_spinbox12_3.setMaximum(5000)
        self.line_thickness_spinbox12_3.setSingleStep(10)
        self.line_thickness_spinbox12_3.setProperty("value", 1000)
        self.line_thickness_spinbox12_3.setObjectName("line_thickness_spinbox12_3")
        self.horizontalLayout_22.addWidget(self.line_thickness_spinbox12_3)
        self.verticalLayout_14.addLayout(self.horizontalLayout_22)
        self.verticalLayout_17.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setStyleSheet("QLabel {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QLabel:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.lineEdit = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    color: #FFFFFF;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_18.addWidget(self.lineEdit)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.result_folder_lineEdit = QtWidgets.QLineEdit(self.page_4)
        self.result_folder_lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"    color: #FFFFFF;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #FFFFFF;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"")
        self.result_folder_lineEdit.setObjectName("result_folder_lineEdit")
        self.horizontalLayout_20.addWidget(self.result_folder_lineEdit)
        self.browse_result_folder_button = QtWidgets.QPushButton(self.page_4)
        self.browse_result_folder_button.setStyleSheet("QPushButton {\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    background-color: rgba(38, 222, 170, 0.1);\n"
"    border: 1px solid rgba(13, 206, 197, 100);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    background-color: rgba(13, 206, 197, 100);\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    text-shadow: 0 0 3px rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 150);\n"
"    background-color: rgba(3, 85, 160, 150);\n"
"    border: 1px solid rgba(13, 206, 197, 150);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 100);\n"
"    background-color: rgba(3, 85, 160, 50);\n"
"    border: 1px solid rgba(13, 206, 197, 50);\n"
"}\n"
"")
        self.browse_result_folder_button.setObjectName("browse_result_folder_button")
        self.horizontalLayout_20.addWidget(self.browse_result_folder_button)
        self.verticalLayout_15.addLayout(self.horizontalLayout_20)
        self.verticalLayout_17.addLayout(self.verticalLayout_15)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_7.addWidget(self.stackedWidget)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "道路标志识别"))
        self.label_4.setText(_translate("mainWindow", "道路标志识别"))
        self.pushButton_5.setText(_translate("mainWindow", "参数设置"))
        self.pushButton.setText(_translate("mainWindow", "标志识别"))
        self.pushButton_4.setText(_translate("mainWindow", "数据库"))
        self.pushButton_2.setText(_translate("mainWindow", "图像处理"))
        self.pushButton_3.setText(_translate("mainWindow", "用户信息"))
        self.refreshButton_2.setText(_translate("mainWindow", "数据分析"))
        self.refreshButton.setText(_translate("mainWindow", "显示数据"))
        self.insertButton_2.setText(_translate("mainWindow", "插入数据"))
        self.deleteButton_2.setText(_translate("mainWindow", "删除数据"))
        self.filterButton_3.setText(_translate("mainWindow", "数据筛选"))
        self.label_17.setText(_translate("mainWindow", "数据排序"))
        self.sortcomboBox_2.setItemText(0, _translate("mainWindow", "sign_count"))
        self.sortcomboBox_2.setItemText(1, _translate("mainWindow", "detection_time"))
        self.sortcomboBox_3.setItemText(0, _translate("mainWindow", "asc"))
        self.sortcomboBox_3.setItemText(1, _translate("mainWindow", "desc"))
        self.analysisComboBox.setItemText(0, _translate("mainWindow", "柱状图"))
        self.analysisComboBox.setItemText(1, _translate("mainWindow", "折线图"))
        self.analysisComboBox.setItemText(2, _translate("mainWindow", "饼图"))
        self.analysisComboBox.setItemText(3, _translate("mainWindow", "箱线图"))
        self.refreshButton_3.setText(_translate("mainWindow", "确定"))
        self.label_3.setText(_translate("mainWindow", "model"))
        self.comboBox.setItemText(0, _translate("mainWindow", "yolov5s.pt"))
        self.comboBox.setItemText(1, _translate("mainWindow", "yolov5m.pt"))
        self.comboBox.setItemText(2, _translate("mainWindow", "yolov5l.pt"))
        self.comboBox.setItemText(3, _translate("mainWindow", "yolov5x.pt"))
        self.label_10.setText(_translate("mainWindow", "input"))
        self.fileButton.setToolTip(_translate("mainWindow", "file"))
        self.cameraButton.setToolTip(_translate("mainWindow", "camera"))
        self.rtspButton.setToolTip(_translate("mainWindow", "rtsp"))
        self.label_2.setText(_translate("mainWindow", "IoU"))
        self.label.setText(_translate("mainWindow", "conf"))
        self.label_8.setText(_translate("mainWindow", "speed"))
        self.checkBox.setText(_translate("mainWindow", "enable"))
        self.label_5.setText(_translate("mainWindow", "TextLabel"))
        self.label_11.setText(_translate("mainWindow", "预警结果"))
        self.saveCheckBox.setText(_translate("mainWindow", "Result Save"))
        self.SavedatabaseCheckBox.setText(_translate("mainWindow", "Detdta Save"))
        self.visualize_checkbox1.setText(_translate("mainWindow", "Visualize"))
        self.imageFilterButton.setText(_translate("mainWindow", "图像滤波"))
        self.imageFilterComboBox.setItemText(0, _translate("mainWindow", "均值滤波"))
        self.imageFilterComboBox.setItemText(1, _translate("mainWindow", "高斯滤波"))
        self.imageFilterComboBox.setItemText(2, _translate("mainWindow", "中值滤波"))
        self.previewFilterButton.setText(_translate("mainWindow", "预览"))
        self.morphologyButton.setText(_translate("mainWindow", "形态学处理"))
        self.morphologyComboBox.setItemText(0, _translate("mainWindow", "膨胀"))
        self.morphologyComboBox.setItemText(1, _translate("mainWindow", "腐蚀"))
        self.morphologyComboBox.setItemText(2, _translate("mainWindow", "开运算"))
        self.morphologyComboBox.setItemText(3, _translate("mainWindow", "闭运算"))
        self.previewmorphologyButton.setText(_translate("mainWindow", "预览"))
        self.histogramButton.setText(_translate("mainWindow", "直方图处理"))
        self.histogramComboBox.setItemText(0, _translate("mainWindow", "直方图均衡化"))
        self.previewhistogramButton.setText(_translate("mainWindow", "预览"))
        self.imageEnhanceButton.setText(_translate("mainWindow", "图像增强"))
        self.imageEnhanceComboBox.setItemText(0, _translate("mainWindow", "对比度增强"))
        self.imageEnhanceComboBox.setItemText(1, _translate("mainWindow", "饱和度调整"))
        self.imageEnhanceComboBox.setItemText(2, _translate("mainWindow", "调整色相"))
        self.imageEnhanceComboBox.setItemText(3, _translate("mainWindow", "调整亮度"))
        self.imageEnhanceComboBox.setItemText(4, _translate("mainWindow", "Gamma 校正"))
        self.imageEnhanceComboBox.setItemText(5, _translate("mainWindow", "二值化"))
        self.imageEnhanceComboBox.setItemText(6, _translate("mainWindow", "亮度增强"))
        self.imageEnhanceComboBox.setItemText(7, _translate("mainWindow", "锐化"))
        self.imageEnhanceComboBox.setItemText(8, _translate("mainWindow", "平滑"))
        self.imageEnhanceComboBox.setItemText(9, _translate("mainWindow", "水平翻转"))
        self.imageEnhanceComboBox.setItemText(10, _translate("mainWindow", "垂直翻转"))
        self.imageEnhanceComboBox.setItemText(11, _translate("mainWindow", "水平垂直翻转"))
        self.apply_custom_adjustments_imageEnhance.setText(_translate("mainWindow", "自定义"))
        self.previewEnhanceButton.setText(_translate("mainWindow", "预览"))
        self.loadImageButton.setText(_translate("mainWindow", "加载图像"))
        self.openFolderButton.setText(_translate("mainWindow", "打开文件夹"))
        self.saveFolderButton.setText(_translate("mainWindow", "选择路径"))
        self.saveButton.setText(_translate("mainWindow", "保存"))
        self.scaleSlider.setToolTip(_translate("mainWindow", "<html><head/><body><p>scaleSlider</p></body></html>"))
        self.previousImageButton.setText(_translate("mainWindow", "上一个"))
        self.nextImageButton.setText(_translate("mainWindow", "下一个"))
        self.enhanceMethod1Checkbox.setText(_translate("mainWindow", "Image flip"))
        self.enhanceMethod2Checkbox.setText(_translate("mainWindow", "Random Crop"))
        self.enhanceMethod3Checkbox.setText(_translate("mainWindow", "Random Resize"))
        self.enhanceMethod4Checkbox.setText(_translate("mainWindow", "Random Rotation"))
        self.enhanceMethod5Checkbox.setText(_translate("mainWindow", "Random BCSH"))
        self.enhanceMethod6Checkbox.setText(_translate("mainWindow", "Random Wipe"))
        self.enhanceMethod7Checkbox.setText(_translate("mainWindow", "Weighted Random Noise"))
        self.enhanceMethod8Checkbox.setText(_translate("mainWindow", "CutOut"))
        self.enhanceMethod9Checkbox.setText(_translate("mainWindow", "Mixup"))
        self.enhanceMethod10Checkbox.setText(_translate("mainWindow", "Mosaic"))
        self.helpButton.setToolTip(_translate("mainWindow", "<html><head/><body><p>查看参数详情</p></body></html>"))
        self.advancedSettingsButton.setText(_translate("mainWindow", "高级参数设置"))
        self.enhanceProbabilityInput.setToolTip(_translate("mainWindow", "<html><head/><body><p>请输入增强概率</p></body></html>"))
        self.enhanceProbabilityInput.setText(_translate("mainWindow", "0.5"))
        self.label_18.setText(_translate("mainWindow", "图像增强概率"))
        self.inputFolderButton.setText(_translate("mainWindow", "输入文件夹"))
        self.outputFolderButton.setText(_translate("mainWindow", "输出文件夹"))
        self.startProcessingButton.setText(_translate("mainWindow", "开始批处理"))
        self.hide_labelscheckbox_5.setText(_translate("mainWindow", "Show results"))
        self.save_cropcheckbox_2.setText(_translate("mainWindow", "Save Cropped Images"))
        self.agnostic_nmscheckbox_2.setText(_translate("mainWindow", "The file is created automatically"))
        self.halfcheckbox_2.setText(_translate("mainWindow", "Enable Half Precision Inference"))
        self.agnostic_nmscheckbox.setText(_translate("mainWindow", "Apply Class-Agnostic NMS"))
        self.augmentedcheckbox_3.setText(_translate("mainWindow", "Use parameter enhancement"))
        self.hide_labelscheckbox_4.setText(_translate("mainWindow", "Hidden tag"))
        self.hide_confscheckbox_6.setText(_translate("mainWindow", "Hidden conf"))
        self.label_16.setText(_translate("mainWindow", "Device Choose"))
        self.comboBox_2.setItemText(0, _translate("mainWindow", "0"))
        self.comboBox_2.setItemText(1, _translate("mainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("mainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("mainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("mainWindow", "cpu"))
        self.label_12.setText(_translate("mainWindow", "Input image size"))
        self.label_14.setText(_translate("mainWindow", "Bounding box thickness"))
        self.label_15.setText(_translate("mainWindow", "Maximum detections per image"))
        self.label_13.setText(_translate("mainWindow", "Category filtering"))
        self.browse_result_folder_button.setText(_translate("mainWindow", "Select Result Folder"))

from MouseLabel import Label_click_Mouse
import apprcc_rc
