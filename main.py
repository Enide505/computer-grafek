# from array import array
from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Style

unitSize = 18
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.canvas = Canvas(self.parent, width=800, height = 800)
        self.canvasWidth = self.canvas.winfo_screenwidth()
        self.canvasHeight = self.canvas.winfo_screenheight()

        self.parent.title("Window")
        self.pack(fill=BOTH, expand=1) #для центровки окна
        self.centerWindow()
        self.dx=0
        self.dy=0
        self.cx=0
        self.cy=0
        self.draw_axis(-6, 12, -6, 12)


        self.InitUI()


    def draw_axis(self, x_left, x_right, y_bottom, y_top):
        sw = self.parent.winfo_screenwidth()  # Ширина, высота экрана
        sh = self.parent.winfo_screenheight()

        # Блок оси и их масштаб
        # canvas = Canvas(self)

        # canvas.create_line(0, sh / 2, sw, sh / 2)
        # canvas.pack(fill=BOTH, expand=1)


        # canvas.create_line(sw / 2, 0, sw / 2, sh)
        self.canvas.pack(fill=BOTH, expand=1)
        # canvasWidth = self.canvas.winfo_screenwidth()
        # canvasHeight = self.canvas.winfo_screenheight()
        self.dx = self.canvasWidth / (x_right - x_left)
        self.dy = self.canvasHeight / (y_top - y_bottom)

        self.cx = -x_left * self.dx
        self.cy = y_top * self.dy

        self.canvas.create_line(0, self.cy, self.canvasWidth, self.cy, fill='black')
        self.canvas.create_line(self.cx, 0, self.cx, self.canvasHeight, fill='black')

        x_step = (x_right - x_left) / 18
        x = x_left
        while x <= x_right:
            x_canvas = (x - x_left) * self.dx
            self.canvas.create_line(x_canvas, self.cy - 3, x_canvas, self.cy + 3, fill='black')
            self.canvas.create_text(x_canvas, self.cy + 15, text=str(round(x, 1)), font="Verdana 9", fill='black')
            x += x_step

        y_step = (y_top - y_bottom) / 18
        y = y_top
        while y >= y_bottom:
            y_canvas = (y - y_top) * self.dy
            self.canvas.create_line(self.cx - 3, -y_canvas, self.cx + 3, -y_canvas, fill='black')
            self.canvas.create_text(self.cx + 25, -y_canvas, text=str(round(y, 1)), font="Verdana 9", fill='black')
            y -= y_step




    def centerWindow(self):
        w = 1280                         #ширина, высота окна
        h = 720

        sw = self.parent.winfo_screenwidth()        #Ширина, высота экрана
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))



        # canvas.create_polygon(
        #     points, outline='red',
        #     fill='green', width=2
        # )






    # entry = ttk.Entry()
    # entry.pack(anchor=NW, padx=16, pady=16)



    def InitUI(self):

        shapeCoords=0
        def getShapeCoords():
            global shapeCoords
            shapeCoords = list(map(int, entry1.get().split()))
            for i in range (0,len(shapeCoords),2):
                shapeCoords[i] *= self.dx
                shapeCoords[i]+=self.cx

                # shapeCoords[i]
            for i in range(1, len(shapeCoords), 2):
                shapeCoords[i] *= -self.dy
                shapeCoords[i]+=self.cy
            # shapeCoords[i]
            print(shapeCoords)
            self.canvas.create_polygon(shapeCoords, outline ='green', fill='green')

        def getLineCoords():
            global lineCoords
            lineCoords = list(map(int, entry2.get().split()))
            print(lineCoords)



        self.master.title("Lab1")
        self.style = Style()
        self.style.theme_use("default")

        # frame = Frame(self, relief="raised", borderwidth=1)
        # frame.pack(fill=BOTH, expand=True)                         # что-то не то
        # self.pack(fill=BOTH, expand=True)



        # closeButton = Button(self, text="Закрыть")
        # closeButton.pack(side=RIGHT, padx=5, pady=5)
        # okButton = Button(self, text="Готово", command=getData)
        # okButton.pack(side=RIGHT, padx = 5, pady = 5)
        # label = ttk.Label(self, text = "координаты точек прямой")
        # label.pack(side=RIGHT, padx=5, pady=5)
        # entry = ttk.Entry(self)
        # entry.pack(side = RIGHT, padx=5, pady=5)
#----------------------------------------------------------------------------

        frame1 = Frame(self,relief="raised",borderwidth=1)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Координаты вершин объекта", width=25)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1)
        entry1.pack(side = LEFT, padx=5)#, expand=True)
        okButton1 = Button(frame1, text="Готово", command=getShapeCoords)
        okButton1.pack(side=LEFT, padx=10, pady=5)

        frame2 = Frame(self, relief="raised", borderwidth=1)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Координаты точек прямой", width=25)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2)
        entry2.pack(side = LEFT, padx=5)#, expand=True)
        okButton2 = Button(frame2, text="Готово", command=getLineCoords)
        okButton2.pack(side=LEFT, padx=10, pady=5)



def main():
    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
