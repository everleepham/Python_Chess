import unittest
from Piece import *
from ChessBoard import Game


class PawnTest(unittest.TestCase):
    def test_first_row(self):
        p = Pawn("white", Position(1, 1), Game())
        pos = p.get_possible_moves()
        expected = [
            Position(1, 2),
            Position(1, 3)
        ]
        self.assertEqual(pos, expected)

    def test_last_row(self):
        p = Pawn("white", Position(1, 7), Game())
        pos = p.get_possible_moves()
        expected = []
        self.assertEqual(pos, expected)

    def test_white_destination(self):
        p1 = Pawn("white", Position(1, 1))
        p2 = Rook("white", Position(1, 2)) 
        g = Game()
        g.board[1][1] = p1
        g.board[2][1] = p2
        p1.g = g
        excepted = []
        self.assertEqual(p1.get_possible_moves(), excepted)

    def test_white_destination_2(self):
        p1 = Pawn("white", Position(1, 1))
        p2 = Rook("white", Position(1, 3)) 
        g = Game()
        g.board[1][1] = p1
        g.board[3][1] = p2
        p1.g = g
        excepted = [Position(1, 2)]
        self.assertEqual(p1.get_possible_moves(), excepted)

class RookTest(unittest.TestCase):
    def test_first_row(self):
        r = Rook("white", Position(0, 0), Game())
        pos = r.get_possible_moves()
        expected = [
            Position(1, 0),
            Position(2, 0),
            Position(3, 0),
            Position(4, 0),
            Position(5, 0),
            Position(6, 0),
            Position(7, 0)
        ]
        self.assertEqual(pos, expected)

    def test_last_row(self):
        r = Rook("white", Position(0, 7), Game())
        pos = r.get_possible_moves()
        expected = [
            Position(0, 6),
            Position(0, 5),
            Position(0, 4),
            Position(0, 3),
            Position(0, 2),
            Position(0, 1)
        ]
        self.assertEqual(pos, expected)

    


if __name__ == "__main__":
    unittest.main()