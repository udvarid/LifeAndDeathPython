import tkinter as tk
from time import sleep


class GameUI:
    def __init__(self):
        self.size = 100

    def draw_ui(self, init_size, run_check, run_simulation, ask_next_result):
        self.size = init_size
        max_number_of_tribe = 1
        n = self.size
        lng = 1000 / n
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
            if not run_check():
                params = []
                run_simulation(params)
                print("Simulation started")
            else:
                print("Simulation has been already started")
                return
            while True:
                sleep(1)
                if run_check():
                    result = ask_next_result()
                else:
                    break

        button = tk.Button(master=frame, borderwidth=5, text="Start Simulation", bg="red")
        button.pack(expand=False)
        button.bind("<Button-1>", start_simulation)

        window.mainloop()
