from PyQt5 import QtWidgets, QtCore
from shutil import rmtree
from mainGUI import BookDZGUI
from webbrowser import open
import os
import getBooks

class Worker(QtCore.QThread):
    result = QtCore.pyqtSignal(list)
    def __init__(self, mode, searchWord=None, url=None):
        super().__init__()
        self.mode = mode
        self.searchWord = searchWord
        self.url = url

    def run(self):
        if self.mode == 'search':
            self.result.emit(getBooks.booksc(self.searchWord))

        elif self.mode == 'download':
            msg = getBooks.download(self.url)
            self.result.emit(msg)

        elif self.mode == 'checkUpdate':
            self.result.emit(getBooks.checkUpdate())


class BookDZ(BookDZGUI):
    version = 'v1.4'
    def __init__(self):
        super().__init__()
        self.inintalizeUI()
    
    def inintalizeUI(self):
        self.worker = Worker(mode='checkUpdate')
        self.worker.start()
        self.worker.result.connect(self.checkUpdate)
        self.worker.finished.connect(lambda: 0)

        self.msg = QtWidgets.QMessageBox()
        self.minimize.clicked.connect(
            lambda: self.showMinimized()
        )
        self.maximize.clicked.connect(self.changeSize)
        self.exit.clicked.connect(self.closeEvent)
        self.search.clicked.connect(self.findBooks)
        self.facebook.clicked.connect(
            lambda: open('https://facebook.com/zahir.go')
        )
        self.paypal.clicked.connect(
            lambda: open('https://paypal.me/AZouhayer')
        )
    
    def changeSize(self):
        status = self.maximize.property('max')
        if status: 
            self.loading_label.move(150, 150)
            self.showNormal()

        else: 
            self.loading_label.move(450, 250)    
            self.showMaximized()
        
        self.maximize.setProperty('max', not status)
    
    def closeEvent(self, event=None):
        answer = self.msg.question(self, 'Quit', 
        'Are you sure you want to exit?',
        self.msg.Yes | self.msg.No, self.msg.No)
        if answer == self.msg.Yes: exit()
    
    def findBooks(self):
        self.loading_label.show()
        self.search.setDisabled(True)
        searchWord = self.search_word.text()
        self.worker = Worker('search', searchWord=searchWord)
        self.worker.start()
        self.worker.result.connect(self.addBooks)
        self.worker.finished.connect(
            lambda: self.loading_label.hide()
        )

    def addBooks(self, books):
        if books == []:
            self.addBook('cache/cf48e6721dd9de65fa53e93d01b35f78e73a5d866a29caa49386d06f073fb061')
        
        elif books[0] == 'NoNet':
            self.addBook('cache/aeace42249d7ca8c2c5afa293de35fb30500536c547e9adf785d4cddeeb0f502')

        else:
            self.clearSearch()
            for book in books:
                title = book[0]
                img_path = book[1]
                url = book[2]
                download = QtWidgets.QPushButton(self)
                download.setProperty('url', url)
                download.setProperty('title', title)
                download.clicked.connect(self.getBook)
                self.addBook(img_path, title, download)

        self.search.setEnabled(True)
        rmtree('./books/cache')
    
    def checkUpdate(self, data):
        if data == ['noNet']:
            self.addBook('cache/aeace42249d7ca8c2c5afa293de35fb30500536c547e9adf785d4cddeeb0f502')

        elif data[0] != self.version:
            answer = self.msg.question(self, 'Update', 
            'There is a new update!!\n Do you want to update now?',
            self.msg.Yes | self.msg.No, self.msg.No)
            if answer == self.msg.Yes:
                open(data[1])

        
    def getBook(self):
        currentBtn = self.sender()
        url = currentBtn.property('url')
        title = currentBtn.property('title')
        currentBtn.setDisabled(True)
        currentBtn.setText('Downloading...')
        self.worker = Worker(mode='download', url=url)
        self.worker.start()
        self.worker.result.connect(
            lambda error: self.done(title, currentBtn, error))
        self.worker.finished.connect(
            lambda: None
            )
    
    def done(self, title, btn, error):
        print(error)
        if error == ['noNet']:
            self.addBook('cache/aeace42249d7ca8c2c5afa293de35fb30500536c547e9adf785d4cddeeb0f502')

        if error == [False]:
            self.msg.information(self, 'Limits!!', 
            'You can download only 5 books in 24H.',
            self.msg.Ok, self.msg.Ok
            )
        else:
            self.msg.information(self, 'Done', 
                f'{title} at "{os.getcwd()}/books".',
                self.msg.Ok, self.msg.Ok)
            
            if error[1] == 'epub':
                answer = self.msg.question(self, 'Convert',
                'This book is not pdf format.\n' +
                'Do you like to convert it to pdf',
                self.msg.Yes | self.msg.No, self.msg.No)
                if answer == self.msg.Yes:
                    open('https://www.freepdfconvert.com/epub-to-pdf')
        
        btn.setEnabled(True)
        btn.setText("Download")
        

if __name__  == '__main__':
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    window = BookDZ()
    window.show()
    sys.exit(app.exec_())