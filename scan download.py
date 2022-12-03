# -*- coding: utf8 -*-

"""Оконное приложение для скачивания сканов манги с сайта harimanga.com
Может быть полезно переводчикам, клинерам и тайперам, так как
позволяет в несколько кликов скачать сканы манги с этого сайта"""

import requests
import lxml
from bs4 import BeautifulSoup
from tkinter import *


def save_image():
    image_link = link_entry.get()
    image_path = path_entry.get()
    image_name = 'scan' if image_name_entry.get() == '' else image_name_entry.get()
    response = requests.get(image_link)
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    images = html.find_all(class_='page-break no-gaps')
    i = 0
    for image in images:
        p = requests.get(image.img['src'])
        out = open(image_path + '/' + image_name + str(i) + ".jpg", "ab")
        out.write(p.content)
        out.close()
        i += 1


window = Tk()
window.title("Загрузчик сканов с HARIMANGA.COM")
window.geometry('1000x600')

link_text = Label(text='Введите ссылку на главу манхвы',
                  font=('Helvetica', 30),
                  fg='black')
link_entry = Entry(window, font=('Halvetica', 24))
path_text = Label(text='Введите путь для сохранения сканов',
                  font=('Helvetica', 30),
                  fg='black')
path_entry = Entry(window, font=('Halvetica', 24))
image_name_text = Label(text='Введите название сканов (по умолчанию scan)',
                        font=('Helvetica', 30),
                        fg='black')
b = Button(text='Сохранить',
           font=('Helvetica', 30),
           bg='white',
           fg='black',
           command=save_image)
image_name_entry = Entry(window, font=('Halvetica', 24))
link_text.place(x=30, y=20)
link_entry.pack(anchor='nw', padx=30, pady=80)
path_text.place(x=30, y=150)
path_entry.pack(anchor='nw', padx=30, pady=10)
image_name_text.place(x=30, y=280)
image_name_entry.pack(anchor='nw', padx=30, pady=80)
b.place(x=50, y=450)
window.mainloop()
