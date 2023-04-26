import tkinter as tk
from threading import Thread


def get_color(num):
    if num == 0:
        return "blue"
    elif num == 1:
        return "red"
    elif num == 2:
        return "yellow"
    elif num == 3:
        return "black"
    elif num == 4:
        return "green"


def empty_data_for_array(n):
    my_array = []
    for i in range(n):
        my_row = []
        for j in range(n):
            my_row.append(0)
        my_array.append(my_row)
    return my_array


class GameUI:
    def __init__(self):
        self.size = 100
        self.players = 1

    def paint_canvas(self, fr, data_array):
        new_can = tk.Canvas(fr, width=1000, height=1000, bg="lightblue")
        n = self.size
        lng = 1000 / n
        for i in range(n):
            y = i * lng
            for j in range(n):
                x = j * lng
                new_can.create_rectangle(x, y, x + lng, y + lng, fill=get_color(data_array[i][j]))
        return new_can

    def draw_ui(self, init_size, run_check, run_simulation, ask_next_result, stop_simulation):
        self.size = init_size
        max_number_of_tribe = 4
        window = tk.Tk()
        frame_can = tk.Frame(master=window, bg="white")
        frame_can.pack(side=tk.LEFT)

        can = self.paint_canvas(frame_can, empty_data_for_array(self.size))
        can.pack(side=tk.LEFT)

        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5, bg="lightgreen")
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        label = tk.Label(master=frame, text="Settings", bg="green")
        label.pack()

        def increase():
            value = int(lbl_value["text"])
            if value < max_number_of_tribe:
                lbl_value["text"] = f"{value + 1}"
                self.players = value + 1

        def decrease():
            value = int(lbl_value["text"])
            if value > 1:
                lbl_value["text"] = f"{value - 1}"
                self.players = value - 1

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
                cann = self.paint_canvas(frame_can, empty_data_for_array(self.size))
                frame_can.winfo_children()[0].destroy()
                cann.pack()
                params = {
                    'size': self.size,
                    'players': self.players,
                    'init_cells': 50
                }
                run_simulation(params)
                print("Simulation started")
                thread_brain_follower = Thread(target=follow_brain)
                thread_brain_follower.start()
            else:
                print("Simulation has been already started")
                return

        def ask_stop_simulation(event):
            stop_simulation()

        def follow_brain():
            while True:
                if run_check():
                    result = ask_next_result()
                    cann = self.paint_canvas(frame_can, result)
                    frame_can.winfo_children()[0].destroy()
                    cann.pack()
                else:
                    print('End of Simulation')
                    break

        button = tk.Button(master=frame, borderwidth=5, text="Start Simulation", bg="red")
        button.pack(expand=False)
        button.bind("<Button-1>", start_simulation)

        button_stop = tk.Button(master=frame, borderwidth=5, text="Stop Simulation", bg="pink")
        button_stop.pack(expand=False)
        button_stop.bind("<Button-1>", ask_stop_simulation)

        window.mainloop()
