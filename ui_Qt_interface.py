# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt_interfaceoYbFNK.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)
import new_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 404)
        self.actionGithub_page = QAction(MainWindow)
        self.actionGithub_page.setObjectName(u"actionGithub_page")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionCheck_for_updates = QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_11 = QHBoxLayout(self.tab)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.flow_rate_input = QLineEdit(self.groupBox)
        self.flow_rate_input.setObjectName(u"flow_rate_input")
#if QT_CONFIG(tooltip)
        self.flow_rate_input.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.flow_rate_input.setToolTipDuration(-1)

        self.horizontalLayout.addWidget(self.flow_rate_input)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.density_input = QLineEdit(self.groupBox)
        self.density_input.setObjectName(u"density_input")

        self.horizontalLayout_2.addWidget(self.density_input)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.flow_rate_output = QLineEdit(self.groupBox)
        self.flow_rate_output.setObjectName(u"flow_rate_output")
        self.flow_rate_output.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.flow_rate_output)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_5 = QSpacerItem(255, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.side_length_input = QLineEdit(self.groupBox_2)
        self.side_length_input.setObjectName(u"side_length_input")

        self.horizontalLayout_4.addWidget(self.side_length_input)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.base_a_input = QLineEdit(self.groupBox_2)
        self.base_a_input.setObjectName(u"base_a_input")

        self.horizontalLayout_5.addWidget(self.base_a_input)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.base_b_input = QLineEdit(self.groupBox_2)
        self.base_b_input.setObjectName(u"base_b_input")

        self.horizontalLayout_6.addWidget(self.base_b_input)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.height_output = QLineEdit(self.groupBox_2)
        self.height_output.setObjectName(u"height_output")
        self.height_output.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.height_output)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_8.addWidget(self.groupBox_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 135, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 651, 22))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addAction(self.actionDocumentation)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGithub_page.setText(QCoreApplication.translate("MainWindow", u"Github page", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionCheck_for_updates.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"L/min to kg/s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Flow rate in L/min:", None))
#if QT_CONFIG(whatsthis)
        self.flow_rate_input.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.flow_rate_input.setText("")
        self.flow_rate_input.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Density in g/l or kg/m^3:", None))
        self.density_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.225 for N", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Your flow rate in kg/s:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Length to height", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Side length s:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Base a:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Base b:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

