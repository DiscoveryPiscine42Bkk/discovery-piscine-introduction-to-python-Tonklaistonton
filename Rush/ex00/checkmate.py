def checkmate(board_str):
    board = [list(line) for line in board_str.strip().split('\n')]
    size = len(board)
    
    # Find King position
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    ki, kj = king_pos

    # Directions for Bishop/Queen (diagonals)
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Directions for Rook/Queen (straight)
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Pawn threats (assume enemy pawn moves from top to bottom)
    pawn_attacks = [(-1, -1), (-1, 1)]

    # Check for Pawns
    for di, dj in pawn_attacks:
        ni, nj = ki + di, kj + dj
        if 0 <= ni < size and 0 <= nj < size and board[ni][nj] == 'P':
            print("Success")
            return

    # Check for Bishop or Queen (diagonals)
    for di, dj in diag_dirs:
        ni, nj = ki + di, kj + dj
        while 0 <= ni < size and 0 <= nj < size:
            piece = board[ni][nj]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                else:
                    break
            ni += di
            nj += dj

    # Check for Rook or Queen (straight lines)
    for di, dj in straight_dirs:
        ni, nj = ki + di, kj + dj
        while 0 <= ni < size and 0 <= nj < size:
            piece = board[ni][nj]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                else:
                    break
            ni += di
            nj += dj

    # Not in check
    print("Fail")
