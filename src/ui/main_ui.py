# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"background-color: rgb(232, 234, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.auth = QWidget()
        self.auth.setObjectName(u"auth")
        self.gridLayout = QGridLayout(self.auth)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.AuthWidget = QWidget(self.auth)
        self.AuthWidget.setObjectName(u"AuthWidget")
        self.verticalLayout_2 = QVBoxLayout(self.AuthWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login = QLineEdit(self.AuthWidget)
        self.login.setObjectName(u"login")

        self.verticalLayout_2.addWidget(self.login)

        self.password = QLineEdit(self.AuthWidget)
        self.password.setObjectName(u"password")

        self.verticalLayout_2.addWidget(self.password)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.enter = QPushButton(self.AuthWidget)
        self.enter.setObjectName(u"enter")

        self.horizontalLayout_4.addWidget(self.enter)

        self.reg_a = QPushButton(self.AuthWidget)
        self.reg_a.setObjectName(u"reg_a")

        self.horizontalLayout_4.addWidget(self.reg_a)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.auth_tip = QLabel(self.AuthWidget)
        self.auth_tip.setObjectName(u"auth_tip")
        self.auth_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.auth_tip)


        self.gridLayout.addWidget(self.AuthWidget, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.auth)
        self.register_2 = QWidget()
        self.register_2.setObjectName(u"register_2")
        self.gridLayout_3 = QGridLayout(self.register_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.w_layout = QWidget(self.register_2)
        self.w_layout.setObjectName(u"w_layout")
        self.verticalLayout_6 = QVBoxLayout(self.w_layout)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.fio = QLineEdit(self.w_layout)
        self.fio.setObjectName(u"fio")

        self.verticalLayout_6.addWidget(self.fio)

        self.phone = QLineEdit(self.w_layout)
        self.phone.setObjectName(u"phone")

        self.verticalLayout_6.addWidget(self.phone)

        self.r_login = QLineEdit(self.w_layout)
        self.r_login.setObjectName(u"r_login")

        self.verticalLayout_6.addWidget(self.r_login)

        self.r_password = QLineEdit(self.w_layout)
        self.r_password.setObjectName(u"r_password")

        self.verticalLayout_6.addWidget(self.r_password)

        self.user_type = QComboBox(self.w_layout)
        self.user_type.addItem("")
        self.user_type.addItem("")
        self.user_type.addItem("")
        self.user_type.setObjectName(u"user_type")

        self.verticalLayout_6.addWidget(self.user_type)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reg = QPushButton(self.w_layout)
        self.reg.setObjectName(u"reg")

        self.horizontalLayout_5.addWidget(self.reg)

        self.cancel = QPushButton(self.w_layout)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_5.addWidget(self.cancel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.gridLayout_3.addWidget(self.w_layout, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.register_2)
        self.table_page = QWidget()
        self.table_page.setObjectName(u"table_page")
        self.horizontalLayout_2 = QHBoxLayout(self.table_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.table_page)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_4.addWidget(self.pushButton_4)

        self.stats = QPushButton(self.widget)
        self.stats.setObjectName(u"stats")

        self.verticalLayout_4.addWidget(self.stats)

        self.logout = QPushButton(self.widget)
        self.logout.setObjectName(u"logout")

        self.verticalLayout_4.addWidget(self.logout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedData = QStackedWidget(self.table_page)
        self.stackedData.setObjectName(u"stackedData")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedData.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedData.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedData)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add = QPushButton(self.table_page)
        self.add.setObjectName(u"add")

        self.horizontalLayout.addWidget(self.add)

        self.change = QPushButton(self.table_page)
        self.change.setObjectName(u"change")

        self.horizontalLayout.addWidget(self.change)

        self.remove = QPushButton(self.table_page)
        self.remove.setObjectName(u"remove")

        self.horizontalLayout.addWidget(self.remove)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.table_page)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.table_page)
        self.stats_2 = QWidget()
        self.stats_2.setObjectName(u"stats_2")
        self.verticalLayout_5 = QVBoxLayout(self.stats_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.s_back = QPushButton(self.stats_2)
        self.s_back.setObjectName(u"s_back")

        self.horizontalLayout_3.addWidget(self.s_back)

        self.pushButton_5 = QPushButton(self.stats_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.stats_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.stackedWidget.addWidget(self.stats_2)
        self.z = QWidget()
        self.z.setObjectName(u"z")
        self.widget_3 = QWidget(self.z)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(140, 0, 93, 564))
        self.widget_3.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_9 = QPushButton(self.widget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_8.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_8.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_8.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_8.addWidget(self.pushButton_12)

        self.logout_3 = QPushButton(self.widget_3)
        self.logout_3.setObjectName(u"logout_3")

        self.verticalLayout_8.addWidget(self.logout_3)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.layoutWidget_2 = QWidget(self.z)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(320, 140, 305, 238))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_3 = QPushButton(self.layoutWidget_2)
        self.add_3.setObjectName(u"add_3")

        self.horizontalLayout_6.addWidget(self.add_3)

        self.change_3 = QPushButton(self.layoutWidget_2)
        self.change_3.setObjectName(u"change_3")

        self.horizontalLayout_6.addWidget(self.change_3)

        self.remove_3 = QPushButton(self.layoutWidget_2)
        self.remove_3.setObjectName(u"remove_3")

        self.horizontalLayout_6.addWidget(self.remove_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.tableWidget_3 = QTableWidget(self.layoutWidget_2)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_9.addWidget(self.tableWidget_3)

        self.stackedWidget.addWidget(self.z)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedData.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.enter.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.reg_a.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.auth_tip.setText("")
        self.fio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.r_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.r_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.user_type.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.user_type.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440", None))
        self.user_type.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440", None))

        self.reg.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043e\u0440\u044b", None))
        self.stats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.remove.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.s_back.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u044b\u0445 \u0437\u0430\u044f\u0432\u043e\u043a: ", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u044f\u0432\u043a\u0438", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043e\u0440\u044b", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.logout_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.add_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.change_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.remove_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

