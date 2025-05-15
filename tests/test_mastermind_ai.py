
# Tests unitaires complets pour mastermind_ai.py
import unittest
import mastermind_ai
import random

class TestMastermindAI(unittest.TestCase):
    def test_toutes_pieces(self):
        pieces = mastermind_ai.toutes_pieces()
        self.assertEqual(len(pieces), 16)
        self.assertEqual(len(set(pieces)), 16)
        for p in pieces:
            self.assertEqual(len(p), 4)

    def test_lignes_plateau(self):
        plateau = [f"BDEC" for _ in range(16)]
        lignes = mastermind_ai.lignes_plateau(plateau)
        self.assertEqual(len(lignes), 10)
        for l in lignes:
            self.assertEqual(len(l), 4)

    def test_meme_attribut(self):
        ligne = ['BDEC', 'BDEC', 'BDEC', 'BDEC']
        self.assertTrue(mastermind_ai.meme_attribut(ligne))
        ligne2 = ['BDEC', 'SDEC', 'BDEC', 'BDEC']
        self.assertTrue(mastermind_ai.meme_attribut(ligne2))
        ligne3 = ['BDEC', 'SLEC', 'BLFP', None]
        self.assertFalse(mastermind_ai.meme_attribut(ligne3))

    def test_victoire(self):
        plateau = [None]*16
        self.assertFalse(mastermind_ai.victoire(plateau))
        plateau[0:4] = ['BDEC', 'BDEC', 'BDEC', 'BDEC']
        self.assertTrue(mastermind_ai.victoire(plateau))

    def test_coups_possibles(self):
        plateau = [None]*16
        self.assertEqual(mastermind_ai.coups_possibles(plateau), list(range(16)))
        plateau[0] = 'BDEC'
        self.assertNotIn(0, mastermind_ai.coups_possibles(plateau))

    def test_pieces_disponibles(self):
        plateau = [None]*16
        dispo = mastermind_ai.pieces_disponibles(plateau, None)
        self.assertEqual(len(dispo), 16)
        plateau[0] = 'BDEC'
        dispo2 = mastermind_ai.pieces_disponibles(plateau, None)
        self.assertNotIn('BDEC', dispo2)

    def test_simule(self):
        plateau = [None]*16
        nouv = mastermind_ai.simule(plateau, 0, 'BDEC')
        self.assertEqual(nouv[0], 'BDEC')
        self.assertIsNot(plateau, nouv)

    def test_coup_gagnant(self):
        plateau = [None]*16
        plateau[0:3] = ['BDEC', 'BDEC', 'BDEC']
        piece = 'BDEC'
        pos = mastermind_ai.coup_gagnant(plateau, piece)
        self.assertIn(pos, [3])
        plateau = [None]*16
        piece = 'BDEC'
        pos = mastermind_ai.coup_gagnant(plateau, piece)
        self.assertIsNone(pos)

    def test_piece_dangereuse(self):
        plateau = [None]*16
        plateau[0:3] = ['BDEC', 'BDEC', 'BDEC']
        dispo = mastermind_ai.pieces_disponibles(plateau, None)
        dangereuses = mastermind_ai.piece_dangereuse(plateau, None, dispo)
        self.assertIsInstance(dangereuses, list)

    def test_minimax(self):
        plateau = [None]*16
        en_attente = 'BDEC'
        pos, piece = mastermind_ai.minimax(plateau, en_attente, profondeur=2)
        self.assertIn(pos, range(16))
        self.assertIn(piece, mastermind_ai.toutes_pieces())

    def test_choose_move_first(self):
        state = {'board': [None]*16, 'piece': None}
        move = mastermind_ai.choose_move(state)
        self.assertIsNone(move['pos'])
        self.assertIn(move['piece'], mastermind_ai.toutes_pieces())

    def test_choose_move_play(self):
        state = {'board': [None]*16, 'piece': 'BDEC'}
        move = mastermind_ai.choose_move(state)
        self.assertIn(move['pos'], range(16))
        self.assertEqual(len(move['piece']), 4)

    def test_choose_move_gagnant(self):
        plateau = [None]*16
        plateau[0:3] = ['BDEC', 'BDEC', 'BDEC']
        state = {'board': plateau, 'piece': 'BDEC'}
        move = mastermind_ai.choose_move(state)
        self.assertEqual(move['pos'], 3)

    def test_choose_move_erreur(self):
        # Cas limite : plateau plein
        plateau = ['BDEC']*16
        state = {'board': plateau, 'piece': 'BDEC'}
        try:
            move = mastermind_ai.choose_move(state)
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
