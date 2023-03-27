import tkinter as tk


def frame_all():
    border_effects = {
        "flat": tk.FLAT,
        "sunken": tk.SUNKEN,
        "raised": tk.RAISED,
        "groove": tk.GROOVE,
        "ridge": tk.RIDGE,
    }

    window = tk.Tk()

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.LEFT)
        label = tk.Label(master=frame, text=relief_name)
        label.pack()

    window.mainloop()


def frame_pack():
    window = tk.Tk()

    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

    frame2 = tk.Frame(master=window, width=100, bg="yellow")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    frame3 = tk.Frame(master=window, width=50, bg="blue")
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    window.mainloop()


def frame_place():
    window = tk.Tk()

    frame = tk.Frame(master=window, width=150, height=150)
    frame.pack()

    label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
    label1.place(x=0, y=0)

    label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
    label2.place(x=75, y=75)

    window.mainloop()


def frame_grid():
    window = tk.Tk()

    for i in range(5):
        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(5):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=frame, text=f"{i}-{j}")
            label.pack()

    window.mainloop()


def canvas():
    l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    n = 100  # this is the length of the list l
    lngt = 800 // n  # this is the dimension of the squares that I want

    fen = tk.Tk()
    fen.geometry("1200x800")

    # I would like to create a table of 4 rows on canvas
    # each row should contain 4 squares
    can = tk.Canvas(fen, width=450, height=400, bg="lightblue")
    can.pack(side=tk.LEFT)

    for i in range(n):
        y = i * lngt
        for j in range(n):
            x = j * lngt
            can.create_rectangle(x, y, x + lngt, y + lngt, fill="red")

    f = tk.Frame(fen, width=150, height=400, bg="lightcoral")
    f.pack(side=tk.LEFT)

    fen.mainloop()


canvas()
