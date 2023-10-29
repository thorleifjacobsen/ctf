from pwn import *
import os
from stockfish import Stockfish

# Download stockfish from: https://stockfishchess.org/download/ and place it in the same folder as this script.
stockfish = Stockfish(path="./stockfish/stockfish-ubuntu-x86-64-avx2", depth=32, parameters={"Threads": 4, "Minimum Thinking Time": 30, "Skill Level": 20})

# Establish the target
target = remote("46.9.42.114", 9999)

# Read until bottom of the initial board board:
rows = target.recvuntil(b"a   b   c   d   e   f   g   h\n").decode()
# Split by newline to easier access each row
rows = rows.split("\n")
# Filter out all who do not start with | which are the rows of the board.
rows = list(filter(lambda x: x.startswith("|"), rows))
# Remove the first | of each row
rows = list(map(lambda x: x[1:], rows))
# Loop through all rows and split by | and trim content
rows = [list(map(lambda x: x.strip(), row.split("|"))) for row in rows]
# Remove last element of each row as this is the row number. We know it starts with 8 and decrements.
rows = [row[:-1] for row in rows]
# Create a crude FEN string and feed stockfish to get started.
stockfish.set_fen_position("".join(rows[0])+"/pppppppp/8/8/8/8/PPPPPPPP/"+"".join(rows[7])+" w KQkq - 0 2")


keepLooping = True
while keepLooping:
    try:
        # Read his move
        target.recvuntil(b"My move: ")
        move = target.recvuntil(b"\n").decode().strip()
        stockfish.make_moves_from_current_position([move])

        # Print board
        target.recvuntil(b"Your move: ").decode()
        myMove = stockfish.get_best_move_time(4000)
        stockfish.make_moves_from_current_position([myMove])
        target.sendline(myMove.encode())
        
        os.system('cls||clear')
        print(stockfish.get_board_visual())
        print("His move: ", move)
        print("My move: ", myMove)

    except (socket.error, ConnectionResetError, EOFError) as e:
        # If it closes we just oupput the data in the buffer.
        # It is most likely a win or loose message.
        print(target.clean().decode())
        keepLooping = False