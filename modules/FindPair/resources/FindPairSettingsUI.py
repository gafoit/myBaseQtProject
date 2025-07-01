# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindPairSettingsUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(287, 124)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.PTLabel = QLabel(Dialog)
        self.PTLabel.setObjectName(u"PTLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PTLabel.sizePolicy().hasHeightForWidth())
        self.PTLabel.setSizePolicy(sizePolicy)
        self.PTLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.PTLabel)

        self.preview_time = QSpinBox(Dialog)
        self.preview_time.setObjectName(u"preview_time")
        sizePolicy.setHeightForWidth(self.preview_time.sizePolicy().hasHeightForWidth())
        self.preview_time.setSizePolicy(sizePolicy)
        self.preview_time.setMinimum(10)
        self.preview_time.setMaximum(600000)
        self.preview_time.setValue(1000)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.preview_time)

        self.Label = QLabel(Dialog)
        self.Label.setObjectName(u"Label")
        sizePolicy.setHeightForWidth(self.Label.sizePolicy().hasHeightForWidth())
        self.Label.setSizePolicy(sizePolicy)
        self.Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.Label)

        self.pair_count = QSpinBox(Dialog)
        self.pair_count.setObjectName(u"pair_count")
        sizePolicy.setHeightForWidth(self.pair_count.sizePolicy().hasHeightForWidth())
        self.pair_count.setSizePolicy(sizePolicy)
        self.pair_count.setMinimum(2)
        self.pair_count.setMaximum(50)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.pair_count)

        self.ELabel = QLabel(Dialog)
        self.ELabel.setObjectName(u"ELabel")
        sizePolicy.setHeightForWidth(self.ELabel.sizePolicy().hasHeightForWidth())
        self.ELabel.setSizePolicy(sizePolicy)
        self.ELabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ELabel)

        self.Endless = QCheckBox(Dialog)
        self.Endless.setObjectName(u"Endless")
        sizePolicy.setHeightForWidth(self.Endless.sizePolicy().hasHeightForWidth())
        self.Endless.setSizePolicy(sizePolicy)
        self.Endless.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Endless.setAutoRepeat(False)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.Endless)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.restore = QPushButton(Dialog)
        self.restore.setObjectName(u"restore")

        self.horizontalLayout_2.addWidget(self.restore)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.save = QPushButton(Dialog)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.PTLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0435\u0434\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 (\u043c\u0441)", None))
        self.Label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u041a\u043e\u043b-\u0432\u043e <span style=\" font-weight:700;\">\u041f\u0430\u0440</span> \u043a\u0430\u0440\u0442\u043e\u0447\u0435\u043a:</p></body></html>", None))
        self.ELabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0445\u043e\u0434 \u043d\u0430 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.restore.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

