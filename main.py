import time
import tkinter as tk
import matplotlib
from tkinter import messagebox, filedialog

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import algorithms

matplotlib.use('Agg')


class ClippingApp:

    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Clipping algorithms')
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.resizable(width=False, height=False)

        self.scale = range(0, 100)

        self.figure = plt.figure(figsize=(7, 7), dpi=100)
        plt.grid(linewidth=0.5, which='both', axis='both', color='gray', linestyle='--')
        plt.ylabel('y')
        plt.xlabel('x')

        # plt.xticks(np.arange(0, self.scale.stop + 10, 10))
        # plt.yticks(np.arange(0, self.scale.stop + 10, 10))
        plt.axis('equal')

        self.canvas = FigureCanvasTkAgg(self.figure)
        self.canvas.get_tk_widget().pack(side=tk.LEFT)

        self.options_frame = tk.Frame(self.master)
        self.options_frame.pack(side=tk.RIGHT, padx=10)

        self.scale_var = tk.IntVar(self.options_frame)
        self.scale_var.set(100)

        self.alg_var = tk.StringVar(value="l")

        radiobutton1 = tk.Radiobutton(self.options_frame, text="Liang Barsky", variable=self.alg_var,
                                      value="l")
        radiobutton1.select()
        radiobutton1.pack()

        tk.Radiobutton(self.options_frame, text='Sutherland Hodgman', variable=self.alg_var, value="c").pack()

        tk.Button(self.options_frame, text='Build', command=self.clip).pack()

        self.filepath = None

    def start(self):
        self.master.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.master.destroy()
            plt.close()

    def ask_file(self):
        self.filepath = filedialog.askopenfilename(initialdir='.', filetypes=[("Text files", "*.txt")])

    def clear_canvas(self):
        plt.clf()
        plt.grid(linewidth=0.5, which='both', axis='both', color='gray', linestyle='--')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.axis('equal')

    def parse_file1(self):
        with open(self.filepath, 'r') as file:
            data = file.read()
            split_data = data.split()
            num = int(split_data[0])
            del split_data[0]
            k = 0
            res = []
            for i in range(num):
                res.append(
                    [int(split_data[k]), int(split_data[k + 1]), int(split_data[k + 2]), int(split_data[k + 3])])
                k += 4
            res1 = [int(split_data[-4]), int(split_data[-3]), int(split_data[-2]), int(split_data[-1])]
            return res, res1

    def parse_file2(self):
        with open(self.filepath, 'r') as file:
            data = file.read()
            split_data = data.split()

            num = int(split_data[0])
            polygon = []
            clip_polygon = []
            k = 1
            for i in range(num):
                polygon.append([int(split_data[k]), int(split_data[k + 1])])
                k += 2

            num = int(split_data[k])
            k += 1
            for i in range(num):
                clip_polygon.append([int(split_data[k]), int(split_data[k + 1])])
                k += 2

            return polygon, clip_polygon

    def clip(self):
        if self.alg_var.get() == 'l':
            self.process_liang_barsky()
        else:
            self.process_sutherland_hodgman()

    def process_sutherland_hodgman(self):


        try:
            self.ask_file()
            if self.filepath == None or self.filepath == '':
                messagebox.showerror(message='file is not chosen', title='Error')
                return

            self.clear_canvas()
            polygon, clip_polygon = self.parse_file2()

            new_polygon = algorithms.sutherland_hodgman(polygon, clip_polygon)

            self.draw_polygon(polygon, 'blue', 2)
            self.draw_polygon(clip_polygon, 'black', 3)
            if new_polygon != None:
                self.draw_polygon(new_polygon, 'red', 4)

            plt.title('Sutherland Hodgman')
            self.canvas.draw()
        except:
            messagebox.showerror(message='file is wrong(2)', title='Error')

    def process_liang_barsky(self):
        try:
            self.ask_file()
            if self.filepath == None or self.filepath == '':
                messagebox.showerror(message='file is not chosen', title='Error')
                return

            self.clear_canvas()

            lines, clip_rectangle = self.parse_file1()
            new_lines = []
            for line in lines:
                new_lines.append(algorithms.liang_barsky(line[0],
                                                         line[1],
                                                         line[2],
                                                         line[3],
                                                         clip_rectangle[0],
                                                         clip_rectangle[1],
                                                         clip_rectangle[2],
                                                         clip_rectangle[3]))

            for line in lines:
                plt.plot([line[0], line[2]], [line[1], line[3]], color='blue', linewidth=2)

            for line in new_lines:
                if line != None:
                    plt.plot([line[0], line[2]], [line[1], line[3]], color='red', linewidth=4)

            self.draw_clip_rectangle(clip_rectangle[0], clip_rectangle[1], clip_rectangle[2], clip_rectangle[3])
            plt.title('Liang Barskiy')
            self.canvas.draw()

        except:
            messagebox.showerror(message='file is wrong(1)', title='Error')

    def draw_clip_rectangle(self, x_min, y_min, x_max, y_max):
        plt.plot([x_min, x_max], [y_min, y_min], color='black', linewidth=3)
        plt.plot([x_max, x_max], [y_min, y_max], color='black', linewidth=3)
        plt.plot([x_min, x_max], [y_max, y_max], color='black', linewidth=3)
        plt.plot([x_min, x_min], [y_min, y_max], color='black', linewidth=3)


    def draw_polygon(self, polygon, color, linewidth):
        for i in range(len(polygon) - 1):
            plt.plot([polygon[i][0], polygon[i+1][0]], [polygon[i][1], polygon[i+1][1]], color=color, linewidth=linewidth)
        plt.plot([polygon[-1][0], polygon[0][0]], [polygon[-1][1], polygon[0][1]], color=color, linewidth=linewidth)



if __name__ == "__main__":
    ClippingApp().start()

# pyinstaller --windowed -F --icon=clip.ico -d bootloader main.py --name clipping --onefile