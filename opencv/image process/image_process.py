from design import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import cv2
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Resim verisini saklamak için bir değişken
        self.image = None

        # Butonlar için sinyaller
        self.ui.pushButton_3.clicked.connect(self.loadImage)
        self.ui.pushButton.clicked.connect(self.color)
        self.ui.pushButton_2.clicked.connect(self.grayscale)
        self.ui.pushButton_4.clicked.connect(self.unchanged)

    def loadImage(self):
        # Resim seçimi
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Fotoğraf Seç", 
            "", 
            "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp);;Tüm Dosyalar (*)", 
            options=options
        )

        if file_path:
            # OpenCV ile resmi yükleme
            self.image = cv2.imread(file_path)
            if self.image is not None:
                # QLabel üzerinde resmi göstermek için QPixmap'e dönüştürme
                height, width, channel = self.image.shape
                bytes_per_line = channel * width
                q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format_BGR888)
                self.ui.label.setPixmap(QPixmap.fromImage(q_image).scaled(self.ui.label.size(), Qt.KeepAspectRatio))

    def color(self):
        if self.image is not None:
            # Renkli görüntü için OpenCV'de herhangi bir işlem yapmadan gösterme
            height, width, channel = self.image.shape
            bytes_per_line = channel * width
            q_image = QImage(self.image.data, width, height, bytes_per_line, QImage.Format_BGR888)
            self.ui.label.setPixmap(QPixmap.fromImage(q_image).scaled(self.ui.label.size(), Qt.KeepAspectRatio))

    def grayscale(self):
        if self.image is not None:
            # Grayscale dönüşümü
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            height, width = gray_image.shape
            bytes_per_line = width
            q_image = QImage(gray_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            self.ui.label.setPixmap(QPixmap.fromImage(q_image).scaled(self.ui.label.size(), Qt.KeepAspectRatio))

    def unchanged(self):
        if self.image is not None:
            # Orijinal görüntü değişmeden gösteriliyor
            self.color()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
