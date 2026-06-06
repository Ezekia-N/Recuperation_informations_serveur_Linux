import sys
from PySide6.QtWidgets import QApplication, QWidget, QButtonGroup, QLabel, QListWidget, QAbstractItemView, QSizePolicy, QProgressBar, QListWidgetItem
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from ui_form import Ui_Widget
import json
import subprocess
import psutil
import socket
import math
import ctypes
import os
import pyqtgraph as pg

class Information:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.output = subprocess.run([os.path.abspath(os.path.join(current_dir, "../bash/system_identity.sh"))], capture_output=True, text=True)
        self.systemID = json.loads(self.output.stdout)

        self.fs_json = subprocess.run([os.path.abspath(os.path.join(current_dir, "../bash/file_system.sh"))], text=True, capture_output=True)
        self.fs = json.loads(self.fs_json.stdout)

        # Chargement de la bibliothèque C partagée                  
        self.ram = ctypes.CDLL(os.path.abspath(os.path.join(current_dir, "../../lib/libram_usage.so")))
        self.cpu = ctypes.CDLL(os.path.abspath(os.path.join(current_dir, "../../lib/libcpu_usage.so")))

        self.ram.get_ram_usage.restype = ctypes.c_double
        self.cpu.get_cpu_usage.restype = ctypes.c_double

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Récuperation d'information système sur un serveur linux")

        self.info = Information()
        self.font_style = "font-family: Monospace; font-size: 10pt;"
        self.cpu_percent = 0.0
        self.ram_percent = 0.0

        self.paginationAccueil();

        self.information_systeme_detaille()

        self.systeme()
        self.processeur()
        self.ram()
        self.storage()
        self.reseau()
        self.sideBarVisibility()
        self.gestionSidebar()
        self.systeme_fichier()
        self.materiel()
        self.ressource_label()
        self.ressource_label_detail()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.ressource_usage)

    def information_systeme_detaille(self):
        self.sysInfo = {
            "Nom d'hôte" : self.info.systemID['MODEL'].strip(),
            "Distribution" : self.info.systemID['DISTRIBUTION'].strip(),
            "Nom du noyau" : self.info.systemID['KERNEL_NAME'].strip(),
            "Version noyau" : self.info.systemID['KERNEL_VERSION'].strip(),
            "Architecture" : self.info.systemID['ARCHITECTURE'].strip(),
            "Type de systeme" : self.info.systemID['TYPE'].strip(),
            "Date d'installation" : self.info.systemID["DATE_INSTA"].strip(),
            "Uptime" : self.info.systemID['UPTIME'].strip(),
            "Date et Heure" : self.info.systemID['DATE'].strip(),
            "Fuseau horaire": subprocess.run(["cat", "/etc/timezone"], text=True, capture_output=True) or "N/A"
        }

        self.env = {
            "Environnement" : self.info.systemID['DE'].strip(),
            "Shell" : self.info.systemID['SHELL'].strip(), 
            "Utilisateur courant" : self.info.systemID['USER'].strip(),
            "Repertoire personnel": self.info.systemID['HOME'].strip(),
            "Session bureau" : self.info.systemID['DESKTOP_SESSION'].strip(),
            "Repertoire courant" : self.info.systemID['PWD'].strip(),
            "Niveau d'execution" : self.info.systemID['RUNLEVEL'].strip(),
            "Langue" : self.info.systemID['LANG'].strip()
        }

        line = 0
        for key, value in self.sysInfo.items():
            self.ui.gridLayout_information_base.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_information_base.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1
        
        line = 0
        for key, value in self.env.items():
            self.ui.gridLayout_environnement.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_environnement.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1

    def paginationAccueil(self):
        self.page = {
                "apercu"    : 0,
                "systeme"   : 1,
                "materiel"  : 2,
                "reseau"    : 3,
                "stockage"  : 4,
                "ressource" : 5
        }
        self.ui.bouton_apercu.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["apercu"]))
        self.ui.bouton_systeme.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["systeme"]))
        self.ui.bouton_materiel.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["materiel"]))
        self.ui.bouton_reseau.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["reseau"]))
        self.ui.bouton_stockage.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["stockage"]))
        self.ui.bouton_ressource.clicked.connect(lambda: self.ui.conteneur_accueil.setCurrentIndex(self.page["ressource"]))
    
    def sideBarVisibility(self):
        sidebar = self.ui.sidebar
        self.ui.bouton_fermer.clicked.connect(
        lambda: sidebar.setVisible(False) if sidebar.isVisible() else sidebar.setVisible(True))

    def systeme(self):
        self.listSysInfo = QListWidget()
        self.listSysInfoL = QListWidget()

        self.listSysInfoL.setWordWrap(True)
        self.listSysInfo.setWordWrap(True)
        self.listSysInfo.setSelectionMode(QAbstractItemView.NoSelection)
        self.listSysInfoL.setSelectionMode(QAbstractItemView.NoSelection)
        self.listSysInfo.setFocusPolicy(Qt.NoFocus)
        self.listSysInfoL.setFocusPolicy(Qt.NoFocus)

        self.listSysInfo.addItem(self.info.systemID['DISTRIBUTION'])
        self.listSysInfo.addItem(f"Noyau {self.info.systemID['KERNEL_VERSION']}")
        self.listSysInfo.setFont(QFont("Monospace", 10))

        line = 0
        for key, value in self.sysInfo.items():
            if key in ["Nom d'hôte", "Distribution", "Version noyau", "Architecture", "Uptime"]:
                self.ui.gridLayout_system.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
                self.ui.gridLayout_system.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
                line += 1

        for key, value in self.env.items():
            if key in ["Environnement", "Shell"]:
                self.ui.gridLayout_system.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
                self.ui.gridLayout_system.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
                line += 1

        self.ui.layout_system.addWidget(self.listSysInfo)
        self.ui.layout_system.addStretch()

    def processeur(self):
        self.procInfo = {
            "Fabricant" : self.info.systemID["FABRICANT"].strip(),
            "Modèle" : self.info.systemID["MODELE"].strip(),
            "Architecture" : self.info.systemID["ARCHITECTURE_PROC"].strip(),
            "Nombre de sockets" : self.info.systemID["SOCKET_NUMBER"].strip(),
            "Nombre de coeurs physiques" : self.info.systemID["COEUR_PHYSIQUE"].strip(),
            "Nombre de threads" : self.info.systemID["THREAD_NUMBER"].strip(),
            "Fréquence actuelle" : self.info.systemID["FREQ_ACTUELLE"].strip(),
            "Fréquence maximale" : self.info.systemID["FREQ_MAX"].strip(),
            "Température CPU" : self.info.systemID["TEMPERATURE"].strip(),
            "Cache L1" : self.info.systemID["CL1"].strip(),
            "Cache L2" : self.info.systemID["CL2"].strip(),
            "Cache L3" : self.info.systemID["CL3"].strip()
        }

        line = 0
        for key, value in self.procInfo.items():
            if key in ["Modèle"]:
                continue
            self.ui.gridLayout_cpu.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_cpu.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1

        self.listProcInfo = QListWidget()
        self.listProcInfo.setWordWrap(True)
        self.listProcInfo.setSelectionMode(QAbstractItemView.NoSelection)
        self.listProcInfo.setFocusPolicy(Qt.NoFocus)
        self.listProcInfo.setFont(QFont("Monospace", 10))

        self.listProcInfo.addItem(self.procInfo["Modèle"])
        self.listProcInfo.addItem(f"{self.procInfo["Nombre de threads"]} coeur")
          
        self.ui.layout_processeur.addWidget(self.listProcInfo)
        self.ui.layout_processeur.addStretch()

    def ram(self):
        self.ram_total = float(self.info.systemID['RAM_TOTAL_M'].strip())
        self.ramInfo = {
            "Fabricant" : self.info.systemID["FAB_RAM"].strip(),
            "Type" : self.info.systemID["RAM_TYPE"].strip(),
            "Nombre de slots" : self.info.systemID["RAM_SLOT_NUMBER"].strip(),
            "Nombre de barrettes" : self.info.systemID["BAR_NUMBER"].strip(),
            "Capacité maximum" : self.info.systemID["RAM_MAX_CAPACITY"].strip(),
            "Mem Totale" : self.info.systemID["RAM_TOTAL"].strip(),
            "Mem Utilisée" : self.info.systemID["RAM_UTILISE"].strip(),
            "Mem Libre" : self.info.systemID["RAM_LIBRE"].strip(),
            "Buffers" : self.info.systemID["BUFFERS"].strip(),
            "Cache" : self.info.systemID["CACHE"].strip(),
            "Swap total" : self.info.systemID["SWAP_TOTAL"].strip(),
            "Swap utilisé" : self.info.systemID["SWAP_UTILISE"].strip(),
            "Fréquence" : self.info.systemID["FREQ_RAM"].strip()
        }

        line = 0
        for key, value in self.ramInfo.items():
            self.ui.gridLayout_ram.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_ram.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1

        self.RAMInfo = QLabel()
        bar = QProgressBar()
        label = QLabel()

        self.ram_pourcentage = self.info.ram.get_ram_usage()
        label.setText(f"<b>{self.ram_pourcentage:.2f}%</b> utilisé initial")

        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(self.ram_pourcentage)

        bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 10px;
                background-color: #E0E0E0;     
                text-align: center;             
                color: #101E34;                 
                font-weight: bold;
                height:1px;
            }

            QProgressBar::chunk {
                background-color: green;      
                border-radius: 10px;          
            }
        """)

        self.RAMInfo.setText(f"{self.info.systemID['RAM_UTILISE'].strip().replace('i', 'B')} / {self.info.systemID['RAM_TOTAL'].strip().replace('i', 'B')}")
        self.RAMInfo.setFont(QFont("Inter", 10))

        self.ui.layout_ram.addWidget(self.RAMInfo)
        self.ui.layout_ram.addWidget(bar)
        self.ui.layout_ram.addWidget(label)
        self.ui.layout_ram.addStretch()

    def gestionSidebar(self):
        self.groupe_boutons = QButtonGroup(self)
        self.groupe_boutons.setExclusive(True)

        self.groupe_boutons.addButton(self.ui.bouton_apercu)
        self.groupe_boutons.addButton(self.ui.bouton_systeme)
        self.groupe_boutons.addButton(self.ui.bouton_materiel)
        self.groupe_boutons.addButton(self.ui.bouton_reseau)
        self.groupe_boutons.addButton(self.ui.bouton_stockage)
        self.groupe_boutons.addButton(self.ui.bouton_ressource)

        stylesheet_bouton = """
                QPushButton
                {
                        background:transparent;
                        width: 100%;
                        padding: 7px 0px 7px 10px;
                        border-radius: 8px;
                        text-align: left;
                }
                QPushButton:hover
                {
                        background-color: rgb(26, 95, 180);
                }
                QPushButton:pressed
                {
                        font-weight:bold;
                }
                QPushButton:checked
                {
                        background-color: rgb(26, 95, 180);
                        font-weight:bold;
                }
        """
        self.ui.bouton_apercu.setChecked(True)

        for bouton in self.groupe_boutons.buttons():
            bouton.setCheckable(True)
            bouton.setStyleSheet(stylesheet_bouton)

    def storage(self):
        self.stockage = {
            "Taille globale totale": self.info.systemID["DISK_TOTAL"].strip(),
            "Espace global utilise": self.info.systemID["DISK_UTILISE"].strip(),
            "Nom disque": self.info.systemID["DISK_NAME"].strip(),
            "Type SSD/HDD/NVMe": self.info.systemID["DISK_TYPE"].strip(),
            "Taille": self.info.systemID["DISK_SIZE"].strip(),
            "Temperature": self.info.systemID["DISK_TEMPERATURE"].strip(),
            "Numero serie": self.info.systemID["DISK_SERIAL"].strip(),
            "Interface SATA/NVMe": self.info.systemID["DISK_INTERFACE"].strip(),
            "Point de montage": self.info.systemID["MOUNT_POINT"].strip(),
            "Systeme de fichiers": self.info.systemID["FILE_SYSTEM"].strip(),
            "Taille partition": self.info.systemID["PARTITION_SIZE"].strip(),
            "Utilisation": self.info.systemID["PARTITION_USAGE"].strip(),
        }

        line = 0
        for key, value in self.stockage.items():
            self.ui.gridLayout_disque.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_disque.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1        

        self.diskInfo = QLabel()
        bar = QProgressBar()
        label = QLabel()

        diskTotal = float(self.info.systemID['DISK_TOTAL'].strip().replace("G", ""))
        diskUtilise = float(self.info.systemID['DISK_UTILISE'].strip().replace("G", ""))
        disk_pourcentage = (diskUtilise/diskTotal) * 100
        label.setText(f"<b>{disk_pourcentage:.2f}%</b> utilisé")

        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(disk_pourcentage)

        bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 10px;
                background-color: #E0E0E0;    
                text-align: center;             
                color: #101E34;            
                font-weight: bold;
                height: 2px;
            }

            QProgressBar::chunk {
                background-color: yellow;  
                border-radius: 10px;        
            }
        """)

        self.diskInfo.setText(f"{self.info.systemID['DISK_UTILISE'].strip()} / {self.info.systemID['DISK_TOTAL'].strip()}")
        self.diskInfo.setFont(QFont("Inter", 10))
        self.ui.layout_fs.addWidget(self.diskInfo)
        self.ui.layout_fs.addWidget(bar)
        self.ui.layout_fs.addWidget(label)
        self.ui.layout_fs.addStretch()

    def reseau(self):
        self.network = {
            "Nom interface": self.info.systemID["NET_NAME"].strip(),
            "Adresse IPv4": self.info.systemID["NET_IPV4"].strip(),
            "Adresse IPv6": self.info.systemID["NET_IPV6"].strip(),
            "Ip public" : self.info.systemID["PUBLICIP"].strip(),
            "MAC Address": self.info.systemID["NET_MAC"].strip(),
            "MTU": self.info.systemID["NET_MTU"].strip(),
            "Etat UP/DOWN": self.info.systemID["NET_STATE"].strip(),
            "Gateway": self.info.systemID["NET_GATEWAY"].strip(),
            "DNS": self.info.systemID["NET_DNS"].strip(),
            "DHCP ou Statique": self.info.systemID["NET_IP_ASSIGN"].strip(),
            "Octets envoyes": self.info.systemID["NET_TX_BYTES"].strip(),
            "Octets recus": self.info.systemID["NET_RX_BYTES"].strip(),
            "Debit descendant": self.info.systemID["NET_SPEED_DOWN"].strip(),
            "Debit ascendant": self.info.systemID["NET_SPEED_UP"].strip(),
        }

        line = 0
        for key, value in self.network.items():
            self.ui.gridLayout_reseau2.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_reseau2.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1    

        stats = psutil.net_if_stats()
        address = psutil.net_if_addrs()

        line = 1
        container = self.ui.grid_reseau
        container1 = self.ui.grid_reseau_2
        mono_font = QFont("Monospace", 10)

        for interface, ip in address.items():
            stat_info = stats.get(interface)
            
            if stat_info:
                isUp = "UP" if stat_info.isup else "DOWN"
            else:
                isUp = "UNKNOWN"
            
            ipV4 = "Pas d'adresse"
            for addr in ip:
                if addr.family == socket.AF_INET:
                    ipV4 = addr.address
                    break
                    
            Linterface = QLabel(interface)
            Lip = QLabel(ipV4)
            Lstate = QLabel(isUp)
            
            Linterface.setFont(mono_font)
            Lip.setFont(mono_font)
            Lstate.setFont(mono_font)
            
            container.addWidget(Linterface, line, 0)
            container.addWidget(Lip, line, 1)
            container.addWidget(Lstate, line, 2)
            
            Linterface2 = QLabel(interface)
            Lip2 = QLabel(ipV4)
            Lstate2 = QLabel(isUp)
            
            Linterface2.setFont(mono_font)
            Lip2.setFont(mono_font)
            Lstate2.setFont(mono_font)
            
            container1.addWidget(Linterface2, line, 0)
            container1.addWidget(Lip2, line, 1)
            container1.addWidget(Lstate2, line, 2)
            
            line += 1

    def systeme_fichier(self):
        self.fs_dict = {key: {} for key in reversed(self.info.fs.keys())}

        for key, value in self.info.fs.items():
            if not value == "":
                self.fs_dict[key]["used"] = float(value.split(",")[0])
                self.fs_dict[key]["percent"] = float(value.split(",")[1])

        line = 1
        for key, value in self.fs_dict.items():
            if key in ["/", "/home", "/var", "/usr"]:
                taille = value["used"]
                if taille > 1024:
                    taille_string = f"{taille/1024:.2f} Go"
                else:
                    taille_string = f"{taille} Mo"

                bar = QProgressBar()
                bar1 = QProgressBar()
                bar.setMinimum(0)
                bar1.setMinimum(0)
                bar.setMaximum(100)
                bar1.setMaximum(100)
                bar.setValue(value["percent"])
                bar1.setValue(value["percent"])

                couleur = ""
                if (value["percent"] <= 31):
                    couleur = "green"
                elif value["percent"] >= 80:
                    couleur = "red"
                else:
                    couleur = "yellow"
                
                bar.setStyleSheet(f"""
                    QProgressBar {{
                        border: none;
                        border-radius: 10px;           
                        background-color: #E0E0E0;    
                        text-align: center;             
                        color: #101E34;            
                        font-weight: bold;
                        height: 2px;
                    }}

                    QProgressBar::chunk {{
                        background-color: {couleur};  
                        border-radius: 10px;        
                    }}
                """)

                bar1.setStyleSheet(f"""
                    QProgressBar {{
                        border: none;
                        border-radius: 10px;           
                        background-color: #E0E0E0;    
                        text-align: center;             
                        color: #101E34;            
                        font-weight: bold;
                        height: 2px;
                    }}

                    QProgressBar::chunk {{
                        background-color: {couleur};  
                        border-radius: 10px;        
                    }}
                """)

                self.ui.gridLayout_fs.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
                self.ui.gridLayout_fs.addWidget(QLabel(taille_string, styleSheet=self.font_style), line, 1)
                self.ui.gridLayout_fs.addWidget(bar, line, 2)

                self.ui.gridLayout_fs_2.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
                self.ui.gridLayout_fs_2.addWidget(QLabel(taille_string, styleSheet=self.font_style), line, 1)
                self.ui.gridLayout_fs_2.addWidget(bar1, line, 2)

                line += 1

    def ressource_usage(self):
        self.cpu_percent = self.info.cpu.get_cpu_usage()
        self.ram_percent = self.info.ram.get_ram_usage()

        self.cpu_value_label.setText(f"{self.cpu_percent:.2f}%")
        self.ram_value_label.setText(f"{self.ram_percent:.2f}%")
      
        self.cpu_history.pop(0)     
        self.cpu_history.append(self.cpu_percent) 

        self.ram_history.pop(0)        
        self.ram_history.append(self.ram_percent) 

        self.cpu_curve.setData(self.cpu_history)
        self.ram_curve.setData(self.ram_history)

    def ressource_label_detail(self):
        self.graphe = pg.PlotWidget()
        self.graphe.setBackground(None)
        self.graphe.setYRange(0, 100)
        self.graphe.showGrid(x=True, y=True)
        self.graphe.addLegend(offset=(10, 10), labelTextColor='w')
        self.ui.groupBox_ressource_layout.addWidget(self.graphe)

        self.courbe_cpu = self.graphe.plot(name="utilisation cpu", pen=pg.mkPen(color='orange', width=2))
        self.courbe_ram = self.graphe.plot(name="utilisation ram", pen=pg.mkPen(color='green', width=2))

        self.point_max = 30
        self.cpuHistory = [0.0] * self.point_max
        self.ramHistory = [0.0] * self.point_max

        self.timer_ressource_detail = QTimer(self)
        self.timer_ressource_detail.timeout.connect(self.ressource_detail)
        self.timer_ressource_detail.start(1000)

    def ressource_detail(self):
        self.cpuHistory.pop(0)     
        self.cpuHistory.append(self.cpu_percent) 

        self.ramHistory.pop(0)        
        self.ramHistory.append(self.ram_percent) 

        self.courbe_cpu.setData(self.cpuHistory)
        self.courbe_ram.setData(self.ramHistory)

    def ressource_label(self):
        self.ui.gridLayout_ressource.addWidget(QLabel("RAM", styleSheet=self.font_style), 1, 0)
        self.ui.gridLayout_ressource.addWidget(QLabel("CPU", styleSheet=self.font_style), 0, 0)

        self.cpu_value_label = QLabel("0.00%", styleSheet=self.font_style)
        self.ram_value_label = QLabel("0.00%", styleSheet=self.font_style)
        self.ui.gridLayout_ressource.addWidget(self.cpu_value_label, 0, 2)
        self.ui.gridLayout_ressource.addWidget(self.ram_value_label, 1, 2)

        self.cpu_graph = pg.PlotWidget()
        self.cpu_graph.setBackground(None)
        self.cpu_graph.hideAxis('left')
        self.cpu_graph.hideAxis('bottom')
        self.cpu_graph.setMenuEnabled(False)
        self.cpu_graph.setMouseEnabled(x=False, y=False)
        self.cpu_graph.setYRange(0, 100)
        self.ui.gridLayout_ressource.addWidget(self.cpu_graph, 0, 1)

        self.ram_graph = pg.PlotWidget()
        self.ram_graph.setBackground(None)
        self.ram_graph.hideAxis('left')
        self.ram_graph.hideAxis('bottom')
        self.ram_graph.setMenuEnabled(False)
        self.ram_graph.setMouseEnabled(x=False, y=False)
        self.ram_graph.setYRange(0, 100)
        self.ui.gridLayout_ressource.addWidget(self.ram_graph, 1, 1)

        self.cpu_curve = self.cpu_graph.plot(pen=pg.mkPen(color='orange', width=2))
        self.ram_curve = self.ram_graph.plot(pen=pg.mkPen(color='green', width=2)) 

        self.max_points = 30
        self.cpu_history = [0.0] * self.max_points
        self.ram_history = [0.0] * self.max_points

    def materiel(self):
        self.mat = {
            "Carte mere Fabricant": self.info.systemID["BOARD_VENDOR"].strip(),
            "Carte mere Modele": self.info.systemID["BOARD_NAME"].strip(),
            "Carte mere Version": self.info.systemID["BOARD_VERSION"].strip(),
            "BIOS Version": self.info.systemID["BIOS_VERSION"].strip(),
            "BIOS Date": self.info.systemID["BIOS_DATE"].strip(),
            "GPU": self.info.systemID["GPU_NAME"].strip(),
        }

        line = 0
        for key, value in self.mat.items():
            self.ui.gridLayout_mat0.addWidget(QLabel(f"{key}", styleSheet=self.font_style), line, 0)
            self.ui.gridLayout_mat0.addWidget(QLabel(f"{value}", styleSheet=self.font_style), line, 1)
            line += 1

        self.ui.gridLayout_materiel.setColumnStretch(1, 2)
        self.ui.gridLayout_materiel.addWidget(QLabel("CPU", styleSheet=self.font_style), 0, 0)
        self.ui.gridLayout_materiel.addWidget(QLabel(self.info.systemID["CPU"].strip(), styleSheet=self.font_style), 0, 1)
        self.ui.gridLayout_materiel.addWidget(QLabel("GPU", styleSheet=self.font_style), 1, 0)
        self.ui.gridLayout_materiel.addWidget(QLabel(self.info.systemID["GPU"].strip(), styleSheet=self.font_style), 1, 1)
        self.ui.gridLayout_materiel.addWidget(QLabel("RAM", styleSheet=self.font_style), 2, 0)
        self.ui.gridLayout_materiel.addWidget(QLabel(f"{round(self.ram_total/1024)} Go {self.info.systemID["RAM_TYPE"].strip()}", styleSheet=self.font_style), 2, 1)
        self.ui.gridLayout_materiel.addWidget(QLabel("DISK", styleSheet=self.font_style), 3, 0)
        self.ui.gridLayout_materiel.addWidget(QLabel(self.info.systemID["DISK_TOTAL"].strip().replace("G", " Go"), styleSheet=self.font_style), 3, 1)
        self.ui.gridLayout_materiel.addWidget(QLabel("BIOS", styleSheet=self.font_style), 4, 0)
        self.ui.gridLayout_materiel.addWidget(QLabel(self.info.systemID["BIOS_VERSION"].strip(), styleSheet=self.font_style), 4, 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
