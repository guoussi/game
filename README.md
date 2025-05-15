
# Quarto Mastermind IA

Ce projet c'est une IA Quarto super forte, genre vraiment difficile à battre, même pour les pros ou d'autres robots.

## Ce que le projet sait faire
- **Client asynchrone** : il parle avec un serveur Quarto (en JSON, c'est stylé).
- **IA trop balèze** : elle réfléchit à fond (minimax profondeur 2+), elle voit les pièges, elle ne fait jamais de move nul, elle aime le centre.
- **Script de lancement** : tu peux lancer l'IA facilement, pas besoin de galérer.
- **Tests unitaires** : pour vérifier que tout marche (on a testé plein de trucs, c'est sérieux).
- **README** et **.gitignore** : pour que le projet soit propre.

## Comment on lance l'IA ?
1. Faut Python 3.10 ou plus, et installer les trucs :
   ```bash
   pip install -r requirements.txt
   ```
2. Tu mets tes infos dans `players.json`.
3. Et tu démarres l'IA :
   ```bash
   python start_player.py
   ```

## C'est quoi tous ces fichiers ?
- `mastermind_client.py` : le client qui discute avec le serveur
- `mastermind_ai.py` : l'IA qui réfléchit trop
- `core_protocol.py` : pour gérer les messages JSON
- `run_mastermind.py` : un exemple pour lancer
- `players.json` : où tu mets ton pseudo et tout
- `tests/` : les tests pour voir si ça bug
- `.github/` : des trucs pour Copilot
- `.gitignore`, `requirements.txt`, `README.md` : pour que ce soit clean

## Tester si tout marche
Pour checker que tout fonctionne, lance :
```bash
python -m unittest discover -v tests
```

## Licence
Projet fait maison, si ça ressemble à un autre, c'est pas fait exprès.
