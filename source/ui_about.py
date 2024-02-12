# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutfrRpFm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import new_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 240)
        Form.setWindowOpacity(1.000000000000000)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(100, 100))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icon_t.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(187, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.label)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Converter</p><p>Version 0.1</p><p>This is a tool for different conversions and more.</p><p>This program is using following libraries:<br/>Python: 3.12.2<br/>PySide: 6.6.1<br/>ctypes: 1.1.0</p><p>Copyright \u00a9 2024 Roman Stetsiuk</p><p>Source code: <a href=\"https://github.com/curious-grapes/converter-tool\"><span style=\" text-decoration: underline; color:#0000ff;\">Github<br/></span></a>My website: <a href=\"https://curious-grapes.one/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://curious-grapes.one/</span></a></p></body></html>", None))
    # retranslateUi

