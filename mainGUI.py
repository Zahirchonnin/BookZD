# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class BookDZGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setStyleSheet("""#main {
	background-color: #986f43
}

#titleBar {
	border-bottom: 3px solid white;
	border-radius: 5px;
	background-color:  #d3b291
}
#logo {
	background-color: transparent;
}

#close, #minimize, #maximize, #paypal, #facebook {
	background-color: rgba(255, 255, 255, 100);
	border: 4px solid black;
	border-radius: 5px;
	border-top: 0; border-left: 0;
}

#close {
	color: red;
}

#minimize {
	color: green;
}
#minimize::pressed, #close::pressed, #provider::pressed, #maximize::pressed, #paypal::pressed, #facebook::pressed {
	background-color: rgba(0, 0, 0, 30);
	border: 4px solid black;
	border-bottom: 0;
	border-right: 0
}

#search_word {
	background-color: rgba(255, 255, 255, 50);
	border: 3px solid white;
	color: white;
	border-radius: 5px;
}

#search_word::focus {
	border: 2px solid rgb(163, 156, 255);
	border-radius: 6px
}

#search {
	background-color: #d3b291;
	border: 3px solid black;
	border-radius: 5px;
}

#search::pressed {
	background-color: #d3b291;
	border: 2px solid #986f43;
	border-radius: 6px;
	padding-left: 10px;
}

#Books, #container {	
	background-color: rgba(255, 255, 255, 10);
	border: 2px solid black;
	border-bottom: 0;
	border-radius: 5px;
	}
#booksFrame {
	background-color: rgba(0, 0, 0, 100)
}

#thumbnail {
	border: 1px solid black;
	border-top-left-radius: 5px
}

#thumbnail::hover {
	border: 3px solid rgb(105, 92, 255)
}

#bookTitle {
    font: 75 16pt "Verdana";
	color: black;
}

#bookTitle::hover{
    background-color: rgba(0, 0, 0, 100);
	color: #986f43
}
#download {
	background-color: rgb(47, 255, 33);
    text-align: left;
    padding-left: 20px;
	font: 75 16pt "Verdana";
	border: 1px solid black;
	border-bottom-left-radius: 20px;
	border-top-right-radius: 20px
}

#download::hover {
    padding-left: 50px;
    }

#download::pressed {
	border-radius: 0;
	border-bottom-right-radius: 20px;
	border-top-left-radius: 20px;
	padding-left: 20px;
}

#download::disabled {
    background-color: yellow
}
""")

    def setupUi(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setObjectName('main')
        self.resize(791, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleBar = QtWidgets.QFrame(self)
        self.titleBar.setMinimumSize(QtCore.QSize(10, 60))
        self.titleBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.titleBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleBar.setObjectName("titleBar")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.titleBar)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.logo = QtWidgets.QLabel(self.titleBar)
        self.logo.setMinimumSize(QtCore.QSize(70, 50))
        self.logo.setMaximumSize(QtCore.QSize(70, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("cache/7f5153dac8758955a9b3fe30c8d74f0178f9d3800235cf3039533f36c122cc61"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_4.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.titleBar)
        self.title.setMinimumSize(QtCore.QSize(1000, 0))
        self.title.setMaximumSize(QtCore.QSize(100, 1000))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_4.addWidget(self.title)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.paypal = QtWidgets.QPushButton(self.titleBar)
        self.paypal.setMaximumSize(QtCore.QSize(50, 60))
        self.paypal.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cache/6dddea5e300ffeda3cf84eadc98a887e6bcc044a127c76e8851f25f7e4e088f6"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paypal.setIcon(icon)
        self.paypal.setIconSize(QtCore.QSize(30, 30))
        self.paypal.setObjectName("paypal")
        self.horizontalLayout_3.addWidget(self.paypal)
        self.facebook = QtWidgets.QPushButton(self.titleBar)
        self.facebook.setMaximumSize(QtCore.QSize(50, 60))
        self.facebook.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cache/203fd5a31b8612536dd78b7552c43a6861cbfea5e371c53292b98712ebe4732b"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebook.setIcon(icon1)
        self.facebook.setIconSize(QtCore.QSize(30, 30))
        self.facebook.setObjectName("facebook")
        self.horizontalLayout_3.addWidget(self.facebook)
        self.minimize = QtWidgets.QPushButton(self.titleBar)
        self.minimize.setMinimumSize(QtCore.QSize(50, 30))
        self.minimize.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.minimize.setFont(font)
        self.minimize.setObjectName("minimize")
        self.horizontalLayout_3.addWidget(self.minimize)
        self.maximize = QtWidgets.QPushButton(self.titleBar)
        self.maximize.setProperty('max', False)
        self.maximize.setMinimumSize(QtCore.QSize(50, 30))
        self.maximize.setMaximumSize(QtCore.QSize(60, 60))
        self.maximize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cache/fa843c530d01d119bb2fe43dd1bb530960bd2c47ec69827eb1ed5462fd0af863"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("cache/50faabdf305d3364062fbd3070a15ddd712a49300e9063cd05d9410c628093d0"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.maximize.setIcon(icon)
        self.maximize.setIconSize(QtCore.QSize(40, 40))
        self.maximize.setCheckable(True)
        self.maximize.setObjectName("maximize")
        self.horizontalLayout_3.addWidget(self.maximize)
        self.exit = QtWidgets.QPushButton(self.titleBar)
        self.exit.setMinimumSize(QtCore.QSize(50, 30))
        self.exit.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("close")
        self.horizontalLayout_3.addWidget(self.exit)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.titleBar)
        self.booksFrame = QtWidgets.QFrame(self)
        self.booksFrame.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.booksFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.booksFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.booksFrame.setObjectName("booksFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.booksFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_word = QtWidgets.QLineEdit(self.booksFrame)
        self.search_word.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.search_word.setFont(font)
        self.search_word.setObjectName("search_word")
        self.horizontalLayout_2.addWidget(self.search_word)
        self.search = QtWidgets.QPushButton(self.booksFrame)
        self.search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("cache/807d8f6ff4020af1d8834e50f055d6cbd69a3018d8e9ee6093ed50cdf0d8aee1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setIconSize(QtCore.QSize(100, 30))
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.Books = QtWidgets.QScrollArea(self.booksFrame)
        self.Books.setMinimumSize(QtCore.QSize(0, 300))
        self.Books.setMaximumSize(QtCore.QSize(16777215, 600))
        self.Books.setWidgetResizable(True)
        self.Books.setObjectName("Books")
        self.container = QtWidgets.QWidget()
        self.container.setGeometry(QtCore.QRect(0, 0, 749, 384))
        self.container.setObjectName("container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Books.setWidget(self.container)
        self.verticalLayout_2.addWidget(self.Books)
        self.verticalLayout.addWidget(self.booksFrame)

        self.loading_label = QtWidgets.QLabel(self)
        self.loading = QtGui.QMovie('cache/53d1702680dca0c90ee75a34ffd15a7fd0c649b94aa095c6e3bce29b4a60c7e2')
        self.loading_label.setMovie(self.loading)
        self.loading_label.move(150, 150)
        self.loading_label.setScaledContents(True)
        self.loading_label.resize(500, 250)
        self.loading_label.hide()
        self.loading.start()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def addBook(self, _thumbnail, _title='ERROR', _download=None):
        if 'ERROR' in _title:
            msg = QtWidgets.QLabel(self.container)
            pixmap = QtGui.QPixmap(_thumbnail)
            msg.resize(300, 300)
            msg.setPixmap(
                    pixmap.scaled(
                        msg.size(), QtCore.Qt.KeepAspectRatio, 
                        QtCore.Qt.SmoothTransformation
                                )
                            )
            msg.setObjectName('msg')
            gridLayout = QtWidgets.QGridLayout()
            gridLayout.addWidget(msg, 0, 0, 2, 2)
            self.verticalLayout_3.addLayout(gridLayout)
        
        else:
            gridLayout = QtWidgets.QGridLayout()
            gridLayout.setObjectName("gridLayout")
            pixmap = QtGui.QPixmap(_thumbnail)
            thumbnail = QtWidgets.QLabel(self.container)
            thumbnail.setMinimumSize(QtCore.QSize(200, 200))
            thumbnail.setMaximumSize(QtCore.QSize(200, 200))
            thumbnail.setPixmap(
                    pixmap.scaled(
                        thumbnail.size(), QtCore.Qt.KeepAspectRatio, 
                        QtCore.Qt.SmoothTransformation
                                )
                            )
            thumbnail.setObjectName("thumbnail")
            gridLayout.addWidget(thumbnail, 0, 0, 2, 1)

            title = QtWidgets.QLabel(self.container)
            title.setText(_title)
            title.setWordWrap(True)
            title.setObjectName("bookTitle")
            gridLayout.addWidget(title, 0, 1, 1, 1)

            download = _download
            download.setObjectName("download")
            download.setMinimumSize(QtCore.QSize(200, 50))
            download.setText("DOWNLOAD")
            gridLayout.addWidget(download, 1, 1, 1, 1)

            self.verticalLayout_3.addLayout(gridLayout)            
            
        self.Books.setWidget(self.container)
    
    def clearSearch(self):
        del self.verticalLayout_3
        del self.container

        self.container = QtWidgets.QWidget()
        self.container.setGeometry(QtCore.QRect(0, 0, 749, 384))
        self.container.setObjectName("container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Books.setWidget(self.container)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("main", "Form"))
        self.title.setText(_translate("main", "BookZD"))
        self.minimize.setText(_translate("main", "_"))
        self.exit.setText(_translate("main", "X"))
        self.search_word.setPlaceholderText(_translate("main", "Enter book title you looking for..."))