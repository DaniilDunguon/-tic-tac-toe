from tkinter import *
import random
import webbrowser

root = Tk()
root.title('Крестики-нолики')
root.geometry("700x400")
root.resizable(False, False)
game_run = True
field = []
cross_count = 0
status = ""
def callbackHref1(event):
    webbrowser.open_new(r"https://ru.wikipedi"
                        r"a.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%"
                        r"D1%82%D0%B8%D0%BA%D0%B8-%D0%"
                        r"BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8")
def callbackHref2(event):
    webbrowser.open_new(r"https://ru.wikipedi"
                        r"a.org/wiki/%D0%9A%D1%80%D0%B5%D1%81%"
                        r"D1%82%D0%B8%D0%BA%D0%B8-%D0%"
                        r"BD%D0%BE%D0%BB%D0%B8%D0%BA%D0%B8")

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
grid = Frame(root)

label = Label(root, text='Крестики/нолики', font="Arial 15", foreground="#13459c")
label.place(x=95, y=50)
new_button = Button(root, text='Новая игра', command=new_game, width=24, height=2, font="Arial 12 bold")
new_button.place(x=50, y=200)

new_button = Button(root, text='Об игре', command=new_game, width=12, height=1, font="Arial 11", foreground="#232536")
new_button.place(x=185, y=150)
new_button.bind("<Button-1>", callbackHref2)
new_button = Button(root, text='Нашли ошибку?', command=new_game, width=12, height=1, font="Arial 11", foreground="#232536")
new_button.bind("<Button-1>", callbackHref1)
new_button.place(x=50, y=150)

for row in range(3):
    line = []

    for col in range(3):

        button = Button(grid, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew', columnspan=1,)

        line.append(button)
    field.append(line)

grid.place(x=375, y=50)
root.mainloop()