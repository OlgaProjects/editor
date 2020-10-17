import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from tkinter.messagebox import showerror
from tkinter import messagebox
import codecs
from Text_editor import *
from settings import *

app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

scroll = Scrollbar(app, orient=VERTICAL, command=text.yview) #создали скролл
scroll.pack(side='right', fill='y') #разместили скролл
text.configure(yscrollcommand=scroll.set) #связь текста со скроллом
text.pack() #разместили поле с текстом

menuBar = tkinter.Menu(app) #Создаем меню
editor = Text_editor()

app_menu = tkinter.Menu(menuBar) # выпадающее меню "файла"
app_inquiry = tkinter.Menu(menuBar) #выпадающее меню "справки"

app_menu.add_command(label='Новый',command=editor.new_file)
app_menu.add_command(label='Открыть',command=editor.open_file)
app_menu.add_command(label='Сохранить',command=editor.save_file)
app_menu.add_command(label='Сохранить как',command=editor.save_as_file)

app_inquiry.add_command(label='О программе', command=editor.get_info)
app_inquiry.add_command(label='Интерфейс')
app_inquiry.add_command(label='Настройки')
app_inquiry.add_command(label='Помощь')
app_inquiry.add_command(label='Лицензионное соглашение')

menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка', menu=app_inquiry)
menuBar.add_cascade(label='Вид')
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar) #публкуем меню

app.mainloop()  #создаем бесконечный цикл нашего приложения
