# from https://all-python.ru/primery/kalendar.html
from tkinter import *
from tkinter import messagebox as mb, ttk, simpledialog
import calendar
import datetime


class MyCalendar(simpledialog.Dialog):
    def __init__(self, parent, title) -> None:
        # self.root = Tk()
        # self.root.title('Calendar')
        self.days = []
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.rezult = self.now
        super().__init__(parent, title)

    def mouseClick(self, event, date):
        # print(f"mouse clicked on {date}")
        self.rezult = date
        self.destroy()

    def prew(self):
        # global month, year
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):
        # global month, year
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def fill(self):
        self.info_label['text'] = calendar.month_name[self.month] + \
            ', ' + str(self.year)
        self.month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            self.prew_month_days = calendar.monthrange(self.year-1, 12)[1]
        else:
            self.prew_month_days = calendar.monthrange(
                self.year, self.month - 1)[1]
        self.week_day = calendar.monthrange(self.year, self.month)[0]
        for n in range(self.month_days):
            self.days[n + self.week_day]['text'] = n+1
            self.days[n + self.week_day]['fg'] = 'black'
            self.days[n + self.week_day].bind(
                "<Button>", lambda x,
                m=datetime.date(
                    self.year, self.month, n+1): self.mouseClick(x, m))
            if (self.year == self.now.year and
                    self.month == self.now.month and n == self.now.day):
                self.days[n + self.week_day]['background'] = 'green'
            else:
                self.days[n + self.week_day]['background'] = 'lightgray'
        for n in range(self.week_day):
            self.days[self.week_day - n - 1][
                'text'] = self.prew_month_days - n
            self.days[self.week_day - n - 1]['fg'] = 'gray'
            self.days[self.week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6*7 - self.month_days - self.week_day):
            self.days[self.week_day + self.month_days + n]['text'] = n+1
            self.days[self.week_day + self.month_days + n]['fg'] = 'gray'
            self.days[self.week_day + self.month_days +
                      n]['background'] = '#f3f3f3'

    def body(self, frame):
        prew_button = Button(frame, text='<', command=self.prew)
        prew_button.grid(row=0, column=0, sticky='nsew')
        next_button = Button(frame, text='>', command=self.next)
        next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = Label(frame, text='0', width=1, height=1,
                                font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')
        for n in range(7):
            lbl = Label(frame, text=calendar.day_abbr[n], width=1, height=1,
                        font=('Verdana', 10, 'normal'), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                lbl = Label(frame, text='0', width=4, height=2,
                            font=('Verdana', 16, 'bold'))
                lbl.grid(row=row+2, column=col, sticky='nsew')

                self.days.append(lbl)
        self.fill()
        # self.root.mainloop()
        return frame



    
