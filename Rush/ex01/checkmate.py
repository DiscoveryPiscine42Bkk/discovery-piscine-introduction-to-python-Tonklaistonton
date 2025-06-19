def  checkmate(*rows):
        board = [list(row) for row in rows]
        pieces = {'K', 'Q', 'B', 'R', 'P'}
        piece_dirs = {
            'Q': [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (1,-1), (-1,1)],
            'R': [(-1,0), (1,0), (0,-1), (0,1)],
            'B': [(-1,-1), (1,1), (1,-1), (-1,1)],
        }
        # Find king
        king_pos = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos is not None:
                break
        if king_pos is None:
            print("Error: No King found")
            return
        kx, ky = king_pos
        # Check for Pawn ("P") attack
        for dx, dy in [(-1,-1), (-1,1)]:
            x, y = kx+dx, ky+dy
            if 0 <= x < n and 0 <= y < n and board[x][y] == 'P':
                print("Success")
                return
        # Check for all sliding pieces
        for piece, dirs in piece_dirs.items():
            for dx, dy in dirs:
                x, y = kx+dx, ky+dy
                while 0 <= x < n and 0 <= y < n:
                    c = board[x][y]
                    if c == '.':
                        x += dx
                        y += dy
                        continue
                    if c == piece or (piece == 'Q' and c in 'QR') or (piece == 'B' and c == 'Q') or (piece == 'R' and c == 'Q'):
                        print("Success")
                        return
                    break
        # Check for Knight ("N") attack
        for dx, dy in [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]:
            x, y = kx+dx, ky+dy
            if 0 <= x < n and 0 <= y < n and board[x][y] == 'N':
                print("Success")
                return
        print("Fail")