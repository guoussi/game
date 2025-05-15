

# Quarto Mastermind IA

> **Mise à jour : 15 mai 2025**

Ce projet propose une IA Quarto très performante, conçue pour être un adversaire redoutable, même face à des joueurs expérimentés ou d'autres intelligences artificielles.


## Fonctionnalités principales
- **Client asynchrone** : communication fluide avec un serveur Quarto via JSON.
- **IA avancée** : stratégie basée sur minimax (profondeur 2+), anticipation des pièges, aucun coup perdant, préférence pour le centre.
- **Script de lancement** : démarrage simple et rapide de l'IA.
- **Tests unitaires** : couverture sérieuse pour garantir la fiabilité.
- **Documentation claire** : README et .gitignore pour un projet bien organisé.


## Lancer l'IA
1. Prérequis : Python 3.10 ou supérieur.
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurer vos informations dans `players.json`.
4. Démarrer l'IA :
   ```bash
   python start_player.py
   ```


## Structure du projet
- `mastermind_client.py` : client de communication avec le serveur
- `mastermind_ai.py` : logique de l'IA Quarto
- `core_protocol.py` : gestion du protocole JSON
- `run_mastermind.py` : exemple de lancement
- `players.json` : configuration des joueurs
- `tests/` : tests unitaires
- `.gitignore`, `requirements.txt`, `README.md` : fichiers de gestion et documentation


## Lancer les tests
Pour vérifier le bon fonctionnement du projet :
```bash
python -m unittest discover -v tests
```


## Licence
Projet original, toute ressemblance avec un autre projet Quarto IA serait fortuite.
