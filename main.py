from ChessBoard import *

g = Game()

turn = "WHITE"
while True:
    print("Turn:", turn)
    # Check if the moves is valid
    try:
        src = input("   Enter the source position (x,y): ")
        dst = input("   Enter the destination position (x,y): ")
        src = Position(int(src[1]), int(src[3]))
        dst = Position(int(dst[1]), int(dst[3]))
        g.move_piece(src, dst)
    except Exception as e:
        print("Error:", e)
        continue

# Check if the moves is valid
    # piece = g.board[src.y][src.x]
    # g.move_piece(src, dst)

    g.print()

    if g.is_check():
        print("Check!")

    if g.is_checkmate():
        print("Checkmate!")
        break

    turn = "BLACK" if turn == "WHITE" else "WHITE"