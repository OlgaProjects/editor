import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename
from tkinter.messagebox import showerror
from tkinter import messagebox
import codecs
from settings import *

app = tkinter.Tk()
text = tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap = 'word')

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = 'Без названия'
        text.delete('1.0', tkinter.END)

    def open_file(self):
        inp = askopenfilename()#открываем по названию
        if inp is None:
            return
        with codecs.open(inp, encoding='utf-8') as inp_text: # кодировка текста
            data = inp_text.read()# помещаем в переменную прочитанный текст после кодировки
            text.delete('1.0', tkinter.END)# удаляем напечатанный текст в окне
            text.insert('1.0', data)# помещаем наш перекодированный текст
            print(data)


    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode='w', defaultextension='txt') # открываем окно
        data = text.get('1.0', tkinter.END) #считываем все с поля, что вводили
        try:
            output.write(data.rstrip()) #попытка записать и обрезка лишних проблелов справа
        except Exception:
            showerror(title='Ошибка', message='Ошибка при сохранении файла')

    def get_info(self):
        messagebox.showinfo('О программе', 'Информация о нашем приложении. Спасибо, что его используете!')



