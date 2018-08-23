from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 725)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/16x16.png', QtCore.QSize(16, 16))
        app_icon.addFile('icons/24x24.png', QtCore.QSize(24, 24))
        app_icon.addFile('icons/32x32.png', QtCore.QSize(32, 32))
        app_icon.addFile('icons/48x48.png', QtCore.QSize(48, 48))
        app_icon.addFile('icons/256x256.png', QtCore.QSize(256, 256))
        MainWindow.setWindowIcon(app_icon)

        # Parsing Variables
        self.sList = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        self.dfSoup = pd.DataFrame(self.sList, columns=['boolList'])
        self.dfSoup["soupObjectList"] = ""
        self.data = []
        self.nbCol = 1
        self.dfTab = pd.DataFrame(self.sList, columns=['boolList'])
        self.dfTab["headerList"] = ""
        self.dfHeaders = pd.DataFrame()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.AddressBar = QtWidgets.QLineEdit(self.centralwidget)
        self.AddressBar.setObjectName("AddressBar")
        # To address bar function
        self.AddressBar.returnPressed.connect(lambda: self.webViewAndParse(self.WebButt, self.AddressBar))
        # Tab 1
        self.gridLayout.addWidget(self.AddressBar, 0, 1, 1, 2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # WebView
        self.WebButt = QtWebEngineWidgets.QWebEngineView(self.tab_1)
        self.WebButt.setObjectName("WebButt")
        self.horizontalLayout.addWidget(self.WebButt)
        # To changed url function
        self.WebButt.urlChanged.connect(lambda: self.parse(self.WebButt.url().toString()))

        self.tabWidget.addTab(self.tab_1, "")

        # Tab 2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("""
        .QTextBrowser {
            selection-background-color: lightgreen;
            }
        """)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.textCursor = self.textBrowser.textCursor()
        self.tabWidget.addTab(self.tab_2, "")

        # Tab 3
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.DBTitle = QtWidgets.QLineEdit(self.tab_3)
        self.DBTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.DBTitle.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.DBTitle)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.delCol = QtWidgets.QPushButton(self.tab_3)
        self.delCol.setObjectName("pushButton_9")
        self.horizontalLayout_11.addWidget(self.delCol)

        self.delCol.clicked.connect(self.removeColumn)

        self.clearDB = QtWidgets.QPushButton(self.tab_3)
        self.clearDB.setObjectName("pushButton_7")
        self.horizontalLayout_11.addWidget(self.clearDB)

        self.clearDB.clicked.connect(self.clearingDB)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.line_ex = QtWidgets.QFrame(self.tab_3)
        self.line_ex.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_ex.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_ex.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line_ex)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButtonCSV = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonCSV.setObjectName("radioButton")
        self.horizontalLayout_9.addWidget(self.radioButtonCSV)
        self.radioButtonJSON = QtWidgets.QRadioButton(self.tab_3)
        self.radioButtonJSON.setObjectName("radioButton_2")
        self.horizontalLayout_9.addWidget(self.radioButtonJSON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.exportDB = QtWidgets.QPushButton(self.tab_3)
        self.exportDB.setObjectName("pushButton_6")
        self.horizontalLayout_13.addWidget(self.exportDB)

        self.exportDB.clicked.connect(self.toPandas)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logoSpider = QtWidgets.QLabel(self.frame)
        self.logoSpider.setPixmap(QtGui.QPixmap('sg-logo.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoSpider.sizePolicy().hasHeightForWidth())
        self.logoSpider.setSizePolicy(sizePolicy)
        self.logoSpider.setMinimumSize(QtCore.QSize(75, 75))
        self.logoSpider.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.logoSpider)
        self.ScrapGodL = QtWidgets.QLabel(self.frame)
        self.ScrapGodL.setPixmap(QtGui.QPixmap('sg-txt.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrapGodL.sizePolicy().hasHeightForWidth())
        self.ScrapGodL.setSizePolicy(sizePolicy)
        self.ScrapGodL.setMinimumSize(QtCore.QSize(150, 75))
        self.ScrapGodL.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.ScrapGodL)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # DIV ATTRS

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.divButt1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divButt1.sizePolicy().hasHeightForWidth())
        self.divButt1.setSizePolicy(sizePolicy)
        self.divButt1.setMaximumSize(QtCore.QSize(50, 50))
        self.divButt1.setObjectName("divButt1")
        self.gridLayout_2.addWidget(self.divButt1, 0, 1, 2, 1)
        self.divLine1 = QtWidgets.QLineEdit(self.frame)
        self.divLine1.setMinimumSize(QtCore.QSize(215, 0))
        self.divLine1.setObjectName("divLine1")
        self.gridLayout_2.addWidget(self.divLine1, 1, 0, 1, 1)
        self.divLab1 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divLab1.sizePolicy().hasHeightForWidth())
        self.divLab1.setSizePolicy(sizePolicy)
        self.divLab1.setMinimumSize(QtCore.QSize(215, 15))
        self.divLab1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.divLab1.setAlignment(QtCore.Qt.AlignCenter)
        self.divLab1.setObjectName("divLab1")
        self.gridLayout_2.addWidget(self.divLab1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.divLine1.textChanged.connect(lambda: self.divScraping(self.divLine1, 1))

        self.divButt1.clicked.connect(lambda: self.delLine(1))

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.atButt1 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atButt1.sizePolicy().hasHeightForWidth())
        self.atButt1.setSizePolicy(sizePolicy)
        self.atButt1.setMaximumSize(QtCore.QSize(50, 50))
        self.atButt1.setObjectName("atButt1")
        self.gridLayout_3.addWidget(self.atButt1, 0, 1, 2, 1)
        self.atLine1 = QtWidgets.QLineEdit(self.frame)
        self.atLine1.setMinimumSize(QtCore.QSize(215, 0))
        self.atLine1.setObjectName("atLine1")

        self.atLine1.textChanged.connect(lambda: self.attrsScraping(self.atLine1, 2))

        self.atButt1.clicked.connect(lambda: self.delLine(2))

        self.gridLayout_3.addWidget(self.atLine1, 1, 0, 1, 1)
        self.atLab1 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atLab1.sizePolicy().hasHeightForWidth())
        self.atLab1.setSizePolicy(sizePolicy)
        self.atLab1.setMinimumSize(QtCore.QSize(215, 15))
        self.atLab1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.atLab1.setAlignment(QtCore.Qt.AlignCenter)
        self.atLab1.setObjectName("atLab1")
        self.gridLayout_3.addWidget(self.atLab1, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        # ADDING SPACE ____________________________________________________________
        self.addVar = 0

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QtCore.QSize(10, 40))
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_8.addWidget(self.pushButton_10)

        self.pushButton_10.clicked.connect(self.substract)

        # 'Add' Button
        self.adder = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adder.sizePolicy().hasHeightForWidth())
        self.adder.setSizePolicy(sizePolicy)
        self.adder.setMinimumSize(QtCore.QSize(10, 40))
        self.adder.setMaximumSize(QtCore.QSize(40, 16777215))
        self.adder.setObjectName("pushButton_5")

        self.adder.clicked.connect(self.adding)

        self.horizontalLayout_8.addWidget(self.adder)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.elements = QtWidgets.QSpinBox(self.frame)
        self.elements.setMaximumSize(QtCore.QSize(40, 16777215))
        self.elements.setObjectName("spinBox")
        self.horizontalLayout_5.addWidget(self.elements)

        self.elements.valueChanged.connect(lambda: self.elementsGetting(self.elements, 7))

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.checkTBox = QtWidgets.QCheckBox(self.frame)
        self.checkTBox.setObjectName("checkBox")
        self.horizontalLayout_5.addWidget(self.checkTBox)

        self.checkTBox.stateChanged.connect(lambda: self.textChecked(self.checkTBox, 8))

        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.fromSlider = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromSlider.sizePolicy().hasHeightForWidth())
        self.fromSlider.setSizePolicy(sizePolicy)
        self.fromSlider.setMinimumSize(QtCore.QSize(225, 0))
        self.fromSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fromSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_6.addWidget(self.fromSlider)
        self.fromSlider.setMinimum(-99)
        self.fromSlider.setMaximum(99)
        self.fromSlider.setValue(0)

        self.fromSlider.valueChanged.connect(lambda: self.charactersFromTo(self.fromSlider, self.toSlider, 9))

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(24, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.toSlider = QtWidgets.QSlider(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toSlider.sizePolicy().hasHeightForWidth())
        self.toSlider.setSizePolicy(sizePolicy)
        self.toSlider.setMinimumSize(QtCore.QSize(225, 0))
        self.toSlider.setOrientation(QtCore.Qt.Horizontal)
        self.toSlider.setObjectName("horizontalSlider_2")
        self.horizontalLayout_7.addWidget(self.toSlider)
        self.toSlider.setMinimum(-99)
        self.toSlider.setMaximum(99)
        self.toSlider.setValue(-1)

        self.toSlider.valueChanged.connect(lambda: self.charactersFromTo(self.fromSlider, self.toSlider, 9))

        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.searchEdit = QtWidgets.QLineEdit(self.frame)
        self.searchEdit.setObjectName("lineEdit_7")
        self.findButt = QtWidgets.QPushButton(self.frame)
        self.findButt.setObjectName("pushButton_11")

        self.searchEdit.returnPressed.connect(self.findingStuff)
        self.findButt.clicked.connect(self.findingStuff)

        self.horizontalLayout_10.addWidget(self.searchEdit)
        self.horizontalLayout_10.addWidget(self.findButt)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addStretch()
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addColLine = QtWidgets.QLineEdit(self.frame)
        self.addColLine.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.addColLine)
        self.addCol = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addCol.sizePolicy().hasHeightForWidth())
        self.addCol.setSizePolicy(sizePolicy)
        self.addCol.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.addCol)

        self.addCol.clicked.connect(self.addingColumn)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.clearAll = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearAll.sizePolicy().hasHeightForWidth())
        self.clearAll.setSizePolicy(sizePolicy)
        self.clearAll.setMaximumSize(QtCore.QSize(16777215, 52))
        self.clearAll.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.clearAll)

        self.clearAll.clicked.connect(self.clearing)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.gridLayout.addWidget(self.frame, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setCurrentIndex(1)

    def webViewAndParse(self, viewer, line):
        self.dfSoup.boolList = False
        if line.text().isspace() is False:
            if ('https' or 'www') in line.text():
                newAddy = line.text()
                viewer.setUrl(QtCore.QUrl(newAddy))
            else:
                newAddy = 'https://www.' + line.text()
                viewer.setUrl(QtCore.QUrl(newAddy))

            try:
                r = requests.get(newAddy)
                self.dfSoup.soupObjectList[0] = BeautifulSoup(r.text, 'html.parser')
                self.dfSoup.boolList = False
                self.dfSoup.boolList[0] = True
                self.divLine1.clear()
                self.atLine1.clear()
                if self.addVar == 1:
                    self.divLine2.clear()
                    self.atLine2.clear()
                elif self.addVar == 2:
                    self.divLine2.clear()
                    self.atLine2.clear()
                    self.divLine3.clear()
                    self.atLine3.clear()
                self.elements.clear()
                self.checkTBox.setCheckState(0)
                self.fromSlider.setValue(0)
                self.toSlider.setValue(-1)
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.textBrowser.setPlainText(str(self.dfSoup.soupObjectList[0]))
            except requests.exceptions.RequestException as e:
                print(e)

    def parse(self, url):
        self.dfSoup.boolList = False
        if ('http' or 'www') in str(url):
            newAddy = str(url)
        else:
            newAddy = 'https://www.' + str(url)
        try:
            r = requests.get(newAddy)
            self.dfSoup.soupObjectList[0] = BeautifulSoup(r.text, 'html.parser')
            self.dfSoup.boolList = False
            self.dfSoup.boolList[0] = True
            self.divLine1.clear()
            self.atLine1.clear()
            if self.addVar == 1:
                self.divLine2.clear()
                self.atLine2.clear()
            elif self.addVar == 2:
                self.divLine2.clear()
                self.atLine2.clear()
                self.divLine3.clear()
                self.atLine3.clear()
            self.elements.clear()
            self.checkTBox.setCheckState(0)
            self.fromSlider.setValue(0)
            self.toSlider.setValue(-1)
            self.lineEdit_5.clear()
            self.lineEdit_6.clear()
            self.textBrowser.clear()
            self.textBrowser.setPlainText(str(self.dfSoup.soupObjectList[0]))
        except requests.exceptions.RequestException as e:
            print(e)

    def divScraping(self, div, nb):
        self.dfSoup.boolList[nb] = False
        nbVar = nb
        while not self.dfSoup.boolList[nb]:
            nb -= 1
            if nb == -1:
                break
        if nb != -1:
            newSoup = ''
            self.data = []
            for result in self.dfSoup.soupObjectList[nb].find_all(div.text()):
                newSoup = newSoup + str(result)
                self.data.append(str(result))
            if newSoup == '':
                self.textBrowser.setPlainText(str(self.dfSoup.soupObjectList[nb]))
                self.dfSoup.boolList[7] = False
            else:
                self.elements.clear()
                self.checkTBox.setCheckState(0)
                self.fromSlider.setValue(0)
                self.toSlider.setValue(-1)
                self.lineEdit_5.clear()
                self.lineEdit_6.clear()
                self.textBrowser.clear()
                self.textBrowser.setPlainText(newSoup)
                self.dfSoup.soupObjectList[nbVar] = BeautifulSoup(newSoup, 'html.parser')
                self.dfSoup.boolList[nbVar] = True
                self.mostRecentSoup = self.dfSoup.soupObjectList[nb].find_all(div.text())

    def attrsScraping(self, attrs, nb):
        self.dfSoup.boolList[nb] = False
        nbVar = nb
        while not self.dfSoup.boolList[nb]:
            nb -= 1
            if nb == -1:
                break
        if nb != -1:
            transfo = attrs.text()
            if '=' in transfo:
                transfo = transfo.split('=')
                transfo1 = transfo[0]
                transfo2 = transfo[1].replace('"', '')
                self.data = []
                newSoup = ''
                for result in self.dfSoup.soupObjectList[nb].find_all(attrs={transfo1: transfo2}):
                    newSoup = newSoup + str(result)
                    self.data.append(str(result))
                if newSoup == '':
                    self.textBrowser.setPlainText(str(self.dfSoup.soupObjectList[nb]))
                    self.dfSoup.boolList[7] = False
                else:
                    self.elements.clear()
                    self.dfSoup.boolList[7:] = False
                    self.checkTBox.setCheckState(0)
                    self.fromSlider.setValue(0)
                    self.toSlider.setValue(-1)
                    self.lineEdit_5.clear()
                    self.lineEdit_6.clear()
                    self.textBrowser.clear()
                    self.textBrowser.setPlainText(newSoup)
                    self.dfSoup.soupObjectList[nbVar] = BeautifulSoup(newSoup, 'html.parser')
                    self.dfSoup.boolList[nbVar] = True
                    self.mostRecentSoup = self.dfSoup.soupObjectList[nb].find_all(attrs={transfo1: transfo2})
            else:
                self.textBrowser.setPlainText(str(self.dfSoup.soupObjectList[nb]))

    def findingStuff(self):
        if self.textBrowser.find(self.searchEdit.text()):
            self.textBrowser.find(self.searchEdit.text())
        else:
            self.textBrowser.selectAll()
            self.textBrowser.moveCursor(QtGui.QTextCursor.Start)
            self.textBrowser.find(self.searchEdit.text())

    def elementsGetting(self, nbele, nb):
        self.dfSoup.boolList[nb] = False
        nbVar = nb
        while not self.dfSoup.boolList[nb]:
            nb -= 1
            if nb == -1:
                break
        if nb > 0:
            if nbele.value() < len(self.mostRecentSoup):
                if self.checkTBox.isChecked():
                    newSoup = str(self.mostRecentSoup[nbele.value()].text[self.fromSlider.value():])
                else:
                    newSoup = str(self.mostRecentSoup[nbele.value()])
                if newSoup == '':
                    self.textBrowser.setPlainText(str(newSoup))
                    self.dfSoup.boolList[nbVar] = True
                else:
                    self.data = []
                    self.data.append(newSoup)
                    self.textBrowser.clear()
                    self.textBrowser.setPlainText(newSoup)
                    self.dfSoup.boolList[nbVar] = True

    def textChecked(self, state, nb):
        self.dfSoup.boolList[nb] = False
        nbVar = nb
        while not self.dfSoup.boolList[nb]:
            nb -= 1
            if nb == -1:
                break
        if nb > 0:
            if state.isChecked():
                newSoup = ''
                self.data = []
                if self.dfSoup.boolList[7]:
                    newSoup = newSoup + str(self.mostRecentSoup[self.elements.value()].text[self.fromSlider.value():self.toSlider.value()])
                    self.data.append(newSoup)
                else:
                    for result in self.mostRecentSoup:
                        newSoup = newSoup + str(result.text)
                        self.data.append(str(result.text))
                if newSoup == '':
                    self.textBrowser.setPlainText(str(newSoup))
                else:
                    self.textBrowser.clear()
                    self.textBrowser.setPlainText(newSoup)
                    self.dfSoup.boolList[nbVar] = True
            else:
                self.data = []
                newSoup = ''
                if self.dfSoup.boolList[7]:
                    newSoup = newSoup + str(self.mostRecentSoup[self.elements.value()])
                    self.data.append(newSoup)
                else:
                    newSoup = newSoup + str(self.mostRecentSoup)
                    self.data.append(newSoup)
                if newSoup == '':
                    self.textBrowser.setPlainText(str(self.mostRecentSoup[self.elements.value()]))
                else:
                    self.textBrowser.clear()
                    self.textBrowser.setPlainText(newSoup)

    def charactersFromTo(self, slideF, slideT, nb):
        self.dfSoup.boolList[nb] = False
        self.lineEdit_5.setText(str(slideF.value()))
        self.lineEdit_6.setText(str(slideT.value()))
        nb = nb - 2
        newSoup = ''
        while not self.dfSoup.boolList[nb]:
            nb -= 1
            if nb == -1:
                break
        if nb > 0:
            if self.checkTBox.isChecked():
                self.data = []
                if self.dfSoup.boolList[7]:
                    newSoup = newSoup + str(self.mostRecentSoup[self.elements.value()].text[self.fromSlider.value():self.toSlider.value()])
                    self.data.append(newSoup)
                else:
                    for result in self.mostRecentSoup:
                        newSoup = newSoup + str(result.text[self.fromSlider.value():self.toSlider.value()])
                        self.data.append(str(result.text[self.fromSlider.value():self.toSlider.value()]))
                if newSoup == '':
                    self.textBrowser.setPlainText(str(newSoup))
                else:
                    self.textBrowser.clear()
                    self.textBrowser.setPlainText(newSoup)

    def delLine(self, nb):
        if nb == 1:
            self.divLine1.clear()
        elif nb == 2:
            self.atLine1.clear()
        elif nb == 3:
            self.divLine2.clear()
        elif nb == 4:
            self.atLine2.clear()
        elif nb == 5:
            self.divLine3.clear()
        elif nb == 6:
            self.atLine3.clear()

    def clearing(self):
        self.dfSoup.boolList[1:] = False
        self.divLine1.clear()
        self.atLine1.clear()
        if self.addVar == 1:
            self.divLine2.clear()
            self.atLine2.clear()
        if self.addVar == 2:
            self.divLine2.clear()
            self.atLine2.clear()
            self.divLine3.clear()
            self.atLine3.clear()
        self.elements.clear()
        self.dfSoup.boolList[7:] = False
        self.checkTBox.setCheckState(0)
        self.fromSlider.setValue(0)
        self.toSlider.setValue(-1)
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.addColLine.clear()

    def clearingDB(self):
        self.tableWidget.clear()
        self.dfTab.boolList = False
        self.DBTitle.setText('Dataset Title')

    def toPandas(self):
        dfTemp = pd.DataFrame()
        for col in range(self.tableWidget.columnCount()):
            listTemp = []
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, col)
                if item is not None:
                    listTemp.append(item.text())
                else:
                    listTemp.append('')
            column_values = pd.Series(listTemp)
            dfTemp.insert(loc=col, column=list(self.dfHeaders)[col], value=column_values, allow_duplicates=True)
        if self.radioButtonCSV.isChecked():
            if self.DBTitle.text() == "":
                dfTemp.to_csv("Untilted Dataset.csv")
            else:
                dfTemp.to_csv(self.DBTitle.text() + ".csv")
        elif self.radioButtonJSON.isChecked():
            if self.DBTitle.text() == "":
                dfTemp.to_json("Untilted Dataset.json")
            else:
                dfTemp.to_json(self.DBTitle.text() + ".json")

    def addingColumn(self):
        nbRow = 0
        nbCol = self.tableWidget.columnCount()
        cstRow = self.tableWidget.rowCount()
        self.dfHeaders[self.addColLine.text()] = "nun"
        self.nbCol += 1

        while self.tableWidget.columnCount() < len(list(self.dfHeaders)):
            self.tableWidget.insertColumn(nbCol)
        self.tableWidget.setHorizontalHeaderLabels(list(self.dfHeaders))

        if len(self.data) > cstRow:
            addThisMuch = len(self.data) - cstRow
            while addThisMuch > 0:
                self.tableWidget.insertRow(cstRow)
                addThisMuch -= 1

        for bigIt in self.data:
            res = QtWidgets.QTableWidgetItem(bigIt)
            self.tableWidget.setCurrentCell(nbRow, nbCol)
            self.tableWidget.setItem(nbRow, nbCol, res)
            nbRow += 1

        self.dfHeaders[self.addColLine.text()] = [len(self.data)]

    def removeColumn(self):
        if self.tableWidget.columnCount() > 0:
            var = 0
            nb = self.tableWidget.currentColumn()
            self.tableWidget.removeColumn(nb)
            hName = list(self.dfHeaders)[nb]
            del self.dfHeaders[hName]
            for i in range(len(list(self.dfHeaders))):
                if var < self.dfHeaders.iloc[0, i]:
                    var = self.dfHeaders.iloc[0, i]
            self.tableWidget.setRowCount(var)

    def adding(self):
        if self.addVar == 0:

            self.gridLayout_4 = QtWidgets.QGridLayout()
            self.gridLayout_4.setObjectName("gridLayout_4")
            self.divButt2 = QtWidgets.QPushButton(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.divButt2.sizePolicy().hasHeightForWidth())
            self.divButt2.setSizePolicy(sizePolicy)
            self.divButt2.setMaximumSize(QtCore.QSize(50, 50))
            self.divButt2.setObjectName("divButt2")
            self.gridLayout_4.addWidget(self.divButt2, 0, 1, 2, 1)
            self.divLine2 = QtWidgets.QLineEdit(self.frame)
            self.divLine2.setMinimumSize(QtCore.QSize(215, 0))
            self.divLine2.setObjectName("divLine2")
            self.gridLayout_4.addWidget(self.divLine2, 1, 0, 1, 1)
            self.divLab2 = QtWidgets.QLabel(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.divLab2.sizePolicy().hasHeightForWidth())
            self.divLab2.setSizePolicy(sizePolicy)
            self.divLab2.setMinimumSize(QtCore.QSize(215, 15))
            self.divLab2.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.divLab2.setAlignment(QtCore.Qt.AlignCenter)
            self.divLab2.setObjectName("divLab2")
            self.gridLayout_4.addWidget(self.divLab2, 0, 0, 1, 1)
            self.verticalLayout.insertLayout(3, self.gridLayout_4)

            self.divLine2.textChanged.connect(lambda: self.divScraping(self.divLine2, 3))

            self.divButt2.clicked.connect(lambda: self.delLine(3))

            self.gridLayout_5 = QtWidgets.QGridLayout()
            self.gridLayout_5.setObjectName("gridLayout_5")
            self.atButt2 = QtWidgets.QPushButton(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.atButt2.sizePolicy().hasHeightForWidth())
            self.atButt2.setSizePolicy(sizePolicy)
            self.atButt2.setMaximumSize(QtCore.QSize(50, 50))
            self.atButt2.setObjectName("atButt1")
            self.gridLayout_5.addWidget(self.atButt2, 0, 1, 2, 1)
            self.atLine2 = QtWidgets.QLineEdit(self.frame)
            self.atLine2.setMinimumSize(QtCore.QSize(215, 0))
            self.atLine2.setObjectName("atLine2")
            self.gridLayout_5.addWidget(self.atLine2, 1, 0, 1, 1)
            self.atLab2 = QtWidgets.QLabel(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.atLab2.sizePolicy().hasHeightForWidth())
            self.atLab2.setSizePolicy(sizePolicy)
            self.atLab2.setMinimumSize(QtCore.QSize(215, 15))
            self.atLab2.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.atLab2.setAlignment(QtCore.Qt.AlignCenter)
            self.atLab2.setObjectName("atLab2")
            self.gridLayout_5.addWidget(self.atLab2, 0, 0, 1, 1)
            self.verticalLayout.insertLayout(4, self.gridLayout_5)

            self.atLine2.textChanged.connect(lambda: self.attrsScraping(self.atLine2, 4))

            self.atButt2.clicked.connect(lambda: self.delLine(4))

            self.retranslateUi(MainWindow)
            self.addVar += 1

        elif self.addVar == 1:
            self.gridLayout_6 = QtWidgets.QGridLayout()
            self.gridLayout_6.setObjectName("gridLayout_6")
            self.divButt3 = QtWidgets.QPushButton(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.divButt3.sizePolicy().hasHeightForWidth())
            self.divButt3.setSizePolicy(sizePolicy)
            self.divButt3.setMaximumSize(QtCore.QSize(50, 50))
            self.divButt3.setObjectName("divButt3")
            self.gridLayout_6.addWidget(self.divButt3, 0, 1, 2, 1)
            self.divLine3 = QtWidgets.QLineEdit(self.frame)
            self.divLine3.setMinimumSize(QtCore.QSize(215, 0))
            self.divLine3.setObjectName("divLine3")
            self.gridLayout_6.addWidget(self.divLine3, 1, 0, 1, 1)
            self.divLab3 = QtWidgets.QLabel(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.divLab3.sizePolicy().hasHeightForWidth())
            self.divLab3.setSizePolicy(sizePolicy)
            self.divLab3.setMinimumSize(QtCore.QSize(215, 15))
            self.divLab3.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.divLab3.setAlignment(QtCore.Qt.AlignCenter)
            self.divLab3.setObjectName("divLab3")
            self.gridLayout_6.addWidget(self.divLab3, 0, 0, 1, 1)
            self.verticalLayout.insertLayout(5, self.gridLayout_6)

            self.divLine3.textChanged.connect(lambda: self.divScraping(self.divLine3, 5))

            self.divButt3.clicked.connect(lambda: self.delLine(5))

            self.gridLayout_7 = QtWidgets.QGridLayout()
            self.gridLayout_7.setObjectName("gridLayout_7")
            self.atButt3 = QtWidgets.QPushButton(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.atButt3.sizePolicy().hasHeightForWidth())
            self.atButt3.setSizePolicy(sizePolicy)
            self.atButt3.setMaximumSize(QtCore.QSize(50, 50))
            self.atButt3.setObjectName("atButt1")
            self.gridLayout_7.addWidget(self.atButt3, 0, 1, 2, 1)
            self.atLine3 = QtWidgets.QLineEdit(self.frame)
            self.atLine3.setMinimumSize(QtCore.QSize(215, 0))
            self.atLine3.setObjectName("atLine3")
            self.gridLayout_7.addWidget(self.atLine3, 1, 0, 1, 1)
            self.atLab3 = QtWidgets.QLabel(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.atLab3.sizePolicy().hasHeightForWidth())
            self.atLab3.setSizePolicy(sizePolicy)
            self.atLab3.setMinimumSize(QtCore.QSize(215, 15))
            self.atLab3.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.atLab3.setAlignment(QtCore.Qt.AlignCenter)
            self.atLab3.setObjectName("atLab3")
            self.gridLayout_7.addWidget(self.atLab3, 0, 0, 1, 1)
            self.verticalLayout.insertLayout(6, self.gridLayout_7)

            self.atLine3.textChanged.connect(lambda: self.attrsScraping(self.atLine3, 6))

            self.atButt3.clicked.connect(lambda: self.delLine(6))

            self.retranslateUi(MainWindow)
            self.addVar += 1

    def substract(self):
        if self.addVar == 1:
            self.clearLayout(self.gridLayout_4)
            del self.gridLayout_4
            self.clearLayout(self.gridLayout_5)
            del self.gridLayout_5
            self.addVar -= 1
        elif self.addVar == 2:
            self.clearLayout(self.gridLayout_6)
            del self.gridLayout_6
            self.clearLayout(self.gridLayout_7)
            del self.gridLayout_7
            self.addVar -= 1

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScrapGod"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Web"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Scrape"))
        self.DBTitle.setText(_translate("MainWindow", "Dataset Title"))
        self.delCol.setText(_translate("MainWindow", "Remove Column"))
        self.clearDB.setText(_translate("MainWindow", "Clear Dataset"))
        self.radioButtonCSV.setText(_translate("MainWindow", "CSV"))
        self.radioButtonJSON.setText(_translate("MainWindow", "JSON"))
        self.exportDB.setText(_translate("MainWindow", "Export Dataset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Data"))
        self.divButt1.setText(_translate("MainWindow", "Cancel"))
        self.divLab1.setText(_translate("MainWindow", "Div"))
        self.atButt1.setText(_translate("MainWindow", "Cancel"))
        self.atLab1.setText(_translate("MainWindow", "Attrs"))
        try:
            self.divButt2.setText(_translate("MainWindow", "Cancel"))
            self.divLab2.setText(_translate("MainWindow", "2 - Div"))
            self.atButt2.setText(_translate("MainWindow", "Cancel"))
            self.atLab2.setText(_translate("MainWindow", "2 - Attrs"))
            self.divButt3.setText(_translate("MainWindow", "Cancel"))
            self.divLab3.setText(_translate("MainWindow", "3 - Div"))
            self.atButt3.setText(_translate("MainWindow", "Cancel"))
            self.atLab3.setText(_translate("MainWindow", "3 - Attrs"))
        except Exception:
            pass
        self.pushButton_10.setText(_translate("MainWindow", "Less"))
        self.adder.setText(_translate("MainWindow", "More"))
        self.label_6.setText(_translate("MainWindow", "Element"))
        self.checkTBox.setText(_translate("MainWindow", "Text"))
        self.label_7.setText(_translate("MainWindow", "From"))
        self.label_8.setText(_translate("MainWindow", "To"))
        self.findButt.setText(_translate("MainWindow", "Find"))
        self.addCol.setText(_translate("MainWindow", "Add Column"))
        self.clearAll.setText(_translate("MainWindow", "Clear All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
