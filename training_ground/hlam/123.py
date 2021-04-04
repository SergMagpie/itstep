from tkinter import *
from tkinter.ttk import Radiobutton  
import random
from tkinter.ttk import Combobox 

  
a = ['Выпей кофе','Поговорить с близкими!','Отдохни сегодня','Хорошо бы тебе прогуляться','Напиши друзьям','Покушай здоровой еды','Сделай разминку']
def clicked():
    lbl.configure(text=random.choice(a))
def angr():  
    res = "Привет {}, вот твое предсказание".format(txt.get())  
    lbl.configure(text=res)   

window = Tk()  
window.title('Добро пожаловать в приложение "ПеЧеНьКи"')  
window.geometry('1400x1250')  
selected = IntVar() 
txt = Entry(window,width=10)  
txt.grid(column=10, row=0)
lbl1 = Label(window, text="Введите свой возраст:")  
lbl1.grid(column=18, row=0)
# lbl2.grid(column=20, row=0)   
rad1 = Radiobutton(window,text='Понедельник', value=1, variable=selected)  
rad2 = Radiobutton(window,text='Вторник', value=2, variable=selected)  
rad3 = Radiobutton(window,text='Среда', value=3, variable=selected)
rad4 = Radiobutton(window,text='Четверг', value=4, variable=selected)  
rad5 = Radiobutton(window,text='Пятница', value=5, variable=selected)  
rad6 = Radiobutton(window,text='Суббота', value=6, variable=selected)
rad7 = Radiobutton(window,text='Воскресенье', value=7, variable=selected)  
btn = Button(window, text="За печенькой!", command=clicked, bg="black", fg="yellow") 
angr1 = Button(window, text="Я ввёл имя!", command=angr ,bg="black", fg="yellow")  
lbl = Label(window)  
rad1.grid(column=0, row=0)  
rad2.grid(column=1, row=0)  
rad3.grid(column=2, row=0)
rad4.grid(column=3, row=0)  
rad5.grid(column=4, row=0)  
rad6.grid(column=5, row=0)
rad7.grid(column=6, row=0)  
btn.grid(column=3, row=3)  
lbl.grid(column=0, row=1)
angr1.grid(column=13, row=0)
combo = Combobox(window)  
combo['values'] = ('1-5','6-10','11-15','16-20','21-25','26-35','36-50','>50','конфиденциальная информация')  
# combo.current('конфиденциальная информация')  
combo.grid(column=20, row=0)  
window.mainloop() 