# Copyright 2014 - Samuel de Sousa (felixjr.org)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Booklet(object):
    def setupUi(self, Booklet):
        Booklet.setObjectName(_fromUtf8("Booklet"))
        Booklet.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../booklet.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Booklet.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Booklet)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(True)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        Booklet.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Booklet)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Booklet.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Booklet)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Booklet.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(Booklet)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Booklet.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(Booklet)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(Booklet)
        self.actionSave.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionPrint = QtGui.QAction(Booklet)
        self.actionPrint.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-print"))
        self.actionPrint.setIcon(icon)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionExit = QtGui.QAction(Booklet)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("application-exit"))
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(Booklet)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionNext = QtGui.QAction(Booklet)
        self.actionNext.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-next"))
        self.actionNext.setIcon(icon)
        self.actionNext.setObjectName(_fromUtf8("actionNext"))
        self.actionPrevious = QtGui.QAction(Booklet)
        self.actionPrevious.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-previous"))
        self.actionPrevious.setIcon(icon)
        self.actionPrevious.setObjectName(_fromUtf8("actionPrevious"))
        self.actionFirst = QtGui.QAction(Booklet)
        self.actionFirst.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-first"))
        self.actionFirst.setIcon(icon)
        self.actionFirst.setObjectName(_fromUtf8("actionFirst"))
        self.actionLast = QtGui.QAction(Booklet)
        self.actionLast.setEnabled(False)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("go-last"))
        self.actionLast.setIcon(icon)
        self.actionLast.setObjectName(_fromUtf8("actionLast"))
        self.actionPageNumber = QtGui.QLineEdit(Booklet)
        self.actionPageNumber.setEnabled(False)
        self.actionPageNumber.setReadOnly(True)
        self.actionPageNumber.setObjectName(_fromUtf8("actionPageNumber"))
        self.actionPageNumber.setMaximumWidth(35)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFirst)
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addWidget(self.actionPageNumber)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addAction(self.actionLast)

        self.retranslateUi(Booklet)
        QtCore.QMetaObject.connectSlotsByName(Booklet)

    def retranslateUi(self, Booklet):
        Booklet.setWindowTitle(_translate("Booklet", "Booklet", None))
        self.menuFile.setTitle(_translate("Booklet", "File", None))
        self.menuHelp.setTitle(_translate("Booklet", "Help", None))
        self.toolBar.setWindowTitle(_translate("Booklet", "toolBar", None))
        self.actionOpen.setText(_translate("Booklet", "Open", None))
        self.actionOpen.setShortcut(_translate("Booklet", "Ctrl+O", None))
        self.actionSave.setText(_translate("Booklet", "Save", None))
        self.actionSave.setShortcut(_translate("Booklet", "Ctrl+S", None))
        self.actionPrint.setText(_translate("Booklet", "Print", None))
        self.actionPrint.setShortcut(_translate("Booklet", "Ctrl+P", None))
        self.actionExit.setText(_translate("Booklet", "Exit", None))
        self.actionExit.setShortcut(_translate("Booklet", "Ctrl+Q", None))
        self.actionAbout.setText(_translate("Booklet", "About", None))
        self.actionNext.setText(_translate("Booklet", "Next", None))
        self.actionPrevious.setText(_translate("Booklet", "Previous", None))
        self.actionFirst.setText(_translate("Booklet", "First", None))
        self.actionLast.setText(_translate("Booklet", "Last", None))
        self.actionPageNumber.setText(_translate("Booklet", "0", None))

