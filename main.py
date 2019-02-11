from tkinter import *
from datetime import datetime, date, time

class MainWindow:
    def __init__(self, master):
        """Main window"""
        self.master = master
        self.master.title("Умный дом")
        self.master.resizable(False, False)
        self.screenwidth, self.screenheight = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("800x600+{}+{}".format(self.screenwidth//2-400, self.screenheight//2-300))

        self.add_mainmenu()
        self.add_datetime()
        self.add_meters()

    def add_mainmenu(self):
        self.mainmenu = Menu(self.master)
        self.master.config(menu=self.mainmenu)
        self.configmenu = Menu(self.mainmenu, tearoff=0)
        self.configmenu.add_command(label="Открыть")
        self.configmenu.add_command(label="Сохранить")
        self.mainmenu.add_cascade(label="Настройки", menu=self.configmenu)

    def add_datetime(self):
        self.date = Label(self.master, text="Время")
        self.date.pack()
        self.date.after_idle(self.update_date_time)

    def update_date_time(self):
        self.date.after(1000, self.update_date_time)
        dt = datetime.now()
        self.date['text']=dt.strftime("%H:%M:%S %d %B %Y")
    
    def add_meters(self):
        self.meters_frame = []
        for i in range(2):
            x = Frame()
            self.meters_frame.append(x)
            self.meters_frame[i].pack()
        self.addmeter = Button(text='Настройка счетчиков', command=self.metersconfig)
        self.addmeter.pack()
        self.meters = [{'title': 'Холодная вода', 'indication':'00000001', 'last_indication':'00000001', 'last_pay_date':'1.02.2019', 'cost':'15'}, {'title': 'Горячая вода', 'indication':'000135481', 'last_indication':'000134856', 'last_pay_date':'1.02.2019', 'cost':'15'}]
        x = 0
        for i in self.meters:
            if x < 4:
                self.i = Meter(self.meters_frame[0], i)
            else:
                self.i = Meter(self.meters_frame[1], i)
            x += 1


    def metersconfig(self):
        MetersConfig(self)

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

class MetersConfig():
    def __init__(self, main_window):
        self.main = main_window
        self.window = Toplevel(self.main.master)
        self.window.geometry("800x300+{}+{}".format(self.main.screenwidth//2-400, self.main.screenheight//2-150))
        self.window.columnconfigure(1, weight=2)
        self.window.columnconfigure(2, weight=1)
        self.window.columnconfigure(3, weight=1)
        self.window.columnconfigure(4, weight=1)
        self.window.columnconfigure(5, weight=1)
        self.window.columnconfigure(6, weight=1)
        self.update_table()

    def update_table(self): 
        meters_titles = ['', 'Заголовок', 'Оплата', 'Показания', 'Источник', 'Цена']
        x = 1
        for i in meters_titles:
            meter_titles = Label(self.window, width=20, text=i)
            meter_titles.grid(row=0, column=x)
            x += 1
        index = 0
        meter = []
        x = 1
        for line in self.main.meters:
            meter.append({})
            meter[index]['Check'] = BooleanVar()
            meter[index]['Check'].set(0)
            meter[index]['Checkbutton'] = Checkbutton(self.window, variable=meter[index]['Check'], onvalue=1, offvalue=0, width=5, bg='red')
            meter[index]['Checkbutton'].grid(row=x, column=1)
            meter[index]['title'] = Label(self.window, text=line['title'], width=15, bg='red')
            meter[index]['title'].grid(row=x, column=2)
            meter[index]['last_pay_date'] = Label(self.window, text=line['last_pay_date'], width=15, bg='red')
            meter[index]['last_pay_date'].grid(row=x, column=3)
            meter[index]['last_indication'] = Label(self.window, text=line['last_indication'], width=15, bg='red')
            meter[index]['last_indication'].grid(row=x, column=4)
            meter[index]['indication'] = Label(self.window, text=line['indication'], width=15, bg='red')
            meter[index]['indication'].grid(row=x, column=5)
            meter[index]['cost'] = Label(self.window, text=line['cost'], width=15, bg='red')
            meter[index]['cost'].grid(row=x, column=6)           
            index += 1
            x += 1
        add = Button(self.window, text='Добавить', command=lambda index=[9]: self.meter_edit(index))
        add.grid(row=x, column=1, columnspan=2) 
        edit = Button(self.window, text='Редактировать')
        edit.grid(row=x, column=3, columnspan=2) 
        delete = Button(self.window, text='Удалить') 
        delete.grid(row=x, column=5, columnspan=2) 

    def meter_edit(self, index):
        window = Toplevel(self.window)
        window.geometry("400x300+{}+{}".format(self.main.screenwidth//2-200, self.main.screenheight//2-150))
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        Label(window, text='Новый счетчик').grid(row=0, column=1, columnspan=2)
        x = []
        meters_titles = ['', 'Заголовок', 'Оплата', 'Показания', 'Источник', 'Цена']
        for i in range(1,6):
            l = Label(window, text=meters_titles[i]).grid(row=i, column=1)
            x.append(Entry(window).grid(row=i, column=2)) 
        
            

 
        




    def delmeter(self, index):
        self.main.meters.remove(index)
        print(self.main.meters)




def main():
    root = Tk()
    MainWindow(root)
    print(datetime.now())
    root.mainloop()

if __name__ == "__main__":
    main()