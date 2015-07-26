import re

from PySide import QtGui, QtCore
from PySide.QtGui import QPixmap

from rtsi.service.text_service import TextService


__author__ = 'hoebart'


class StoryWindow(QtGui.QMainWindow):
    def __init__(self, text):
        """
        Initialize Story Window
        :param text: text that should be displayed
        """
        super().__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")

        self.image_list = []
        self.img_index = 0
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.main_layout = QtGui.QVBoxLayout(self.central_widget)
        self.main_layout.setObjectName("mainlayout")
        spacer_item = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.main_layout.addItem(spacer_item)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.grid_layout.setObjectName("grid_layout")

        self.image_frame = QtGui.QFrame(self)
        self.image_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.image_frame.setMaximumSize(QtCore.QSize(16777215, 512))

        self.image_layout = QtGui.QHBoxLayout(self.image_frame)
        self.image_layout.setSpacing(120)
        self.image_layout.setContentsMargins(40, -1, 40, -1)

        self.image_holder3 = QtGui.QLabel(self.image_frame)
        self.image_holder3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.image_holder3.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder3)

        self.image_holder2 = QtGui.QLabel(self.image_frame)
        self.image_holder2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.image_holder2.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder2)

        self.image_holder1 = QtGui.QLabel(self.image_frame)
        self.image_holder1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.image_holder1.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder1)

        self.grid_layout.addWidget(self.image_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.grid_layout)

        self.frame = QtGui.QFrame(self)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))

        self.subtitle_layout = QtGui.QGridLayout(self.frame)

        self.subtitle_label = QtGui.QLabel(self.frame)
        self.subtitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_label.setObjectName("subtitle_label")

        self.subtitle_layout.addWidget(self.subtitle_label, 0, 0, 1, 1)
        self.main_layout.addWidget(self.frame)
        self.setCentralWidget(self.central_widget)

        self.subtitle_label.setText(QtGui.QApplication.translate("Form", "Subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowTitle(
            QtGui.QApplication.translate("StoryWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))

        self.text_service = TextService(text, self)
        self.text_service.change_img.connect(self.switch_to_next_image)

    def append_images(self, images):
        """
        Adds an image to the 'playlist' of images.
        :param image: Image which should be added
        """
        self.image_list.extend(images)
        self.switch_to_next_image()

    @QtCore.Slot()
    def switch_to_next_image(self):
        """
        Takes next image from the list and displays it e.g. when sentence ends.
        """
        if self.image_list[self.img_index] is not None:
            img = QPixmap()
            img.loadFromData(self.image_list[self.img_index])
            self.image_holder2.setPixmap(img)
        else:
            self.image_holder2.setPixmap(None)

        self.img_index += 1
        QtGui.QApplication.processEvents()

    def start(self):
        self.text_service.start_story()
