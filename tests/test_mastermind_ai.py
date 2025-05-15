import unittest
import mastermind_ai

class TestMastermindAI(unittest.TestCase):
    def test_toutes_pieces(self):
        pieces = mastermind_ai.toutes_pieces()
        self.assertEqual(len(pieces), 16)
        for p in pieces:
            self.assertEqual(len(p), 4)

    def test_coup_gagnant(self):
        plateau = [None]*16
        plateau[0:3] = ['BDEC', 'SLEC', 'BLFP']
        piece = 'SDFP'
        pos = mastermind_ai.coup_gagnant(plateau, piece)
        self.assertIn(pos, [3,4,5,6,7,8,9,10,11,12,13,14,15])

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

if __name__ == '__main__':
    unittest.main()
