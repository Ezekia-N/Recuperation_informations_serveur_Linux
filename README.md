# 🖥️ SysInfo — Récupération d'information système sur un serveur Linux

> Application graphique desktop permettant de visualiser en temps réel les informations système d'un serveur Linux, développée avec **Python 3** et **PySide6 (Qt 6)**.

![Aperçu de l'application](screenshot.jpg)

---

## 📋 Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Build & Déploiement](#build--déploiement)
- [Informations système affichées](#informations-système-affichées)

---

## Présentation

**SysInfo** est une application de bureau légère et intuitive conçue pour les administrateurs et utilisateurs Linux souhaitant surveiller leur serveur à travers une interface graphique claire. Elle regroupe en un seul endroit toutes les informations essentielles : système, matériel, réseau, stockage et utilisation des ressources.

---

## Fonctionnalités

L'application est organisée en **6 sections** accessibles via une barre de navigation latérale :

| Section | Description |
|---|---|
| **Aperçu** | Vue synthétique globale : OS, CPU, RAM, Disque |
| **Système** | Distribution, version du noyau, uptime, environnement, shell |
| **Matériel** | CPU, GPU, RAM totale, taille du disque, version BIOS |
| **Réseau** | Interfaces réseau, adresses IP/masque, état (UP/DOWN) |
| **Stockage** | Partitions montées, espace utilisé, pourcentage avec barre de progression |
| **Ressource usage** | Utilisation CPU et RAM en temps réel sous forme de graphique |

Un bouton **Actualiser** en bas de fenêtre permet de relire toutes les données système à la demande.

---

## Prérequis

- **OS** : Linux (Ubuntu 24.04 LTS recommandé)
- **Python** : 3.13 ou supérieur
- **PySide6** : framework Qt 6 pour Python

```bash
pip install PySide6
```

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/<utilisateur>/sysInfo.git
cd sysInfo/data_recuperation
```

2. Installer les dépendances Python :

```bash
pip install PySide6
```

3. Générer les fichiers UI et ressources :

```bash
make
```

---

## Utilisation

### Lancement direct

```bash
make
# ou
python3 src/python/widget.py
```

### Lancement manuel (sans Makefile)

```bash
# 1. Compiler l'interface Qt Designer
pyside6-uic form.ui -o src/python/ui_form.py

# 2. Compiler les ressources (icônes, images)
pyside6-rcc ressources/ressources.qrc -o src/python/ressources_rc.py

# 3. Lancer l'application
python3 src/python/widget.py
```

---

## Structure du projet

```
data_recuperation/
├── form.ui                   # Interface graphique (Qt Designer)
├── Makefile                  # Automatisation build & déploiement
├── ressources/
│   ├── ressources.qrc        # Déclaration des ressources Qt
│   └── images/               # Icônes et images de l'application
└── src/
    └── python/
        ├── widget.py          # Logique principale de l'application
        ├── ui_form.py         # Généré par pyside6-uic (ne pas éditer)
        └── ressources_rc.py   # Généré par pyside6-rcc (ne pas éditer)
```

### Rôle des fichiers clés

- **`widget.py`** — Point d'entrée principal. Contient la logique de lecture des informations système et la mise à jour de l'interface graphique.
- **`form.ui`** — Fichier XML décrivant la disposition des widgets Qt (créé avec Qt Designer / Qt Creator).
- **`ressources.qrc`** — Fichier de ressources Qt référençant les icônes et images embarquées dans l'application.
- **`Makefile`** — Orchestre les étapes de compilation et de déploiement.

---

## Build & Déploiement

### Compiler le projet

```bash
make
```

Cela exécute dans l'ordre :
1. `pyside6-uic form.ui` → génère `ui_form.py`
2. `pyside6-rcc ressources/ressources.qrc` → génère `ressources_rc.py`
3. Lance `widget.py`

### Générer un exécutable autonome

```bash
make deploier
```

Utilise **PyInstaller** pour créer un exécutable standalone (sans console, en fichier unique) :

```bash
pyinstaller --noconsole --onefile src/python/widget.py
```

L'exécutable sera disponible dans le dossier `dist/`.

---

## Informations système affichées

### Système
| Champ | Exemple |
|---|---|
| Nom d'hôte | HP Desktop Pro G2 |
| Distribution | Ubuntu 24.04.4 LTS |
| Version noyau | 6.17.0-35-generic |
| Architecture | x86_64 |
| Uptime | 1 hour, 7 minutes |
| Environnement | GNOME |
| Shell | /bin/bash |

### Matériel
| Composant | Exemple |
|---|---|
| CPU | Intel Core i3-8100 @ 3.60 GHz, 4 cœurs |
| GPU | Intel Corporation CoffeeLake-S GT2 (UHD Graphics) |
| RAM | 8 Go DDR4 |
| Disque | 553 Go |
| BIOS | F.05 |

### Réseau
Affiche pour chaque interface : nom, adresse IP/masque et état (UP / DOWN).

### Stockage
Affiche pour chaque partition montée : système de fichiers, espace utilisé (Mo/Go) et pourcentage d'utilisation avec barre de progression colorée.

---

## Environnement de développement

- **IDE** : Qt Creator 19.0.2
- **Interpréteur** : Python 3.13
- **Framework UI** : PySide6 (Qt 6)
- **Outils de compilation** : `pyside6-uic`, `pyside6-rcc`
- **Déploiement** : PyInstaller

---

*Projet développé sous Ubuntu 24.04.4 LTS — Noyau Linux 6.17, x86\_64*
