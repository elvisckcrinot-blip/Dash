# Dash
Tableau de bord logistique moderne (Dark Mode) pour le suivi des flux Port de Cotonou &lt;> GDIZ Glo-Djigbé.
#  Pilotage Logistique Bénin - Dashboard Tech

![Streamlit](https://shields.io)
![Python](https://shields.io)

##  Description
Cette application est un tableau de bord de pilotage logistique moderne en **Dark Mode**, conçu pour optimiser le suivi des flux de marchandises au Bénin. 

L'outil se concentre sur l'axe stratégique **Port Autonome de Cotonou (PAC)** ↔️ **Zone Industrielle de Glo-Djigbé (GDIZ)** ↔️ **Hinterland**.

###  Fonctionnalités clés :
- **Suivi des KPI en temps réel** : Performance globale, taux de service et occupation des stocks.
- **Monitoring GDIZ** : Analyse spécifique des flux d'entrée et de sortie de la zone de Glo-Djigbé.
- **Cartographie des flux** : Visualisation des axes de transport (Nord/Sud).
- **Gestion des Alertes** : Système de notifications pour les retards portuaires ou ruptures de stock.

##  Installation & Utilisation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com
   ```
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancer l'application :
   ```bash
   streamlit run app.py
   ```

##  Structure du Projet
- `app.py` : Interface utilisateur et mise en page.
- `models.py` : Logique de traitement des données (simulées ou API).
- `.streamlit/` : Configuration graphique (Thème Dark Mode).

---
**Développé pour la modernisation de la supply-chain béninoise.**
