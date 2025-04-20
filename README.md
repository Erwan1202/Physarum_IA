# Physarum_IA

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Work_in_Progress-yellow)

---

## 🧠 Description
Simulation inspirée du comportement du **Physarum Polycephalum**, un organisme unicellulaire célèbre pour sa capacité à explorer et optimiser ses trajets dans son environnement.

Ce projet modélise un Physarum se déplaçant sur une grille 2D, interagissant avec :
- des nutriments 🍎
- des obstacles 🧱
- des phéromones 🧪

---

## 📂 Structure du projet
/Environment/ 
Grid.py # Gestion de la grille et des cellules 
Diffusion.py # Diffusion des phéromones /Physarum/ 
Agent.py # Comportement d'un agent individuel 
Colony.py # Gestion de la colonie d'agents 
Simulation.py # Boucle principale de simulation 
Visualization.py # Affichage graphique de la grille et des agents 
config.py # Paramètres globaux 
README.md # Ce fichier

---

## 🎯 Objectif
Reproduire l'optimisation de chemins et l'adaptation dynamique d'un Physarum dans un environnement discret.

---

## ⚙️ Prérequis
- Python 3.8+
- Bibliothèques Python :
  - `numpy`
  - `matplotlib` (ou `pygame` pour la visualisation alternative)
  - `scipy` (optionnel pour réaction-diffusion)

---

## 🚀 Lancer la simulation
1. Installer les dépendances :
   ```bash
   pip install numpy matplotlib scipy
Exécuter la simulation :

bash
Copier
Modifier
python Simulation.py