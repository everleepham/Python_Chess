# import unittest
# from ChessBoard import Game

# class ChessBoardTest(unittest.TestCase):
#     def test_initial_board_setup(self):
#         chessboard = Game()

#         # Check if the board is initialized correctly
#         expected_board = "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n" \
#                         "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n" \
#                         "                \n" \
#                         "                \n" \
#                         "                \n" \
#                         "                \n" \
#                         "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n" \
#                         "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
#         self.assertEqual(chessboard.board, expected_board)

# if __name__ == '__main__':
#     unittest.main()
import unittest
from ChessBoard import Game

class ChessGameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_board_setup(self):
        expected_board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.assertEqual(self.game.board, expected_board)

    def test_print_board(self):
        expected_output = "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n" \
                        "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n" \
                        "                \n" \
                        "                \n" \
                        "                \n" \
                        "                \n" \
                        "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n" \
                        "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
        self.assertEqual(self.game.print(), expected_output)

if __name__ == '__main__':
    unittest.main()