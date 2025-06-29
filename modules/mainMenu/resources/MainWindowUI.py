# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.NonModal)
        Dialog.resize(496, 252)
        Dialog.setStyleSheet(u"")
        Dialog.setModal(True)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.BigFrame = QFrame(Dialog)
        self.BigFrame.setObjectName(u"BigFrame")
        self.BigFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.gridLayout_3 = QGridLayout(self.BigFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line = QFrame(self.BigFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 9, 1, 1, 1)

        self.label = QLabel(self.BigFrame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.CloseButton = QPushButton(self.BigFrame)
        self.CloseButton.setObjectName(u"CloseButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.CloseButton, 12, 1, 1, 1)

        self.FindPair = QPushButton(self.BigFrame)
        self.FindPair.setObjectName(u"FindPair")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FindPair.sizePolicy().hasHeightForWidth())
        self.FindPair.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.FindPair, 7, 1, 1, 1)

        self.Desc = QPushButton(self.BigFrame)
        self.Desc.setObjectName(u"Desc")
        sizePolicy1.setHeightForWidth(self.Desc.sizePolicy().hasHeightForWidth())
        self.Desc.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.Desc, 10, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.Counting = QPushButton(self.BigFrame)
        self.Counting.setObjectName(u"Counting")
        sizePolicy2.setHeightForWidth(self.Counting.sizePolicy().hasHeightForWidth())
        self.Counting.setSizePolicy(sizePolicy2)
        self.Counting.setMinimumSize(QSize(226, 0))

        self.gridLayout.addWidget(self.Counting, 0, 1, 1, 1)

        self.Formula = QPushButton(self.BigFrame)
        self.Formula.setObjectName(u"Formula")
        sizePolicy2.setHeightForWidth(self.Formula.sizePolicy().hasHeightForWidth())
        self.Formula.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.Formula, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 4, 1, 1, 1)

        self.Concentration = QPushButton(self.BigFrame)
        self.Concentration.setObjectName(u"Concentration")
        sizePolicy2.setHeightForWidth(self.Concentration.sizePolicy().hasHeightForWidth())
        self.Concentration.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.Concentration, 5, 1, 1, 1)

        self.FontOptions = QPushButton(self.BigFrame)
        self.FontOptions.setObjectName(u"FontOptions")
        sizePolicy1.setHeightForWidth(self.FontOptions.sizePolicy().hasHeightForWidth())
        self.FontOptions.setSizePolicy(sizePolicy1)
        self.FontOptions.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.FontOptions, 11, 1, 1, 1)


        self.gridLayout_2.addWidget(self.BigFrame, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0436\u0438\u043c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u0435\u0436\u0438\u043c", None))
        self.CloseButton.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.FindPair.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.Desc.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.Counting.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.Formula.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.Concentration.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.FontOptions.setText(QCoreApplication.translate("Dialog", u"aboba", None))
    # retranslateUi

