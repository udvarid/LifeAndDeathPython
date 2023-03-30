import tkinter as tk
from random import randint
from time import sleep


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


def button_example():
    def increase():
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value + 1}"

    def decrease():
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value - 1}"

    window = tk.Tk()

    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    btn_decrease = tk.Button(master=window, text="-", command=decrease)
    btn_decrease.grid(row=0, column=0, sticky="nsew")

    lbl_value = tk.Label(master=window, text="0")
    lbl_value.grid(row=0, column=1)

    btn_increase = tk.Button(master=window, text="+", command=increase)
    btn_increase.grid(row=0, column=2, sticky="nsew")

    window.mainloop()


def dice_example():
    def roll():
        lbl_result["text"] = str(randint(1, 6))

    window = tk.Tk()
    window.columnconfigure(0, minsize=150)
    window.rowconfigure([0, 1], minsize=50)

    btn_roll = tk.Button(text="Roll", command=roll)
    lbl_result = tk.Label()

    btn_roll.grid(row=0, column=0, sticky="nsew")
    lbl_result.grid(row=1, column=0)

    window.mainloop()


def canvas():
    n = 100  # this is the length of the list l
    lng = 1000 // n  # this is the dimension of the squares that I want

    fen = tk.Tk()
    fen.geometry("1200x800")

    can = tk.Canvas(fen, width=1200, height=1200, bg="lightblue")
    can.pack(side=tk.LEFT)

    button = tk.Button(text="Start Drawing")
    button.pack()

    for i in range(n):
        y = i * lng
        for j in range(n):
            x = j * lng
            can.create_rectangle(x, y, x + lng, y + lng, fill="blue")

    def start_drawing(event):
        for z in range(10):
            sleep(1 / 10)
            rnd_x = randint(0, n - 1) * lng
            rnd_y = randint(0, n - 1) * lng
            can.create_rectangle(rnd_x, rnd_y, rnd_x + lng, rnd_y + lng, fill="red")
            can.update()

    fen.bind("<Key>", start_drawing)
    button.bind("<Button-1>", start_drawing)

    fen.mainloop()


def life_and_death():
    max_number_of_tribe = 1
    n = 100
    lng = 10
    window = tk.Tk()
    can = tk.Canvas(window, width=1000, height=1000, bg="lightblue")
    can.pack(side=tk.LEFT)
    for i in range(n):
        y = i * lng
        for j in range(n):
            x = j * lng
            can.create_rectangle(x, y, x + lng, y + lng, fill="blue")

    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="lightgreen")
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    label = tk.Label(master=frame, text="Settings", bg="green")
    label.pack()

    def increase():
        value = int(lbl_value["text"])
        if value < max_number_of_tribe:
            lbl_value["text"] = f"{value + 1}"

    def decrease():
        value = int(lbl_value["text"])
        if value > 1:
            lbl_value["text"] = f"{value - 1}"

    frame_counter = tk.Frame(master=frame, relief=tk.GROOVE, borderwidth=5, bg="lightyellow")
    frame_counter.rowconfigure(1, minsize=50, weight=1)
    frame_counter.columnconfigure([0, 1, 2], minsize=50, weight=1)
    label_counter = tk.Label(master=frame_counter, text="Number of Tribes", bg="lightyellow")
    label_counter.grid(row=0, column=1)
    btn_decrease = tk.Button(master=frame_counter, text="-", command=decrease)
    btn_decrease.grid(row=1, column=0, sticky="nsew")

    lbl_value = tk.Label(master=frame_counter, text="1")
    lbl_value.grid(row=1, column=1)

    btn_increase = tk.Button(master=frame_counter, text="+", command=increase)
    btn_increase.grid(row=1, column=2, sticky="nsew")

    frame_counter.pack(expand=False)

    def start_simulation(event):
        value = int(lbl_value["text"])
        print(value)

    button = tk.Button(master=frame, borderwidth=5, text="Start Simulation", bg="red")
    button.pack(expand=False)
    button.bind("<Button-1>", start_simulation)

    window.mainloop()


life_and_death()


