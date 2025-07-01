# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindPairResultUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 368)
        Dialog.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(Dialog)
        self.Title.setObjectName(u"Title")
        self.Title.setScaledContents(True)

        self.verticalLayout.addWidget(self.Title)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.Continue = QPushButton(Dialog)
        self.Continue.setObjectName(u"Continue")

        self.verticalLayout.addWidget(self.Continue)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043d\u0435\u0446 \u0438\u0433\u0440\u044b", None))
        self.Title.setText(QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435 \u043f\u0430\u0440\u044b \u043d\u0430\u0439\u0434\u0435\u043d\u044b!", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b \u0441\u043f\u0440\u0430\u0432\u0438\u043b\u0438\u0441\u044c \u0437\u0430 ", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0418 \u043d\u0430\u0448\u043b\u0438 ", None))
        self.Continue.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c!", None))
    # retranslateUi

