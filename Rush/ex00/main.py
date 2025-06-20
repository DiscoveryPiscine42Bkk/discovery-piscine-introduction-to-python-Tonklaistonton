#นำเข้าฟังก์ชัน checkmate จากโมดูลชื่อ checkmate
from checkmate import checkmate
#นิยามฟังก์ชันหลักชื่อ main ที่จะใช้ในการทำงานหลักของโปรแกรม
def main():
#นิยามตัวแปรชื่อ board ซึ่งเป็น string แบบหลายบรรทัด แทนกระดานหมากรุกขนาด 2x2
 board = """\
..
.K\
"""
 checkmate(board)
#ฟังก์ชัน main() ถูกรัน
if __name__ == "__main__":
 main()
 #ตัวหมากแต่ละตัวมีรูปแบบการเดินตามนี้
#Pawn (P):
#. . . . . . .
#. . . . . . .
#. . X . X . .
#. . . P . . .
#. . . . . . .
#. . . . . . .
#. . . . . . .
#Bishop (B):
#X . . . . . X
#. X . . . X .
#. . X . X . .
#. . . B . . .
#. . X . X . .
#. X . . . X .
#X . . . . . X
#Rook (R):
#. . . X . . .
#. . . X . . .
#. . . X . . .
#X X X R X X X
#. . . X . . .
#. . . X . . .
#. . . X . . .
#Queen (Q)
#X . . X . . X
#. X . X . X .
#. . X X X . .
#X X X Q X X X
#. . X X X . .
#. X . X . X .
#X . . X . . X
