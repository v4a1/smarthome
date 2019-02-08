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

        self.addmeter = Button(master, text='Добавить счетчик', command= lambda: AddMeter(self))
        self.addmeter.pack()

        self.meter_frame = Frame()
        self.meter_frame.pack()

        meters = [{'title': 'Холодная вода', 'indication':'00000001', 'last_indication':'00000001', 'last_pay_date':'1.02.2019', 'cost':'15'}, {'title': 'Горячая вода', 'indication':'000135481', 'last_indication':'000134856', 'last_pay_date':'1.02.2019', 'cost':'15'}]

        for i in meters:
            self.i = Meter(self.meter_frame, i)

        #cold_water_meter = {'title': 'Холодная вода', 'indication':'00000001', 'last_indication':'00000001', 'last_pay_date':'1.02.2019', 'cost':'15'}
        #self.cold_water_meter = Meter(self.meter_frame, cold_water_meter)

        #hot_water_meter = {'title': 'Горячая вода', 'indication':'000135481', 'last_indication':'000134856', 'last_pay_date':'1.02.2019', 'cost':'15'}
        #self.hot_water_meter = Meter(self.meter_frame, hot_water_meter)

    def tick(self):
        self.date.after(1000, self.tick)
        dt = datetime.now()
        self.date['text']=dt.strftime("%H:%M:%S %d %B %Y")
    
    def add_meter(self):
        pass

class Meter(Frame):
    def __init__(self, master, date):
        Frame.__init__(self, master)
        self.pack(side=LEFT)
        self['width'] = 200
        self['height'] = 300
        self['bg'] = 'black'
        self['bd'] = 5
        self.label = Label(self, text=date.get('title'))
        self.label.pack()
        self.lebel_indication = Label(self, text='Текущие')
        self.lebel_indication.pack()
        self.indication = Label(self, text=date.get('indication'), font='arial 24')
        self.indication.pack()
        self.last_pay_date = Label(self, text='Оплачены '+date.get('last_pay_date'))
        self.last_pay_date.pack()
        self.last_indication = Label(self, text=date.get('indication'))
        self.last_indication.pack()
        self.pay = Label(self, text='Нужно заплатить ' + str((int(date.get('indication')) - int(date.get('last_indication'))) * int(date.get('cost'))) + ' Рублей')
        self.pay.pack()

class AddMeter():
    def __init__(self, main_window):
        self.main = main_window
        self.windows = Toplevel(main_window.master)
        self.windows.geometry("400x300+{}+{}".format(self.main.screenwidth//2-200, self.main.screenheight//2-150))



def main():
    root = Tk()
    MainWindow(root)
    print(datetime.now())
    root.mainloop()

if __name__ == "__main__":
    main()