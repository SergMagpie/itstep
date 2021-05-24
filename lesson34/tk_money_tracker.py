import tkinter as tk
from tkinter import messagebox as mb, ttk, simpledialog
from datetime import datetime, timedelta, date as d
from wallet import Wallet


class MyDialog(tk.simpledialog.Dialog):
    def __init__(self,
                 parent,
                 title,
                 money_amount=None,
                 date=None,
                 reason=None,
                 contragent=None):
        self.money_amount = money_amount
        self.date = date
        self.reason = reason
        self.contragent = contragent
        super().__init__(parent, title)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.money_amount_label = tk.Label(
            frame, width=25, text="money_amount")
        self.money_amount_label.pack()
        self.money_amount_box = tk.Entry(frame, width=25)
        self.money_amount_box.insert(0, str(self.money_amount or ''))
        self.money_amount_box.pack()

        self.date_label = tk.Label(frame, width=25, text="date")
        self.date_label.pack()
        self.date_box = tk.Entry(frame, width=25)
        self.date_box.insert(0, str(self.date or ''))
        self.date_box.pack()

        self.reason_label = tk.Label(frame, width=25, text="reason")
        self.reason_label.pack()
        self.reason_box = tk.Entry(frame, width=25)
        self.reason_box.insert(0, str(self.reason or ''))
        self.reason_box.pack()

        self.contragent_label = tk.Label(frame, width=25, text="contragent")
        self.contragent_label.pack()
        self.contragent_box = tk.Entry(frame, width=25)
        self.contragent_box.insert(0, str(self.contragent or ''))
        self.contragent_box.pack()

        return frame

    @staticmethod
    def money_validator(value_str):
        """Метод перевіряє правильність введення суми грошей"""
        val = None
        try:
            val = round(float(value_str), 2)
        except ValueError:
            return None
        return val

    @staticmethod
    def date_validator(value_str):
        """Метод перевіряж правильність введення дати"""
        val = None
        try:
            if value_str == '':
                return d.today()
            val = datetime.strptime(value_str, "%Y-%m-%d")
            val = val.date()
        except ValueError:
            return None
        return val

    def ok_pressed(self):
        # print("ok")
        self.money_amount = self.money_validator(
            self.money_amount_box.get())
        self.date = self.date_validator(
            self.date_box.get())
        self.reason = self.reason_box.get()
        self.contragent = self.contragent_box.get()

        if self.money_amount is None:
            mb.showerror("Mistake",
                         "Введіть дані в форматі числа (приклад -20.5)")
        elif self.date is None:
            mb.showerror("Mistake",
                         "Введіть дані в форматі дня (приклад 2021-5-3)")
        if all((self.money_amount, self.date)):
            self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.money_amount = None
        self.date = None
        self.reason = None
        self.contragent = None
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(
            self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(
            self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())


class DateDialog(tk.simpledialog.Dialog):
    def __init__(self,
                 parent,
                 title,
                 date_begin=None,
                 date_end=None):
        self.date_begin = date_begin
        self.date_end = date_end
        super().__init__(parent, title)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.date_begin_label = tk.Label(
            frame, width=25, text="date_begin")
        self.date_begin_label.pack()
        self.date_begin_box = tk.Entry(frame, width=25)
        self.date_begin_box.insert(0, str(self.date_begin or ''))
        self.date_begin_box.pack()

        self.date_end_label = tk.Label(
            frame, width=25, text="date_end")
        self.date_end_label.pack()
        self.date_end_box = tk.Entry(frame, width=25)
        self.date_end_box.insert(0, str(self.date_end or ''))
        self.date_end_box.pack()

        return frame

    @staticmethod
    def date_validator(value_str):
        """Метод перевіряж правильність введення дати"""
        val = None
        try:
            if value_str == '':
                return d.today()
            val = datetime.strptime(value_str, "%Y-%m-%d")
            val = val.date()
        except ValueError:
            return None
        return val

    def ok_pressed(self):
        # print("ok")
        self.date_begin = self.date_validator(
            self.date_begin_box.get())
        self.date_end = self.date_validator(
            self.date_end_box.get())

        if self.date_begin is None:
            mb.showerror("Mistake",
                         "Введіть дані в форматі дня (приклад 2021-5-3)")
        elif self.date_end is None:
            mb.showerror("Mistake",
                         "Введіть дані в форматі дня (приклад 2021-5-3)")
        if all((self.date_begin, self.date_end)):
            self.destroy()

    def cancel_pressed(self):
        # print("cancel")
        self.date_begin = None
        self.date_end = None
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(
            self, text='OK', width=5, command=self.ok_pressed)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(
            self, text='Cancel', width=5, command=self.cancel_pressed)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_pressed())
        self.bind("<Escape>", lambda event: self.cancel_pressed())


class TkInterface:
    LAST_WEEK = (d.today() - timedelta(days=7), d.today())
    LAST_MONTH = ((d.today().replace(day=1) - timedelta(days=1)
                   ).replace(day=d.today().day), d.today())

    def __init__(self, wallet) -> None:
        self.wallet = wallet()
        self.window = tk.Tk()

    def main_menu(self):
        self.mainmenu = tk.Menu(self.window)
        self.window.config(menu=self.mainmenu)

        edit_menu = tk.Menu(self.mainmenu, tearoff=0)
        edit_menu.add_command(label="add",
                              command=self.add)
        edit_menu.add_command(label="update",
                              command=self.update)

        all_menu = tk.Menu(self.mainmenu, tearoff=0)
        all_menu.add_command(label="show_all",
                             command=self.show_all)
        all_menu.add_command(label="show_all_for_last_week",
                             command=self.show_all_for_last_week)
        all_menu.add_command(label="show_all_for_last_month",
                             command=self.show_all_for_last_month)

        income_menu = tk.Menu(self.mainmenu, tearoff=0)
        income_menu.add_command(label="show_income",
                                command=self.income)
        income_menu.add_command(label="show_income_for_last_week",
                                command=self.show_income_for_last_week)
        income_menu.add_command(label="show_income_for_last_month",
                                command=self.show_income_for_last_month)

        outcome_menu = tk.Menu(self.mainmenu, tearoff=0)
        outcome_menu.add_command(label="show_outcome",
                                 command=self.outcome)
        outcome_menu.add_command(label="show_outcome_for_last_week",
                                 command=self.show_outcome_for_last_week)
        outcome_menu.add_command(label="show_outcome_for_last_month",
                                 command=self.show_outcome_for_last_month)

        smart_menu = tk.Menu(self.mainmenu, tearoff=0)
        smart_menu.add_command(label="get_the_most_expensive_costs",
                               command=self.get_the_most_expensive_costs)
        smart_menu.add_command(label="get_main_source_of_income",
                               command=self.get_main_source_of_income)

        self.mainmenu.add_cascade(label="Edit",
                                  menu=edit_menu)
        self.mainmenu.add_cascade(label="All",
                                  menu=all_menu)
        self.mainmenu.add_cascade(label="Income",
                                  menu=income_menu)
        self.mainmenu.add_cascade(label="Outcome",
                                  menu=outcome_menu)
        self.mainmenu.add_cascade(label="Smart",
                                  menu=smart_menu)

    def table(self):
        self.tree = ttk.Treeview(self.window,
                                 column=("c1", "c2", "c3", "c4", "c5"),
                                 show='headings')

        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(expand=True, fill='both', side='right')

        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="money_amount")

        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="date")

        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="reason")

        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="contragent")

        self.tree.pack(expand=True, fill='both', side='left')

    def show_info(self, msg):
        mb.showinfo("Information", msg)

    def tk_add_dialog(self, window):
        dialog = MyDialog(title="Add new record", parent=window)
        return dialog.money_amount,\
            dialog.date,\
            dialog.reason,\
            dialog.contragent

    def tk_update_dialog(self, window,
                         id,
                         money_amount,
                         date,
                         reason,
                         contragent):
        dialog = MyDialog(
            window,
            f"Update record {id}",
            money_amount,
            date,
            reason,
            contragent)
        return dialog.money_amount,\
            dialog.date,\
            dialog.reason,\
            dialog.contragent

    def update(self):
        """Метод відповідає за редагування запису"""
        id_row = simpledialog.askinteger("Enter ID",
                                         "Введіть ID запису для зміни")
        record = self.wallet.get_record_whith_id(id_row)
        if not record.count():
            if mb.askyesno(
                    title='Mistake',
                    message='Такого запису не інснує, створити новий?'):
                self.add()
            else:
                print('no')
        else:
            (money_amount,
             date,
             reason,
             contragent) = self.tk_update_dialog(self.window,
                                                 *record[0].variables())
            if money_amount:
                self.wallet.update(id_row, {"money_amount": money_amount,
                                            "date": date,
                                            "reason": reason,
                                            "contragent": contragent})

    def add(self):
        """Метод відповідає за додавання нового запису"""
        (money_amount, transaction_date,
         reason, contragent) = self.tk_add_dialog(self.window)
        if money_amount:
            self.wallet.new_record(money_amount,
                                   transaction_date,
                                   reason,
                                   contragent)

    def to_public(self, records):
        if not records.count():
            self.show_info("There is no information" +
                           "\non your request")
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in records:
            self.tree.insert("", tk.END, values=row.variables())

    def show_all(self):
        records = self.wallet.get_all_records()
        self.to_public(records)

    def show_all_for_last_week(self):
        records = self.wallet.get_all_records(*self.LAST_WEEK)
        self.to_public(records)

    def show_all_for_last_month(self):
        records = self.wallet.get_all_records(*self.LAST_MONTH)
        self.to_public(records)

    def input_dates(self, window, begin, end):
        dialog = DateDialog(window,
                            "Enter dates of period",
                            begin,
                            end)
        return dialog.date_begin, dialog.date_end

    def income(self):
        (begin, end) = self.input_dates(self.window,
                                        d.today(),
                                        d.today())
        records = self.wallet.get_income(begin, end)
        self.to_public(records)

    def show_income_for_last_week(self):
        records = self.wallet.get_income(*self.LAST_WEEK)
        self.to_public(records)

    def show_income_for_last_month(self):
        records = self.wallet.get_income(*self.LAST_MONTH)
        self.to_public(records)

    def outcome(self):
        (begin, end) = self.input_dates(self.window,
                                        d.today(),
                                        d.today())
        records = self.wallet.get_outcome(begin, end)
        self.to_public(records)

    def show_outcome_for_last_week(self):
        records = self.wallet.get_outcome(*self.LAST_WEEK)
        self.to_public(records)

    def show_outcome_for_last_month(self):
        records = self.wallet.get_outcome(*self.LAST_MONTH)
        self.to_public(records)

    def get_the_most_expensive_costs(self):
        records = self.wallet.get_the_most_expensive_costs()
        self.to_public(records)

    def get_main_source_of_income(self):
        records = self.wallet.get_main_source_of_income()
        self.to_public(records)

    def start(self):

        self.main_menu()

        self.table()

        self.window.mainloop()

        self.wallet.close()


if __name__ == "__main__":
    interface = TkInterface(Wallet)
    interface.start()
