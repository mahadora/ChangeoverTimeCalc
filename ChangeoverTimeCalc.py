import tkinter as tk
import tkinter.ttk as ttk

class App():

    def __init__(self, rt, title):
        #region Basics
        self.windowRoot = rt
        self.windowRoot.title(title)
        self.windowRoot.geometry('750x300')
        self.windowRoot.minsize(750,300)
        self.windowRoot.resizable(1,1)

        

if __name__ == "__main__":
    rt = tk.Tk()
    windowRoot = App(rt,title="Changeover Time Calculator")
    rt.mainloop()