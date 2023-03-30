import tkinter as tk


def write_me():
    print("helo")


def life_and_death(call_me):
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
        call_me()

    button = tk.Button(master=frame, borderwidth=5, text="Start Simulation", bg="red")
    button.pack(expand=False)
    button.bind("<Button-1>", start_simulation)

    window.mainloop()


life_and_death(write_me)


# 1, A tkinter-es szervíznek átadok 3 fv-t amit tud hívni:
# - megkérdi, hogy fut e még -> ha nem fut, akkor el lehet indítani
# - elindítja és átad egy map-ban paramétereket (pl. tábla mérete, tribe-ok száma)
# - kér vissza egy tömböt, ami alapján tudja a Canvas-t újra rajzolni
#
# 2, a tkinter külön modulban legyen
#
# 3, az egy külön modulban legyen
