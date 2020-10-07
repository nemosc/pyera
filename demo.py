#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

This program creates a menubar. The
menubar has one menu with an exit action.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTextBrowser,QScrollArea,QFrame,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPalette,QColor
import os


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.run()

    def run(self):
        pass
    def initUI(self):
        file_menu_actions = []
        help_menu_actions = []

        actions = []
        action = QAction('重新启动(&R)', self)
        actions.append(action)
        action = QAction('重新启动(调试)(&D)', self)
        actions.append(action)
        file_menu_actions.append(actions)

        actions = []
        action = QAction('保存日志(&S)...', self)
        action.setShortcut('Ctrl+S')
        actions.append(action)
        action = QAction('打开剪贴板窗口(&C)', self)
        action.setShortcut('Ctrl+C')
        actions.append(action)
        file_menu_actions.append(actions)

        actions = []
        action = QAction('返回标题画面(&T)', self)
        action.setShortcut('Ctrl+T')
        actions.append(action)
        action = QAction('全代码重读(&C)', self)
        actions.append(action)
        action = QAction('文件夹重读(&F)', self)
        actions.append(action)
        action = QAction('文件重读(&A)', self)
        actions.append(action)
        file_menu_actions.append(actions)

        actions = []
        action = QAction('退出(&X)', self)
        action.triggered.connect(qApp.quit)
        actions.append(action)
        file_menu_actions.append(actions)

        help_menu_actions.append([QAction('设置(&C)', self)])

        palette = QPalette()
        palette.setColor(self.backgroundRole(),QColor(0, 0, 0))


        text_browser = QTextBrowser(self)
        text_browser.setGeometry(0,20,1280,700)

        #text_browser.setTextColor(QColor(255,255,255))
        #text_browser.setTextBackgroundColor(QColor(0, 0, 0))
        text_browser.setStyleSheet('QTextBrowser::item:hover{color: white;} QTextBrowser {background-color: black;selection-background-color: black;color: rgb(255,128,64);selection-color: rgb(255,128,64);    font-family:"宋体";font-size:16px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;border: none;}')
        #text_browser.setPalette(palette)
        text = '''
------------------------------------------------------------------------------------------------------------------

※これはの改変・再配布です。
------------------------------------------------------------------------------------------------------------------
[0] 新的开始
[1] 载入存档
'''
        text_browser.append(text)
        text_browser.append('''
        <table width="100%">
            <tr>
                <td style="text-align: center;">Here is some text.</td>
            </tr>
            <tr>
                <td style="text-align: center;"><img height="256" src="resource/test.jpg"/></td>
            </tr>
        </table>
        ''')
        #for i in range(10):
        #    text_browser.append(text)
        #text_browser.append('123\n123\n123\n'*20)
        #text_browser.append('123' * 100)
        #text_browser.setFont(QFont('宋体',16))
        text_browser.setFrameShape(QFrame.NoFrame)
        line_edit = QLineEdit(text_browser)
        line_edit.setGeometry(0, 680, 1264, 20)
        line_edit.setStyleSheet('QLineEdit {background-color: black; black;color: rgb(255,128,64);  font-family:"宋体";font-size:16px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;border: none;}')
        #line_edit.set
        print(text_browser.frameShape())
        print(text_browser.lineWidth())


        # 创建一个菜单栏
        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("QMenuBar {background-color: rgb(240, 240, 240);}")
        # 添加菜单
        file_menu = menu_bar.addMenu('文件(&F)')
        help_menu = menu_bar.addMenu('帮助(&H)')

        # 添加事件
        for i in range(len(file_menu_actions)):
            file_menu.addActions(file_menu_actions[i])
            if i != len(file_menu_actions)-1:
                file_menu.addSeparator()
        for i in range(len(help_menu_actions)):
            help_menu.addActions(help_menu_actions[i])
            if i != len(help_menu_actions)-1:
                help_menu.addSeparator()

        self.setGeometry(300, 100, 1280, 720)
        self.setWindowTitle('pyera')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())