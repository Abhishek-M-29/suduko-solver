from tkinter import *

root = Tk()
root.title('SUDOKU')
root.geometry('415x325')

initial = dict.fromkeys([f'a{i}' for i in range(11, 100) if i % 10], 0)


def ButtonClick(r, c):
    if initial.get(f'a{r}{c}') > 8:
        k = initial[f'a{r}{c}'] = 0
    else:
        initial[f'a{r}{c}'] += 1
        k = initial[f'a{r}{c}']
    Button(root, text=str(k), padx=10, pady=5, borderwidth=3, command=lambda: ButtonClick(r, c),
           bg='light gray').grid(row=r - 1, column=c - 1)


def main():
    lis = list(initial.values())
    board = []
    for k in range(9):
        board.append(lis[k * 9:(k + 1) * 9])
    for g in board:
        for h in range(len(g)):
            g[h] = int(g[h])

    def findEmpty():
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return i, j  # row, column
        return None

    def valid(num, pos):
        row, column = pos
        # checking rows
        for i in range(len(board[0])):
            if board[row][i] == num:
                return False
        # checking columns
        for i in range(len(board)):
            if board[i][column] == num:
                return False

        # checking box
        startRowBox = row // 3
        startColumnBox = column // 3
        for i in range(startRowBox * 3, (startRowBox * 3) + 3):
            for j in range(startColumnBox * 3, (startColumnBox * 3) + 3):
                if board[i][j] == num:
                    return False
        return True

    def solve():  # Credit : medium.com
        find = findEmpty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if valid(i, find):
                board[row][col] = i

                if solve():
                    return True

                board[row][col] = 0
        return False

    solve()
    board = dict(zip([f'a{i}' for i in range(11, 100) if i % 10], ''.join([''.join(map(str, i)) for i in board])))
    return board


def enter():
    op = main()

    for key, value in op.items():

        if initial[key] != int(value):
            Button(root, text=value, padx=10, pady=5, borderwidth=3, bg='pink', fg='red').grid(row=int(key[-2]) - 1,
                                                                                               column=int(key[-1]) - 1)


'''
for i in range(1,10):
    for j in range(1,10):
        print(i,j)
        if ((1 <= i <= 3) or (7 <= i <= 9)) and ((1 <= j <= 3) or (7 <= j <= 9)):
            Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
                    command=lambda: ButtonClick(i, j)).grid(row=i - 1, column=j - 1)
        elif ((1 <= i <= 3) or (7 <= i <= 9)) and (4 <= j <= 7):
            Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
                    command=lambda: ButtonClick(i, j)).grid(row=i - 1, column=j - 1)
        elif (4 <= i <= 7) and ((1 <= j <= 3) or (7 <= j <= 9)):
            Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
                   command=lambda: ButtonClick(i, j)).grid(row=i - 1, column=j - 1)
        elif (4 <= i <= 7) and (4 <= j <= 7):
            Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
                   command=lambda: ButtonClick(i, j)).grid(row=i - 1, column=j - 1)
        else:
            exit(0)

'''



# Row1
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 1)).grid(row=0, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 2)).grid(row=0, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 3)).grid(row=0, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 4)).grid(row=0, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 5)).grid(row=0, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 6)).grid(row=0, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 7)).grid(row=0, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 8)).grid(row=0, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(1, 9)).grid(row=0, column=8)
# Row2
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 1)).grid(row=1, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5,
       command=lambda: ButtonClick(2, 2)).grid(row=1, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 3)).grid(row=1, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 4)).grid(row=1, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 5)).grid(row=1, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 6)).grid(row=1, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 7)).grid(row=1, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 8)).grid(row=1, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(2, 9)).grid(row=1, column=8)
# Row3
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 1)).grid(row=2, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 2)).grid(row=2, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 3)).grid(row=2, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 4)).grid(row=2, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 5)).grid(row=2, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 6)).grid(row=2, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 7)).grid(row=2, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 8)).grid(row=2, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(3, 9)).grid(row=2, column=8)
# Row4
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 1)).grid(row=3, column=0)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 2)).grid(row=3, column=1)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 3)).grid(row=3, column=2)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 4)).grid(row=3, column=3)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 5)).grid(row=3, column=4)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 6)).grid(row=3, column=5)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 7)).grid(row=3, column=6)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 8)).grid(row=3, column=7)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(4, 9)).grid(row=3, column=8)
# Row5
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 1)).grid(row=4, column=0)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 2)).grid(row=4, column=1)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 3)).grid(row=4, column=2)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 4)).grid(row=4, column=3)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 5)).grid(row=4, column=4)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 6)).grid(row=4, column=5)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 7)).grid(row=4, column=6)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 8)).grid(row=4, column=7)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(5, 9)).grid(row=4, column=8)
# Row6
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 1)).grid(row=5, column=0)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 2)).grid(row=5, column=1)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 3)).grid(row=5, column=2)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 4)).grid(row=5, column=3)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 5)).grid(row=5, column=4)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 6)).grid(row=5, column=5)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 7)).grid(row=5, column=6)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 8)).grid(row=5, column=7)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(6, 9)).grid(row=5, column=8)
# Row7
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 1)).grid(row=6, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 2)).grid(row=6, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 3)).grid(row=6, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 4)).grid(row=6, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 5)).grid(row=6, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 6)).grid(row=6, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 7)).grid(row=6, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 8)).grid(row=6, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(7, 9)).grid(row=6, column=8)
# Row8
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 1)).grid(row=7, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 2)).grid(row=7, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 3)).grid(row=7, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 4)).grid(row=7, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 5)).grid(row=7, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 6)).grid(row=7, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 7)).grid(row=7, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 8)).grid(row=7, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(8, 9)).grid(row=7, column=8)
# Row9
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 1)).grid(row=8, column=0)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 2)).grid(row=8, column=1)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 3)).grid(row=8, column=2)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 4)).grid(row=8, column=3)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 5)).grid(row=8, column=4)
Button(root, text='0', bg='light blue', fg='purple', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 6)).grid(row=8, column=5)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 7)).grid(row=8, column=6)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 8)).grid(row=8, column=7)
Button(root, text='0', bg='Orange', fg='Black', padx=10, pady=5, borderwidth=3,
       command=lambda: ButtonClick(9, 9)).grid(row=8, column=8)



    # Enter
Button(root, text='Enter', padx=20, pady=10, borderwidth=5, command=enter).grid(row=3, rowspan=3, column=11)

root.mainloop()
