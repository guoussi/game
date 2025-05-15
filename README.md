
# Quarto Mastermind IA

Ce projet propose une IA Quarto ultra-puissante, conçue pour être imbattable contre la plupart des adversaires humains ou bots classiques.

## Fonctionnalités principales
- **Client asynchrone** pour communication avec un serveur Quarto (protocole JSON).
- **IA avancée** : stratégie minimax profondeur 2+, anticipation des menaces, jamais de coup perdant, priorisation du centre, etc.
- **Script de lancement** pour démarrer facilement l'IA.
- **Tests unitaires** pour garantir la robustesse de l'algorithme (couverture >80%).
- **README** et **.gitignore** propres.

## Lancer l'IA
1. Installez Python 3.10+ et les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Configurez le joueur dans `players.json`.
3. Lancez l'IA avec :
   ```bash
   python start_player.py
   ```

## Structure du projet
- `mastermind_client.py` : client asynchrone Quarto
- `mastermind_ai.py` : IA Quarto imbattable
- `core_protocol.py` : gestion du protocole JSON
- `run_mastermind.py` : script de lancement (exemple)
- `players.json` : configuration du joueur
- `tests/` : tests unitaires
- `.github/` : instructions Copilot
- `.gitignore`, `requirements.txt`, `README.md`

## Tests
Lancez tous les tests unitaires avec :
```bash
python -m unittest discover -v tests
```

## Licence
Projet original, toute ressemblance avec un autre projet serait fortuite.
