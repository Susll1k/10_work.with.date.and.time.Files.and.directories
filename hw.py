#1----------------------------------------------------------------------------------------------------

import datetime 
dt = input("Date: ")
dt = datetime.datetime.strptime(dt, "%Y, %m, %d").date()
print(dt.isocalendar()[1])

#2----------------------------------------------------------------------------------------------------

import datetime
dt = input("Date: ")
dt = datetime.datetime.strptime(dt + '-1', "%Y, %W-%w")
formatted_dt = dt.strftime("%a %d %B %Y %H:%M:%S")
print(formatted_dt)


#3----------------------------------------------------------------------------------------------------

import datetime
year = input("Date: ")
weeknum = 1
while True:
    dt = datetime.datetime.strptime(f"{year}, {weeknum}" + '-0', "%Y, %W-%w")
    if dt.year != int(year):
        break
    formatted_dt = dt.strftime("%a %d %B %Y %H:%M:%S")
    print(formatted_dt)
    weeknum += 1

#4----------------------------------------------------------------------------------------------------

import datetime

def addYears(dt, y):
    year = dt.year + y
    month = dt.month
    day = dt.day
    return dt.strftime(f"{year}-{month}-{day}")

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29), 1))


#5----------------------------------------------------------------------------------------------------

from datetime import datetime
print(datetime.utcnow())
print(datetime.now())

#6----------------------------------------------------------------------------------------------------

from datetime import date
date_1 = date(2008, 12, 29)
date_2 = date(2001, 3, 22)
diff = date_1 - date_2
print(diff.days)

#7----------------------------------------------------------------------------------------------------

from datetime import date
date_1 = date(2008, 12, 29)
date_2 = date(2001, 3, 22)
diff = date_1 - date_2
days = diff.days
print(diff.days)
print(days * 24)
print(days * 24 * 60)
print(days * 24 * 60 * 60)

#8----------------------------------------------------------------------------------------------------

import datetime
import calendar

date_input = input("Введите дату в формате гггг-мм-дд: ")
date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d")
year = date_object.year
month = date_object.month
html_calendar = calendar.HTMLCalendar()
html_code = html_calendar.formatmonth(year, month)
file = open("calendar.html", "w")
file.write(html_code)
file.close()

#9----------------------------------------------------------------------------------------------------

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("filter.txt", "r", encoding="utf-8") as f:
    filters = f.read().split(",")

for filter in filters:
    text = text.replace(filter.strip(), "")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

#10----------------------------------------------------------------------------------------------------

letters = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'Y',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'H',
    'Ц': 'Ts',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Sch',
    'Ъ': '\'',
    'Ы': 'Y',
    'Ь': '\'',
    'Э': 'E',
    'Ю': 'Y',
    'Я': 'Ya',
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'e',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'y',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'ts',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'sch',
    'ъ': "''",
    'ы': 'y',
    'ь': "'",
    'э': 'e',
    'ю': 'y',
    'я': 'ya'
}

mode = input("Mode ru-eng(1), eng-ru(2):")

if mode == '1':
    with open("ex10_ru.txt", "r", encoding="utf-8") as f:
        text = f.read()

    for l in letters:
        text = text.replace(l, letters[l])

    with open("newex10_ru.txt", "w", encoding="utf-8") as f:
        f.write(text)

elif mode == '2':
    with open("ex10_eng.txt", "r", encoding="utf-8") as f:
        text = f.read()

    for l in letters:
        text = text.replace(letters[l], l)

    with open("newex10_eng.txt", "w", encoding="utf-8") as f:
        f.write(text)
else:
    print("Ошибка")


#11----------------------------------------------------------------------------------------------------
    
# Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово 
# quit. После завершения ввода программа должна объединить содержимое всех перечисленных 
# пользователем файлов в один.

lst_files=[]
while True:
    fil=input("Введи название файлов(ex10_eng.txt, ex10_ru.txt, filter.txt, input.txt). Если хочешь завершить напиши quit: ")
    if fil == "quit":
        break
    lst_files.append(fil)

lst_str = []
for i in lst_files:
    with open(i, "r", encoding="utf-8") as f:
        lst_str.append(f.read())

with open("output_ex11.txt", "w", encoding="utf-8") as f:
    for i in lst_str:
        f.write(i)

#12----------------------------------------------------------------------------------------------------
import re  

lst_files=[]
while True:
    fil=input("Введи название файлов(ex10_eng.txt, ex10_ru.txt, filter.txt, input.txt). Если хочешь завершить напиши quit: ")
    if fil == "quit":
        break
    lst_files.append(fil)

lst_str = []
for i in lst_files:
    with open(i, "r", encoding="utf-8") as f:
        words = re.findall("[.,:;~`'/?:*-+%^@#$&]", f.read())
        lst_str.append(words)

with open("output_ex12.txt", "w", encoding="utf-8") as f:
    for i in lst_str:
        for j in i:
            f.write(j)



# 13----------------------------------------------------------------------------------------------------
            
# В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me 
# и переложите туда содержимое указанных папок (сами папки класть не надо).

import shutil
import os

os.mkdir("watch_me")
shutil.move("sub/sub.txt", "watch_me")
shutil.move("video/video.txt", "watch_me")


# 14----------------------------------------------------------------------------------------------------

# В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п. 
# Переименуйте их переставив имя и фамилию местами.

import os
os.rename('ex_14/Misha_Perelman.jpg', 'ex_14/Perelman_Misha.jpg')
os.rename('ex_14/Nina_Stoletova.jpg', 'ex_14/Stoletova_Nina.jpg')


# 15----------------------------------------------------------------------------------------------------

import shutil

with open("list.tsv", "r", encoding="utf-8") as f:
    text = f.read().split()

for t in text:
    shutil.move(t, "list")


# 16----------------------------------------------------------------------------------------------------

# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой 
# файл.
    
with open("ex_16.txt", "r", encoding="utf-8") as f:
    text_f = f.read().split("\n")[-1:]
with open("ex_16.txt", "r", encoding="utf-8") as f:
    txt=f.read()
print(text_f)

for filter in text_f:
    txt = txt.replace(filter.strip(), "")

with open("newex_16.txt", "w", encoding="utf-8") as f:
    f.write(txt)
