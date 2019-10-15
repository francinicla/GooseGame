import random
import time
from tkinter import *
from tkinter import messagebox  # to activate messages


class Menub:
    """ Manage menu """

    def __init__(self, window):

        def mquit():
            m_exit = messagebox.askyesno(title="Quit", message='Are you sure?')
            if m_exit > 0:
                window.destroy()

        def maboutinfo():
            messagebox.showinfo(title="About", message="GIOCO DELL' OCA\n\nCreated by\n\nRoberto Francini")

        """ Create conf windows menu """

        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='Exit', command=mquit)
        players = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Players", menu=players, state=NORMAL)
        mplayers = Menu(players, tearoff=0)
        players.add_cascade(label="Players Numbers", menu=mplayers)
        mplayers.add_radiobutton(label="2 Players", command=lambda: name(2))
        mplayers.add_radiobutton(label="3 Players", command=lambda: name(3))
        mplayers.add_radiobutton(label="4 Players", command=lambda: name(4))
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About', command=maboutinfo)
        menubar.add_cascade(label='About', menu=helpmenu)
        window.config(menu=menubar)


class Dice:

    def __init__(self, value):
        self.value = value
        self.img = PhotoImage(file="images/{}.png".format(value))


def name(number):

    """ Choice players number """
    if Board.game_active != 0:
        Board.mylist.insert(END, "Non puoi cambiare il numero", "dei giocatori con il gioco in corso")

    else:
        Board.giocatori = []
        Board.n_players = number
        Board.giocatori += ["Pippo", 0, 100],
        print(Board.giocatori)
        Board.giocatori += ["Pluto", 0, 200],
        Label(Board.bconf, text=Board.giocatori[0][0], bg='white', font="Helvetica 12 bold", width=10)\
            .grid(row=2, column=2, padx=5)
        Label(Board.bconf, text=Board.giocatori[1][0], bg='white', font="Helvetica 12 bold", width=10)\
            .grid(row=3, column=2, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=4, column=2, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=5, column=2, padx=5)
        Label(Board.bconf, image=Board.red).grid(row=2, column=3)
        Label(Board.bconf, image=Board.yellow).grid(row=3, column=3)
        Label(Board.bconf, text="    ", bg='green').grid(row=4, column=3)
        Label(Board.bconf, text="    ", bg='green').grid(row=5, column=3)
        Label(Board.bconf, text=Board.giocatori[0][2], bg='white', font="Helvetica 12 bold", width=10)\
            .grid(row=2, column=4, padx=5)
        Label(Board.bconf, text=Board.giocatori[1][2], bg='white', font="Helvetica 12 bold", width=10)\
            .grid(row=3, column=4, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=4, column=4, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=5, column=4, padx=5)
        Board.player_list = ["Pippo", "Pluto"]

        if number > 2:
            Board.giocatori += ["Paperino", 0, 300],
            Label(Board.bconf, text=Board.giocatori[2][0], bg='white', font="Helvetica 12 bold", width=10)\
                .grid(row=4, column=2, padx=5)
            Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=5, column=2, padx=5)
            Label(Board.bconf, image=Board.blue).grid(row=4, column=3)
            Label(Board.bconf, text="    ", bg='green').grid(row=5, column=3)
            Label(Board.bconf, text=Board.giocatori[2][2], bg='white', font="Helvetica 12 bold", width=10)\
                .grid(row=4, column=4, padx=5)
            Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=5, column=4, padx=5)
            Board.n_players = number
            Board.player_list = ["Pippo", "Pluto", "Paperino"]
            if number == 4:
                Board.n_players = number
                Board.giocatori += ["Topolino", 0, 400],
                Label(Board.bconf, text=Board.giocatori[3][0], bg='white', font="Helvetica 12 bold", width=10)\
                    .grid(row=5, column=2, padx=5)
                Label(Board.bconf, image=Board.purple).grid(row=5, column=3)
                Label(Board.bconf, text=Board.giocatori[3][2], bg='white', font="Helvetica 12 bold", width=10)\
                    .grid(row=5, column=4, padx=5)
                Board.player_list = ["Pippo", "Pluto", "Paperino", "Topolino"]

        Board.mylist.insert(END, "Hai selezionato {} giocatori".format(Board.n_players))
        Board.mylist.insert(END, "Ora devi tirare il dado", "per scegliere chi comincia", "")

        Board.bconf.update()
        # gioco = Game()


class Board:
    """ Generate board """

    bconf = Tk()
    bconf.geometry('1595x870')
    # bconf.geometry("{0}x{1}+0+0".format(bconf.winfo_screenwidth(), bconf.winfo_screenheight()))
    bconf.configure(background='green', borderwidth=10)
    bconf.title("Gioco dell'oca")

    """ Handle dice and players """

    giocatori = []
    start = 1
    n_dice = 1
    n_players = 1
    player_list = []
    turn = 1
    game_active = 0
    arrow_pos = 2

    """ Handle graphic objects """

    oca = PhotoImage(file="images/giocodelloca.png")
    # oca = oca.subsample(3,3)
    red = PhotoImage(file="images/red1.gif")
    blue = PhotoImage(file="images/blue1.gif")
    yellow = PhotoImage(file="images/yellow1.gif")
    purple = PhotoImage(file="images/purple1.gif")

    """ Generate dice """

    dice1 = Dice(1)
    dice2 = Dice(0)
    print(dice1.value, dice2.value)

    """ Generate frame listbox """

    testo = Frame(bconf)
    scrollbar = Scrollbar(testo)
    scrollbar.grid(row=1, column=2, rowspan=22, sticky='ns')
    mylist = Listbox(testo, yscrollcommand=scrollbar.set, width=28, height=22)
    mylist.insert(END, "Welcome to the 'Gioco dell'oca'", "", "To start", "select the player from the menu", "")
    mylist.grid(row=1, column=1, rowspan=22)
    mylist.see("end")
    scrollbar.config(command=mylist.yview)
    mylist.yview(END)
    testo.grid(row=9, column=2, rowspan=22, columnspan=4, padx=10)
    bconf.update()

    """Generation map relative boxes coordinate to first player (red) """
    map = [[1080, 560],
           [1085, 500], [1090, 445], [1085, 385], [1068, 332], [1045, 280], [1015, 230], [975, 180], [925, 140],
           [878, 108], [826, 81],
           [772, 61], [715, 45], [654, 32], [594, 30], [534, 32], [477, 45], [423, 61], [368, 81], [318, 108],
           [268, 137],
           [218, 175], [176, 219], [143, 270], [118, 328], [108, 385], [104, 445], [115, 506], [136, 565], [172, 618],
           [213, 668],
           [263, 704], [318, 732], [373, 754], [426, 765], [485, 782], [542, 785], [602, 783], [657, 773], [712, 759],
           [768, 740],
           [822, 721], [875, 689], [918, 648], [958, 595], [980, 535], [995, 475], [988, 414], [972, 353], [940, 295],
           [898, 248],
           [848, 212], [795, 186], [742, 162], [680, 146], [623, 138], [562, 136], [500, 150], [445, 166], [388, 185],
           [336, 217],
           [290, 253], [245, 295], [218, 355], [208, 420], [218, 486], [245, 548], [290, 595], [350, 630], [405, 655],
           [465, 670],
           [525, 680], [585, 680], [642, 670], [702, 655], [760, 640], [815, 607], [862, 556], [885, 485], [885, 419],
           [857, 360],
           [808, 310], [750, 275], [686, 255], [624, 245], [560, 245], [500, 260], [435, 285], [380, 315], [336, 368],
           [330, 470]]

    game_board = Canvas(bconf, width=1216, height=844, bg="white")
    sfondo = game_board.create_image(0, 0, image=oca, anchor=NW)

    def __init__(self):

        """ Handle window board """

        Menub(self.bconf)

        self.game_board.grid(row=1, column=1, rowspan=30)

        # sfondo = Label(game_board, image=self.oca).grid(row=1, column=1, rowspan=30)
        self.game_board.tag_lower(self.sfondo)
        Label(Board.bconf, text="Giocatori", bg='white', font="Helvetica 14 bold", width=9)\
            .grid(row=1, column=2, padx=10)
        Label(Board.bconf, text="Posta", bg='white', font="Helvetica 14 bold", width=9).grid(row=1, column=4, padx=10)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=2, column=2, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=3, column=2, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=4, column=2, padx=5)
        Label(Board.bconf, text="", bg='green', font="Helvetica 12 bold", width=10).grid(row=5, column=2, padx=5)
        Label(Board.bconf, text="    ", bg='green').grid(row=2, column=3)
        Label(Board.bconf, image=self.dice1.img).grid(row=7, column=2)
        Label(Board.bconf, image=self.dice2.img).grid(row=7, column=4)
        Button(Board.bconf, text="Tira i dadi", font="Helvetica 12 bold", width=10,
               command=lambda: RollDice()).grid(row=8, column=2, columnspan=3, padx=10, pady=20)
        Board.movearrow(Board, 1)
        self.bconf.mainloop()

    def movearrow(self, turn):

        self.narrow = PhotoImage(file="images/narrow.png")
        self.narrow = self.narrow.subsample(2, 2)
        self.arrow = PhotoImage(file="images/arrow.png")
        self.arrow = self.arrow.subsample(2, 2)

        if turn == 1:
            Label(Board.bconf, image=self.arrow).grid(row=2, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=3, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=4, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=5, column=5, padx=10, sticky=E)
        if turn == 2:
            Label(Board.bconf, image=self.narrow).grid(row=2, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.arrow).grid(row=3, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=4, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=5, column=5, padx=10, sticky=E)
        if turn == 3:
            Label(Board.bconf, image=self.narrow).grid(row=2, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=3, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.arrow).grid(row=4, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=5, column=5, padx=10, sticky=E)
        if turn == 4:
            Label(Board.bconf, image=self.narrow).grid(row=2, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=3, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.narrow).grid(row=4, column=5, padx=10, sticky=E)
            Label(Board.bconf, image=self.arrow).grid(row=5, column=5, padx=10, sticky=E)


class RollDice:

    def __init__(self):

        """Manage roll dice and position pawns"""

        super().__init__()

        roll_dice = Board.n_dice
        num_players = Board.n_players

        if num_players == 1:
            Board.mylist.insert(END, "NON Hai ancora selezionato i giocatori", "Selezionali dal menu in alto")
        else:
            if Board.start == 1:
                for i in range(5):
                    Board.dice1.valore = RollDice.roll_dice(Board, num_players, 2)
                    print("valore dado", Board.dice1.valore)
                    time.sleep(0.3)
                Board.game_active = 1
                Board.start = 0
                Board.n_dice = 2
                Board.turn = Board.dice1.valore
                Board.mylist.insert(END, "Parte il giocatore: " + Board.player_list[Board.turn - 1])
                Board.movearrow(Board, Board.dice1.valore)
                gioco = Game()
            else:
                if roll_dice == 1:
                    for i in range(5):
                        Board.dice1.valore = RollDice.roll_dice(Board.dice1, 6, 2)
                        print("valore dado", Board.dice1.valore)
                        time.sleep(0.3)
                    Board.mylist.insert(END, "Con il dado hai fatto: " + str(Board.dice1.valore))
                    Board.n_dice = 2

                else:
                    for i in range(5):
                        Board.dice1.valore = RollDice.roll_dice(Board.dice1, 6, 2)
                        Board.dice2.valore = RollDice.roll_dice(Board.dice2, 6, 4)
                        print("valore dadi", Board.dice1.valore, Board.dice2.valore)
                        time.sleep(0.3)
                    somma = Board.dice1.valore + Board.dice2.valore
                    Board.mylist.insert(END, "Con i dadi hai fatto: " + str(somma))
                    turno = Board.turn - 1
                    Game.move(somma, Board.turn , Board.giocatori[turno][1])
                    Board.turn += 1
                    if Board.turn > num_players:
                        Board.turn = 1
                    Board.movearrow(Board, Board.turn)


        print("Lista giocatori", Board.player_list)
        print("turno giocatore",Board.turn)
        print("tocca a:", Board.player_list[Board.turn - 1])

    def roll_dice(self, face, position):

        """ Roll dice event """

        print(face, position)
        dado_1 = random.randint(1, face)
        print(dado_1)
        self.dado1 = PhotoImage(file="images/{}.png".format(dado_1))
        # Label(Board.bconf, image=self.dice1.img).grid(row=7,column=2)
        Label(Board.bconf, image=self.dado1).grid(row=7, column=position)
        Board.bconf.update()
        return dado_1


class Game:

    red1 = Label(Board.bconf, image=Board.red)
    yellow1 = Label(Board.bconf, image=Board.yellow)
    blue1 = Label(Board.bconf, image=Board.blue)
    purple1 = Label(Board.bconf, image=Board.purple)

    def __init__(self):

        print(Board.giocatori[0])

        if Board.n_players > 1:

            redx = Board.map[Board.giocatori[0][1]][0]
            redy = Board.map[Board.giocatori[0][1]][1]
            yellowx = Board.map[Board.giocatori[1][1]][0]
            yellowy = Board.map[Board.giocatori[1][1]][1]
            Game.red1.place(x=redx, y=redy)
            Game.yellow1.place(x=yellowx + 20, y=yellowy)
            # Board.game_board.create_image(redx, redy, image=Board.red, anchor=NW)
            # Board.game_board.create_image(yellowx + 20, yellowy, image=Board.yellow, anchor= NW)

            if Board.n_players > 2:
                bluex = Board.map[Board.giocatori[2][1]][0]
                bluey = Board.map[Board.giocatori[2][1]][1]
                # Board.game_board.create_image(bluex, bluey + 17, image=Board.blue, anchor= NW)
                Game.blue1.place(x=bluex, y=bluey+17)
                print(bluex, bluey)

                if Board.n_players > 3:
                    purplex = Board.map[Board.giocatori[2][1]][0]
                    purpley = Board.map[Board.giocatori[2][1]][1]
                    # Board.game_board.create_image(purplex + 20, purpley + 17, image=Board.purple, anchor=NW)
                    Game.purple1.place(x=purplex+20, y=purpley+17)

        Board.bconf.update()

    def move(mosse, giocatore, zona):

        print("Giocata:", mosse, giocatore, zona)
        for i in range(mosse):
            zona += 1
            if giocatore == 1:
                Game.redx = Board.map[zona][0]
                Game.redy = Board.map[zona][1]
                Game.red1.place(x=Game.redx, y=Game.redy)
            elif giocatore == 2:
                Game.yellowx = Board.map[zona][0] + 20
                Game.yellowy = Board.map[zona][1]
                Game.yellow1.place(x=Game.yellowx, y=Game.yellowy)
            elif giocatore == 3:
                Game.bluex = Board.map[zona][0]
                Game.bluey = Board.map[zona][1] + 17
                Game.blue1.place(x=Game.bluex, y=Game.bluey)
            elif giocatore == 4:
                Game.purplex = Board.map[zona][0] + 20
                Game.purpley = Board.map[zona][1] + 17
                Game.purple1.place(x=Game.purplex, y=Game.purpley)
            Board.giocatori[giocatore - 1][1] += 1
            Board.bconf.update()
            time.sleep(0.6)


if __name__ == '__main__':
    board = Board()
