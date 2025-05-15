import unittest
import mastermind_ai
import core_protocol


class TestMastermindAI(unittest.TestCase):
    def test_toutes_pieces(self):
        pieces = mastermind_ai.toutes_pieces()
        self.assertEqual(len(pieces), 16)
        for p in pieces:
            self.assertEqual(len(p), 4)

    def test_coup_gagnant_none(self):
        plateau = [None]*16
        piece = 'BDEC'
        pos = mastermind_ai.coup_gagnant(plateau, piece)
        self.assertIsNone(pos)

    def test_coup_gagnant_win(self):
        plateau = ['BDEC', 'BDEC', 'BDEC', None] + [None]*12
        piece = 'BDEC'
        pos = mastermind_ai.coup_gagnant(plateau, piece)
        self.assertEqual(pos, 3)

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

    def test_piece_dangereuse(self):
        plateau = ['BDEC', 'BDEC', 'BDEC', None] + [None]*12
        dispo = mastermind_ai.pieces_disponibles(plateau, None)
        dangereuses = mastermind_ai.piece_dangereuse(plateau, None, dispo)
        self.assertIn('BDEC', dangereuses)

    def test_minimax(self):
        plateau = [None]*16
        en_attente = 'BDEC'
        pos, piece = mastermind_ai.minimax(plateau, en_attente, profondeur=2)
        self.assertIn(pos, range(16))
        self.assertIn(piece, mastermind_ai.toutes_pieces())

class TestCoreProtocol(unittest.TestCase):
    def test_read_write_json(self):
        import asyncio, io
        class DummyWriter:
            def __init__(self):
                self.data = b''
            def write(self, b):
                self.data += b
            async def drain(self):
                pass
            def close(self):
                pass
            async def wait_closed(self):
                pass
        async def test():
            r, w = io.BytesIO(), DummyWriter()
            obj = {'a': 1, 'b': 'x'}
            await core_protocol.write_json(w, obj)
            r.write(w.data)
            r.seek(0)
            class DummyReader:
                def __init__(self, b):
                    self.b = b
                async def read(self, n):
                    return self.b.read(n)
            reader = DummyReader(r)
            res = await core_protocol.read_json(reader)
            assert res == obj
        asyncio.run(test())

if __name__ == '__main__':
    unittest.main()
