from tkinter import *
from datetime import datetime, date, time

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Умный дом")
        self.master.resizable(False, False)
        self.screenwidth, self.screenheight = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("800x600+{}+{}".format(self.screenwidth//2-400, self.screenheight//2-300))

        self.mainmenu = Menu(self.master)
        self.master.config(menu=self.mainmenu)
        self.configmenu = Menu(self.mainmenu, tearoff=0)
        self.configmenu.add_command(label="Открыть")
        self.configmenu.add_command(label="Сохранить")
        self.mainmenu.add_cascade(label="Настройки", menu=self.configmenu)

        self.date = Label(master, text="Время")
        self.date.pack()
        self.date.after_idle(self.tick)

    def tick(self):
        self.date.after(500, self.tick)
        dt = datetime.now()
        self.date['text']=dt.strftime("%H:%M:%S %d %B %Y")





def main():
    root = Tk()
    MainWindow(root)
    print(datetime.now())
    root.mainloop()

if __name__ == "__main__":
    main()