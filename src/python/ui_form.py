# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import ressources_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1279, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setMaximumSize(QSize(16777215, 16777215))
        Widget.setStyleSheet(u"background-color:#0A192D;\n"
"color:#F0F5FF;")
        self.verticalLayout_3 = QVBoxLayout(Widget)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QWidget(Widget)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMinimumSize(QSize(1279, 61))
        self.titleBar.setStyleSheet(u"background-color:#070F1C;\n"
"color:#F0F5FF;")
        self.titre = QLabel(self.titleBar)
        self.titre.setObjectName(u"titre")
        self.titre.setGeometry(QRect(50, 5, 161, 18))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titre.setFont(font)
        self.description = QLabel(self.titleBar)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(50, 25, 251, 18))
        self.description.setStyleSheet(u"padding:0px;")
        self.logo_linux = QLabel(self.titleBar)
        self.logo_linux.setObjectName(u"logo_linux")
        self.logo_linux.setGeometry(QRect(10, 10, 31, 31))
        self.logo_linux.setPixmap(QPixmap(u":/icons/icons/linux.png"))
        self.logo_linux.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.titleBar)

        self.horizontalWidget = QWidget(Widget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 611))
        self.horizontalWidget.setStyleSheet(u"background:#0A192D;")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 1, -1)
        self.sidebar = QWidget(self.horizontalWidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setStyleSheet(u"background-color:#070F1C;\n"
"color:#F0F5FF;")
        self.verticalLayout = QVBoxLayout(self.sidebar)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bouton_apercu = QPushButton(self.sidebar)
        self.bouton_apercu.setObjectName(u"bouton_apercu")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.bouton_apercu.setFont(font1)
        self.bouton_apercu.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"	font-weight:bold;\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_apercu.setIcon(icon)
        self.bouton_apercu.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_apercu)

        self.bouton_systeme = QPushButton(self.sidebar)
        self.bouton_systeme.setObjectName(u"bouton_systeme")
        self.bouton_systeme.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/ecran-dordinateur.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_systeme.setIcon(icon1)
        self.bouton_systeme.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_systeme)

        self.bouton_materiel = QPushButton(self.sidebar)
        self.bouton_materiel.setObjectName(u"bouton_materiel")
        self.bouton_materiel.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/ordinateur.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_materiel.setIcon(icon2)
        self.bouton_materiel.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_materiel)

        self.bouton_reseau = QPushButton(self.sidebar)
        self.bouton_reseau.setObjectName(u"bouton_reseau")
        self.bouton_reseau.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/linternet.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_reseau.setIcon(icon3)
        self.bouton_reseau.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_reseau)

        self.bouton_stockage = QPushButton(self.sidebar)
        self.bouton_stockage.setObjectName(u"bouton_stockage")
        self.bouton_stockage.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/base-de-donnees.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_stockage.setIcon(icon4)
        self.bouton_stockage.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_stockage)

        self.bouton_processus = QPushButton(self.sidebar)
        self.bouton_processus.setObjectName(u"bouton_processus")
        self.bouton_processus.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:transparent;\n"
"	width: 100%;\n"
"	padding: 7px 0px 7px 10px;\n"
"	border-radius: 8px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/processus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_processus.setIcon(icon5)
        self.bouton_processus.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.bouton_processus)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sidebar)

        self.conteneur_accueil = QStackedWidget(self.horizontalWidget)
        self.conteneur_accueil.setObjectName(u"conteneur_accueil")
        self.conteneur_accueil.setMinimumSize(QSize(1052, 0))
        self.pageApercu = QWidget()
        self.pageApercu.setObjectName(u"pageApercu")
        self.verticalLayout_2 = QVBoxLayout(self.pageApercu)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 10, 15, 2)
        self.conteneur_titreParMenu = QGroupBox(self.pageApercu)
        self.conteneur_titreParMenu.setObjectName(u"conteneur_titreParMenu")
        self.conteneur_titreParMenu.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.label_titreParMenu = QLabel(self.conteneur_titreParMenu)
        self.label_titreParMenu.setObjectName(u"label_titreParMenu")
        self.label_titreParMenu.setGeometry(QRect(0, 0, 151, 18))
        self.label_titreParMenu.setFont(font)
        self.label_descriptionParMenu = QLabel(self.conteneur_titreParMenu)
        self.label_descriptionParMenu.setObjectName(u"label_descriptionParMenu")
        self.label_descriptionParMenu.setGeometry(QRect(0, 20, 321, 18))

        self.verticalLayout_2.addWidget(self.conteneur_titreParMenu)

        self.conteneurInfoPrincipal = QHBoxLayout()
        self.conteneurInfoPrincipal.setSpacing(10)
        self.conteneurInfoPrincipal.setObjectName(u"conteneurInfoPrincipal")
        self.conteneurInfoPrincipal.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_4 = QGroupBox(self.pageApercu)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 30, 30, 30))
        self.label_6.setPixmap(QPixmap(u"icons/monitor.png"))
        self.label_6.setScaledContents(True)
        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 30, 181, 91))
        self.layout_system = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_system.setObjectName(u"layout_system")
        self.layout_system.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 5, 66, 18))

        self.conteneurInfoPrincipal.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.pageApercu)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_8 = QLabel(self.groupBox_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 30, 30, 30))
        self.label_8.setPixmap(QPixmap(u"icons/chip.png"))
        self.label_8.setScaledContents(True)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 30, 181, 91))
        self.layout_processeur = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_processeur.setObjectName(u"layout_processeur")
        self.layout_processeur.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 5, 81, 18))

        self.conteneurInfoPrincipal.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.pageApercu)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 30, 30, 30))
        self.label_9.setPixmap(QPixmap(u"icons/memory.png"))
        self.label_9.setScaledContents(True)
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(50, 30, 181, 91))
        self.layout_ram = QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_ram.setObjectName(u"layout_ram")
        self.layout_ram.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 5, 101, 18))

        self.conteneurInfoPrincipal.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.pageApercu)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 30, 30, 30))
        self.label_10.setPixmap(QPixmap(u"icons/hard-drive.png"))
        self.label_10.setScaledContents(True)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_7)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(50, 30, 181, 91))
        self.layout_fs = QVBoxLayout(self.verticalLayoutWidget_4)
        self.layout_fs.setObjectName(u"layout_fs")
        self.layout_fs.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 5, 131, 18))

        self.conteneurInfoPrincipal.addWidget(self.groupBox_7)


        self.verticalLayout_2.addLayout(self.conteneurInfoPrincipal)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_8 = QGroupBox(self.pageApercu)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_14 = QLabel(self.groupBox_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 10, 151, 18))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_14.setFont(font2)
        self.gridLayoutWidget_4 = QWidget(self.groupBox_8)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 30, 311, 141))
        self.gridLayout_system = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_system.setObjectName(u"gridLayout_system")
        self.gridLayout_system.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.pageApercu)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_15 = QLabel(self.groupBox_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 181, 18))
        font3 = QFont()
        font3.setBold(True)
        self.label_15.setFont(font3)
        self.gridLayoutWidget_5 = QWidget(self.groupBox_9)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 30, 311, 141))
        self.gridLayout_ressource = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_ressource.setObjectName(u"gridLayout_ressource")
        self.gridLayout_ressource.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.pageApercu)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_16 = QLabel(self.groupBox_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 201, 18))
        self.label_16.setFont(font3)
        self.gridLayoutWidget = QWidget(self.groupBox_10)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 311, 111))
        self.grid_reseau = QGridLayout(self.gridLayoutWidget)
        self.grid_reseau.setObjectName(u"grid_reseau")
        self.grid_reseau.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.grid_reseau.addWidget(self.label_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.grid_reseau.addWidget(self.label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.grid_reseau.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_3.addWidget(self.groupBox_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_11 = QGroupBox(self.pageApercu)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_17 = QLabel(self.groupBox_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 10, 66, 18))
        self.label_17.setFont(font3)
        self.gridLayoutWidget_2 = QWidget(self.groupBox_11)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 30, 551, 141))
        self.gridLayout_fs = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_fs.setObjectName(u"gridLayout_fs")
        self.gridLayout_fs.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.gridLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.gridLayout_fs.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout_fs.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.gridLayout_fs.addWidget(self.label_20, 0, 1, 1, 1)

        self.gridLayout_fs.setColumnStretch(0, 1)
        self.gridLayout_fs.setColumnStretch(2, 2)

        self.horizontalLayout_4.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.pageApercu)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 10, 181, 18))
        self.label_18.setFont(font3)
        self.gridLayoutWidget_3 = QWidget(self.groupBox_12)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 30, 431, 111))
        self.gridLayout_materiel = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_materiel.setObjectName(u"gridLayout_materiel")
        self.gridLayout_materiel.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.groupBox_12)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 4)
        self.verticalLayout_2.setStretch(3, 4)
        self.conteneur_accueil.addWidget(self.pageApercu)
        self.pageSysteme = QWidget()
        self.pageSysteme.setObjectName(u"pageSysteme")
        self.verticalLayout_4 = QVBoxLayout(self.pageSysteme)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 10, 15, 2)
        self.conteneur_titreParMenu_2 = QGroupBox(self.pageSysteme)
        self.conteneur_titreParMenu_2.setObjectName(u"conteneur_titreParMenu_2")
        self.conteneur_titreParMenu_2.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.label_titreParMenu_2 = QLabel(self.conteneur_titreParMenu_2)
        self.label_titreParMenu_2.setObjectName(u"label_titreParMenu_2")
        self.label_titreParMenu_2.setGeometry(QRect(0, 0, 251, 18))
        self.label_titreParMenu_2.setFont(font)
        self.label_descriptionParMenu_2 = QLabel(self.conteneur_titreParMenu_2)
        self.label_descriptionParMenu_2.setObjectName(u"label_descriptionParMenu_2")
        self.label_descriptionParMenu_2.setGeometry(QRect(0, 20, 391, 18))

        self.verticalLayout_4.addWidget(self.conteneur_titreParMenu_2)

        self.conteneurInfoPrincipal_2 = QHBoxLayout()
        self.conteneurInfoPrincipal_2.setSpacing(10)
        self.conteneurInfoPrincipal_2.setObjectName(u"conteneurInfoPrincipal_2")
        self.conteneurInfoPrincipal_2.setContentsMargins(-1, -1, 0, 0)
        self.groupBox_13 = QGroupBox(self.pageSysteme)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_titreParMenu_4 = QLabel(self.groupBox_13)
        self.label_titreParMenu_4.setObjectName(u"label_titreParMenu_4")
        self.label_titreParMenu_4.setGeometry(QRect(10, 10, 251, 18))
        self.label_titreParMenu_4.setFont(font)
        self.gridLayoutWidget_6 = QWidget(self.groupBox_13)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 40, 481, 341))
        self.gridLayout_information_base = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_information_base.setObjectName(u"gridLayout_information_base")
        self.gridLayout_information_base.setContentsMargins(0, 0, 0, 0)

        self.conteneurInfoPrincipal_2.addWidget(self.groupBox_13)

        self.groupBox_15 = QGroupBox(self.pageSysteme)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.gridLayoutWidget_7 = QWidget(self.groupBox_15)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 40, 471, 341))
        self.gridLayout_environnement = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_environnement.setObjectName(u"gridLayout_environnement")
        self.gridLayout_environnement.setContentsMargins(0, 0, 0, 0)
        self.label_titreParMenu_7 = QLabel(self.groupBox_15)
        self.label_titreParMenu_7.setObjectName(u"label_titreParMenu_7")
        self.label_titreParMenu_7.setGeometry(QRect(10, 10, 251, 18))
        self.label_titreParMenu_7.setFont(font)

        self.conteneurInfoPrincipal_2.addWidget(self.groupBox_15)

        self.conteneurInfoPrincipal_2.setStretch(0, 1)
        self.conteneurInfoPrincipal_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.conteneurInfoPrincipal_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 10)
        self.conteneur_accueil.addWidget(self.pageSysteme)
        self.pageMateriel = QWidget()
        self.pageMateriel.setObjectName(u"pageMateriel")
        self.verticalLayout_11 = QVBoxLayout(self.pageMateriel)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 10, 15, 2)
        self.conteneur_titreParMenu_3 = QGroupBox(self.pageMateriel)
        self.conteneur_titreParMenu_3.setObjectName(u"conteneur_titreParMenu_3")
        self.conteneur_titreParMenu_3.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.label_titreParMenu_3 = QLabel(self.conteneur_titreParMenu_3)
        self.label_titreParMenu_3.setObjectName(u"label_titreParMenu_3")
        self.label_titreParMenu_3.setGeometry(QRect(0, 0, 251, 18))
        self.label_titreParMenu_3.setFont(font)
        self.label_descriptionParMenu_3 = QLabel(self.conteneur_titreParMenu_3)
        self.label_descriptionParMenu_3.setObjectName(u"label_descriptionParMenu_3")
        self.label_descriptionParMenu_3.setGeometry(QRect(0, 20, 391, 18))

        self.verticalLayout_11.addWidget(self.conteneur_titreParMenu_3)

        self.horizontalWidget_2 = QWidget(self.pageMateriel)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_20 = QGroupBox(self.horizontalWidget_2)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_37 = QLabel(self.groupBox_20)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(50, 10, 141, 18))
        self.label_37.setFont(font3)
        self.gridLayoutWidget_8 = QWidget(self.groupBox_20)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 40, 311, 331))
        self.gridLayout_cpu = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_cpu.setObjectName(u"gridLayout_cpu")
        self.gridLayout_cpu.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.groupBox_20)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 10, 30, 30))
        self.label_19.setPixmap(QPixmap(u"icons/chip.png"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.groupBox_20)

        self.groupBox_21 = QGroupBox(self.horizontalWidget_2)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_38 = QLabel(self.groupBox_21)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(50, 10, 161, 18))
        self.label_38.setFont(font3)
        self.gridLayoutWidget_9 = QWidget(self.groupBox_21)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 40, 311, 331))
        self.gridLayout_ram = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_ram.setObjectName(u"gridLayout_ram")
        self.gridLayout_ram.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.groupBox_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 10, 30, 30))
        self.label_21.setPixmap(QPixmap(u"icons/memory.png"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.groupBox_21)

        self.groupBox_22 = QGroupBox(self.horizontalWidget_2)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_39 = QLabel(self.groupBox_22)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(50, 10, 141, 18))
        self.label_39.setFont(font3)
        self.gridLayoutWidget_10 = QWidget(self.groupBox_22)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 40, 311, 331))
        self.gridLayout_disque = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_disque.setObjectName(u"gridLayout_disque")
        self.gridLayout_disque.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.groupBox_22)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 10, 30, 30))
        self.label_23.setPixmap(QPixmap(u"icons/hard-drive.png"))
        self.label_23.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.groupBox_22)


        self.verticalLayout_11.addWidget(self.horizontalWidget_2)

        self.horizontalWidget1 = QWidget(self.pageMateriel)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalWidget1.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridWidget_16 = QWidget(self.horizontalWidget1)
        self.gridWidget_16.setObjectName(u"gridWidget_16")
        self.gridWidget_16.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.gridLayout_mat0 = QGridLayout(self.gridWidget_16)
        self.gridLayout_mat0.setObjectName(u"gridLayout_mat0")

        self.horizontalLayout_2.addWidget(self.gridWidget_16)

        self.gridWidget_14 = QWidget(self.horizontalWidget1)
        self.gridWidget_14.setObjectName(u"gridWidget_14")
        self.gridWidget_14.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.gridLayout_mat2 = QGridLayout(self.gridWidget_14)
        self.gridLayout_mat2.setObjectName(u"gridLayout_mat2")

        self.horizontalLayout_2.addWidget(self.gridWidget_14)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_11.addWidget(self.horizontalWidget1)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 10)
        self.verticalLayout_11.setStretch(2, 3)
        self.conteneur_accueil.addWidget(self.pageMateriel)
        self.pageReseau = QWidget()
        self.pageReseau.setObjectName(u"pageReseau")
        self.verticalLayout_15 = QVBoxLayout(self.pageReseau)
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, 10, 15, 2)
        self.conteneur_titreParMenu_6 = QGroupBox(self.pageReseau)
        self.conteneur_titreParMenu_6.setObjectName(u"conteneur_titreParMenu_6")
        self.conteneur_titreParMenu_6.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.label_titreParMenu_6 = QLabel(self.conteneur_titreParMenu_6)
        self.label_titreParMenu_6.setObjectName(u"label_titreParMenu_6")
        self.label_titreParMenu_6.setGeometry(QRect(0, 0, 251, 18))
        self.label_titreParMenu_6.setFont(font)
        self.label_descriptionParMenu_6 = QLabel(self.conteneur_titreParMenu_6)
        self.label_descriptionParMenu_6.setObjectName(u"label_descriptionParMenu_6")
        self.label_descriptionParMenu_6.setGeometry(QRect(0, 20, 391, 18))

        self.verticalLayout_15.addWidget(self.conteneur_titreParMenu_6)

        self.gridWidget_3 = QWidget(self.pageReseau)
        self.gridWidget_3.setObjectName(u"gridWidget_3")
        self.gridWidget_3.setStyleSheet(u"background:transparent")
        self.horizontalLayout_6 = QHBoxLayout(self.gridWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 1, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_17 = QGroupBox(self.gridWidget_3)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_titreParMenu_9 = QLabel(self.groupBox_17)
        self.label_titreParMenu_9.setObjectName(u"label_titreParMenu_9")
        self.label_titreParMenu_9.setGeometry(QRect(10, 10, 251, 18))
        self.label_titreParMenu_9.setFont(font)
        self.gridLayoutWidget_12 = QWidget(self.groupBox_17)
        self.gridLayoutWidget_12.setObjectName(u"gridLayoutWidget_12")
        self.gridLayoutWidget_12.setGeometry(QRect(10, 30, 581, 201))
        self.grid_reseau_2 = QGridLayout(self.gridLayoutWidget_12)
        self.grid_reseau_2.setObjectName(u"grid_reseau_2")
        self.grid_reseau_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget_12)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.grid_reseau_2.addWidget(self.label_5, 0, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_24 = QLabel(self.gridLayoutWidget_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.grid_reseau_2.addWidget(self.label_24, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_25 = QLabel(self.gridLayoutWidget_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.grid_reseau_2.addWidget(self.label_25, 0, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_5.addWidget(self.groupBox_17)

        self.groupBox_16 = QGroupBox(self.gridWidget_3)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setStyleSheet(u"background: transparent;\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.groupBox_16)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.groupBox_14 = QGroupBox(self.gridWidget_3)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_titreParMenu_8 = QLabel(self.groupBox_14)
        self.label_titreParMenu_8.setObjectName(u"label_titreParMenu_8")
        self.label_titreParMenu_8.setGeometry(QRect(10, 10, 251, 18))
        self.label_titreParMenu_8.setFont(font)
        self.gridLayoutWidget_11 = QWidget(self.groupBox_14)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(10, 30, 381, 491))
        self.gridLayout_reseau2 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_reseau2.setObjectName(u"gridLayout_reseau2")
        self.gridLayout_reseau2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_6.addWidget(self.groupBox_14)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_15.addWidget(self.gridWidget_3)

        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 16)
        self.conteneur_accueil.addWidget(self.pageReseau)
        self.pageStockage = QWidget()
        self.pageStockage.setObjectName(u"pageStockage")
        self.verticalLayout_12 = QVBoxLayout(self.pageStockage)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 15, 10, 2)
        self.conteneur_titreParMenu_5 = QGroupBox(self.pageStockage)
        self.conteneur_titreParMenu_5.setObjectName(u"conteneur_titreParMenu_5")
        self.conteneur_titreParMenu_5.setStyleSheet(u"border:none;\n"
"background:transparent;")
        self.label_titreParMenu_5 = QLabel(self.conteneur_titreParMenu_5)
        self.label_titreParMenu_5.setObjectName(u"label_titreParMenu_5")
        self.label_titreParMenu_5.setGeometry(QRect(0, 0, 251, 18))
        self.label_titreParMenu_5.setFont(font)
        self.label_descriptionParMenu_5 = QLabel(self.conteneur_titreParMenu_5)
        self.label_descriptionParMenu_5.setObjectName(u"label_descriptionParMenu_5")
        self.label_descriptionParMenu_5.setGeometry(QRect(0, 20, 391, 18))

        self.verticalLayout_12.addWidget(self.conteneur_titreParMenu_5)

        self.groupBox_23 = QGroupBox(self.pageStockage)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setStyleSheet(u"background-color:#101E34;\n"
"color:#F0F5FF;\n"
"border-radius: 20px;")
        self.label_titreParMenu_10 = QLabel(self.groupBox_23)
        self.label_titreParMenu_10.setObjectName(u"label_titreParMenu_10")
        self.label_titreParMenu_10.setGeometry(QRect(10, 10, 251, 18))
        self.label_titreParMenu_10.setFont(font)
        self.gridLayoutWidget_13 = QWidget(self.groupBox_23)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 30, 1001, 221))
        self.gridLayout_fs_2 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_fs_2.setObjectName(u"gridLayout_fs_2")
        self.gridLayout_fs_2.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.gridLayoutWidget_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)

        self.gridLayout_fs_2.addWidget(self.label_26, 0, 2, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_13)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_fs_2.addWidget(self.label_27, 0, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.gridLayout_fs_2.addWidget(self.label_28, 0, 1, 1, 1)

        self.gridLayout_fs_2.setColumnStretch(0, 1)
        self.gridLayout_fs_2.setColumnStretch(2, 2)

        self.verticalLayout_12.addWidget(self.groupBox_23)

        self.verticalWidget_16 = QWidget(self.pageStockage)
        self.verticalWidget_16.setObjectName(u"verticalWidget_16")
        self.verticalWidget_16.setStyleSheet(u"background: transparent;\n"
"border: none;")
        self.verticalLayout_13 = QVBoxLayout(self.verticalWidget_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")

        self.verticalLayout_12.addWidget(self.verticalWidget_16)

        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 9)
        self.verticalLayout_12.setStretch(2, 4)
        self.conteneur_accueil.addWidget(self.pageStockage)

        self.horizontalLayout.addWidget(self.conteneur_accueil)

        self.horizontalLayout.setStretch(0, 2)

        self.verticalLayout_3.addWidget(self.horizontalWidget)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setStyleSheet(u"background-color:#070F1C;\n"
"color:#F0F5FF;\n"
"border:none;")
        self.bouton_fermer = QPushButton(self.groupBox_2)
        self.bouton_fermer.setObjectName(u"bouton_fermer")
        self.bouton_fermer.setGeometry(QRect(10, 3, 20, 20))
        icon6 = QIcon()
        icon6.addFile(u"icons/application(1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_fermer.setIcon(icon6)
        self.bouton_fermer.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 40)
        self.verticalLayout_3.setStretch(2, 2)
        self.horizontalWidget1.raise_()
        self.groupBox_2.raise_()
        self.titleBar.raise_()

        self.retranslateUi(Widget)

        self.conteneur_accueil.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.titre.setText(QCoreApplication.translate("Widget", u"SysInfo", None))
        self.description.setText(QCoreApplication.translate("Widget", u"R\u00e9cup\u00e9ration d'information syst\u00e8me", None))
        self.logo_linux.setText("")
        self.bouton_apercu.setText(QCoreApplication.translate("Widget", u" Aper\u00e7u", None))
        self.bouton_systeme.setText(QCoreApplication.translate("Widget", u" Syst\u00e8me", None))
        self.bouton_materiel.setText(QCoreApplication.translate("Widget", u" Mat\u00e9riel", None))
        self.bouton_reseau.setText(QCoreApplication.translate("Widget", u" R\u00e9seau", None))
        self.bouton_stockage.setText(QCoreApplication.translate("Widget", u" Stockage", None))
        self.bouton_processus.setText(QCoreApplication.translate("Widget", u" Ressource usage", None))
        self.conteneur_titreParMenu.setTitle("")
        self.label_titreParMenu.setText(QCoreApplication.translate("Widget", u"Aper\u00e7u du syst\u00e8me", None))
        self.label_descriptionParMenu.setText(QCoreApplication.translate("Widget", u"Information compl\u00e8tes sur votre serveur Linux", None))
        self.groupBox_4.setTitle("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Widget", u"Syst\u00e8me", None))
        self.groupBox_5.setTitle("")
        self.label_8.setText("")
        self.label_11.setText(QCoreApplication.translate("Widget", u"Processeur", None))
        self.groupBox_6.setTitle("")
        self.label_9.setText("")
        self.label_12.setText(QCoreApplication.translate("Widget", u"M\u00e9moire RAM", None))
        self.groupBox_7.setTitle("")
        self.label_10.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"Disque", None))
        self.groupBox_8.setTitle("")
        self.label_14.setText(QCoreApplication.translate("Widget", u"Information Syst\u00e8me", None))
        self.groupBox_9.setTitle("")
        self.label_15.setText(QCoreApplication.translate("Widget", u"Utilisation des ressources", None))
        self.groupBox_10.setTitle("")
        self.label_16.setText(QCoreApplication.translate("Widget", u"Interface r\u00e9seau", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"IP / Masque", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Interface", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u00c9tat", None))
        self.groupBox_11.setTitle("")
        self.label_17.setText(QCoreApplication.translate("Widget", u"Stockage", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Utilisation en %", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Syst\u00e8me de fichiers", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Utilis\u00e9 en (Mo ou Go)", None))
        self.groupBox_12.setTitle("")
        self.label_18.setText(QCoreApplication.translate("Widget", u"Information mat\u00e9rielles", None))
        self.conteneur_titreParMenu_2.setTitle("")
        self.label_titreParMenu_2.setText(QCoreApplication.translate("Widget", u"Informations syst\u00e8me d\u00e9taill\u00e9es", None))
        self.label_descriptionParMenu_2.setText(QCoreApplication.translate("Widget", u"D\u00e9tails complets sur le syst\u00e8me d'exploitation et le noyau", None))
        self.groupBox_13.setTitle("")
        self.label_titreParMenu_4.setText(QCoreApplication.translate("Widget", u"Informations de base", None))
        self.groupBox_15.setTitle("")
        self.label_titreParMenu_7.setText(QCoreApplication.translate("Widget", u"Environnement", None))
        self.conteneur_titreParMenu_3.setTitle("")
        self.label_titreParMenu_3.setText(QCoreApplication.translate("Widget", u"Informations mat\u00e9rielles", None))
        self.label_descriptionParMenu_3.setText(QCoreApplication.translate("Widget", u"D\u00e9tails complets du mat\u00e9riel de votre serveur", None))
        self.groupBox_20.setTitle("")
        self.label_37.setText(QCoreApplication.translate("Widget", u"Processeur", None))
        self.label_19.setText("")
        self.groupBox_21.setTitle("")
        self.label_38.setText(QCoreApplication.translate("Widget", u"M\u00e9moire RAM", None))
        self.label_21.setText("")
        self.groupBox_22.setTitle("")
        self.label_39.setText(QCoreApplication.translate("Widget", u"Disque", None))
        self.label_23.setText("")
        self.conteneur_titreParMenu_6.setTitle("")
        self.label_titreParMenu_6.setText(QCoreApplication.translate("Widget", u"Informations r\u00e9seau", None))
        self.label_descriptionParMenu_6.setText(QCoreApplication.translate("Widget", u"D\u00e9tail des interfaces et connexions r\u00e9seau", None))
        self.groupBox_17.setTitle("")
        self.label_titreParMenu_9.setText(QCoreApplication.translate("Widget", u"Inteface r\u00e9seau", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"IP / Masque", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"Interface", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"\u00c9tat", None))
        self.groupBox_16.setTitle("")
        self.groupBox_14.setTitle("")
        self.label_titreParMenu_8.setText(QCoreApplication.translate("Widget", u"Informations r\u00e9seau", None))
        self.conteneur_titreParMenu_5.setTitle("")
        self.label_titreParMenu_5.setText(QCoreApplication.translate("Widget", u"Informations de stockage", None))
        self.label_descriptionParMenu_5.setText(QCoreApplication.translate("Widget", u"D\u00e9tail des disques et syst\u00e8me de fichers", None))
        self.groupBox_23.setTitle("")
        self.label_titreParMenu_10.setText(QCoreApplication.translate("Widget", u"Syst\u00e8me de fichiers", None))
        self.label_26.setText(QCoreApplication.translate("Widget", u"Utilisation en %", None))
        self.label_27.setText(QCoreApplication.translate("Widget", u"Syst\u00e8me de fichiers", None))
        self.label_28.setText(QCoreApplication.translate("Widget", u"Utilis\u00e9 en (Mo ou Go)", None))
        self.groupBox_2.setTitle("")
        self.bouton_fermer.setText("")
    # retranslateUi

