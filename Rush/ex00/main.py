from checkmate import checkmate
def main():
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            content = load_file(path)
            if content:
                checkmate(content)
            else:
                print("Error")
    else:
        # กระดาน default หากไม่ระบุ argument
        board = """\
R...
.K..
..P.
...."""
        checkmate(board)

if __name__ == "__main__":
    checkmate(
        "........",
        "...Q....",
        "........",
        "..K.....",
        "........",
        "........",
        "........",
        "........"
    )