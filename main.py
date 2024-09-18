# from array import array
from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Style



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Window")
        self.pack(fill=BOTH, expand=1) #для центровки окна
        self.centerWindow()

        self.InitUI()

    def centerWindow(self):
        w = 1280                         #ширина, высота окна
        h = 720

        sw = self.parent.winfo_screenwidth()        #Ширина, высота экрана
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


        #Блок оси и их масштаб
        canvas = Canvas(self)
        canvas.create_line(0, sh/2, sw, sh/2)
        canvas.pack(fill=BOTH, expand=1)

        canvas.create_line(sw/2, 0, sw/2, sh)
        canvas.pack(fill=BOTH, expand=1)






    # entry = ttk.Entry()
    # entry.pack(anchor=NW, padx=16, pady=16)



    def InitUI(self):

        shapeCoords=0
        def getShapeCoords():
            global shapeCoords
            shapeCoords = entry1.get()
            arrShape = list(map(int, shapeCoords.split()))
            print(shapeCoords)
            print(arrShape)

        def getLineCoords():
            global lineCoords
            lineCoords = entry2.get()
            arrLine = list(map(int, lineCoords.split()))
            print(lineCoords)
            print(arrLine)


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
