# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FindPairMainWindowUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.MainMenu = QAction(MainWindow)
        self.MainMenu.setObjectName(u"MainMenu")
        self.ModeOptions = QAction(MainWindow)
        self.ModeOptions.setObjectName(u"ModeOptions")
        self.CardsFont = QAction(MainWindow)
        self.CardsFont.setObjectName(u"CardsFont")
        self.MainFont = QAction(MainWindow)
        self.MainFont.setObjectName(u"MainFont")
        self.CardFont = QAction(MainWindow)
        self.CardFont.setObjectName(u"CardFont")
        self.MainFont_2 = QAction(MainWindow)
        self.MainFont_2.setObjectName(u"MainFont_2")
        self.MainFont_2.setEnabled(True)
        self.MainFont_2.setShortcutContext(Qt.ShortcutContext.WidgetShortcut)
        self.CardFont_2 = QAction(MainWindow)
        self.CardFont_2.setObjectName(u"CardFont_2")
        self.ModeOptions_2 = QAction(MainWindow)
        self.ModeOptions_2.setObjectName(u"ModeOptions_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PairsFound = QLabel(self.centralwidget)
        self.PairsFound.setObjectName(u"PairsFound")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PairsFound.sizePolicy().hasHeightForWidth())
        self.PairsFound.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.PairsFound.setFont(font)
        self.PairsFound.setWordWrap(True)

        self.horizontalLayout.addWidget(self.PairsFound)

        self.PairsLeft = QLabel(self.centralwidget)
        self.PairsLeft.setObjectName(u"PairsLeft")
        sizePolicy.setHeightForWidth(self.PairsLeft.sizePolicy().hasHeightForWidth())
        self.PairsLeft.setSizePolicy(sizePolicy)
        self.PairsLeft.setFont(font)
        self.PairsLeft.setWordWrap(True)

        self.horizontalLayout.addWidget(self.PairsLeft)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setLineWidth(2)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.StartButton = QPushButton(self.centralwidget)
        self.StartButton.setObjectName(u"StartButton")

        self.gridLayout.addWidget(self.StartButton, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.Shortcuts = QMenu(self.menubar)
        self.Shortcuts.setObjectName(u"Shortcuts")
        self.DisplayOptions = QMenu(self.menubar)
        self.DisplayOptions.setObjectName(u"DisplayOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(False)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.Shortcuts.menuAction())
        self.menubar.addAction(self.DisplayOptions.menuAction())
        self.Shortcuts.addAction(self.MainMenu)
        self.Shortcuts.addSeparator()
        self.DisplayOptions.addAction(self.ModeOptions_2)
        self.DisplayOptions.addSeparator()
        self.DisplayOptions.addAction(self.MainFont_2)
        self.DisplayOptions.addAction(self.CardFont_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainMenu.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u041c\u0435\u043d\u044e", None))
        self.ModeOptions.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.CardsFont.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u0435\u043a", None))
        self.MainFont.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.MainFont.setIconText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0442\u0435\u043a\u0441\u0442", None))
        self.CardFont.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438", None))
        self.CardFont.setIconText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u043e\u0447\u043a\u0438", None))
        self.MainFont_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0448\u0440\u0438\u0444\u0442", None))
#if QT_CONFIG(statustip)
        self.MainFont_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.MainFont_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.CardFont_2.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442 \u043a\u0430\u0440\u0442\u043e\u0447\u0435\u043a", None))
        self.ModeOptions_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c", None))
        self.PairsFound.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440 \u041d\u0430\u0439\u0434\u0435\u043d\u043e:", None))
        self.PairsLeft.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440 \u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c:", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0418\u0433\u0440\u0443", None))
        self.Shortcuts.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.DisplayOptions.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c", None))
    # retranslateUi

