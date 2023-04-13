if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

    # 排序之后又没有显示检测时间，检测时间和那个标志数量好像反过来了
    #数据分析有些字符不太显示这个数据，要进行一些预祝
    #数据表是按照某一时间，某一类别，也就是类别，不会重合到一起
    #给等待时间比较长的添加转圈圈效果



