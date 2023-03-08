# Работа с Excel and JSON
import openpyxl
import json

with open('a.json') as f:
    file =json.load(f)


book = openpyxl.Workbook()

sheet = book.active # Дает доступ к листу

sheet['A1'] = 'id'
sheet['B1'] = 'Language'
sheet['C1'] = 'Edition'
sheet['D1'] = 'Author'

row = 2 # Указываем что начинается со второго ряда
for i in file['book']:
    sheet[row][0].value = i['id']
    sheet[row][1].value = i['language']
    sheet[row][2].value = i['edition']
    sheet[row][3].value = i['author']
    row += 1 # Указываем для записи в каждый ряд

# sheet[2][0].value = 'Hello' # Обращаемся по ряду и по колонке, обязательно указываем value
# sheet.cell(row=1, column=1).value = 'How are you ?' # Еще один вариант записи
#
book.save('my_b.xlsx') # Указываем разрешение при сохранении
book.close() # Обязательно закрывать программу

