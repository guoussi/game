# Quarto Mastermind AI

Ce projet propose une IA Quarto ultra-puissante, conçue pour être imbattable contre la plupart des adversaires humains ou bots classiques.

## Fonctionnalités principales
- **Client asynchrone** pour communication avec un serveur Quarto (protocole JSON).
- **IA avancée** : stratégie minimax profondeur 2+, anticipation des menaces, jamais de coup perdant, priorisation du centre, etc.
- **Script de lancement** pour démarrer facilement l'IA.
- **Tests unitaires** pour garantir la robustesse de l'algorithme.
- **README** et **.gitignore** propres.

## Lancer l'IA
1. Installez Python 3.10+ et les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Lancez l'IA en précisant les paramètres serveur :
   ```bash
   python mastermind_client.py --host <IP_SERVEUR> --port-server <PORT_SERVEUR> --port-client <PORT_CLIENT> --name <NOM_IA> --matricules <MATRICULE1> <MATRICULE2>
   ```

## Structure du projet
- `mastermind_client.py` : client asynchrone Quarto
- `mastermind_ai.py` : IA Quarto imbattable
- `run_mastermind.py` : script de lancement
- `tests/` : tests unitaires
- `.github/` : instructions Copilot
- `.gitignore`, `requirements.txt`, `README.md`

## Personnalisation
Vous pouvez modifier la stratégie IA dans `mastermind_ai.py` pour tester d'autres approches.

## Licence
Projet original, toute ressemblance avec un autre projet serait fortuite.
