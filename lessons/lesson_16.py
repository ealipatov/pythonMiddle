import xlsxwriter
import datetime


date_now = datetime.datetime.now()
# print(date_now)
# print(f"часов: {date_now.hour}")
# print(f"минут: {date_now.minute}")
# print(f"день: {date_now.day}")
# print(f"год: {date_now.year}")
#
# print(date_now - datetime.timedelta(days=3))

students = {
    "Петров": {
        "Математика": [
            (date_now - datetime.timedelta(days=1), 9),
            (date_now - datetime.timedelta(days=3), 8),
            (date_now - datetime.timedelta(days=5), 7)
        ],
        "Физика": [
            (date_now, 7),
            (date_now - datetime.timedelta(days=2), 8),
            (date_now - datetime.timedelta(days=7), 9)
        ]
    },
    "Сидорова": {
        "Математика": [
            (date_now - datetime.timedelta(days=1), 10),
            (date_now - datetime.timedelta(days=3), 9),
            (date_now - datetime.timedelta(days=5), 8)
        ],
        "Физика": [
            (date_now, 8),
            (date_now - datetime.timedelta(days=2), 9),
            (date_now - datetime.timedelta(days=7), 10)
        ]
    }
}
# Создаем файл
workbook = xlsxwriter.Workbook('test_files/students.xlsx')

# Создаем страницу (имя можно не указывать)
worksheet = workbook.add_worksheet("Петров")

# Создадим переменную с форматом - жирный шрифт
bold = workbook.add_format({"bold": True})

# Сделаем записи в ячейки жирным шрифтом
worksheet.write("A1", "Дата", bold)
worksheet.write("B1", "Математика", bold)
worksheet.write("C1", "Физика", bold)

worksheet.write("A2", str(date_now - datetime.timedelta(days=1))[:10])
worksheet.write("A3", str(date_now - datetime.timedelta(days=2))[:10])
worksheet.write("A4", str(date_now - datetime.timedelta(days=3))[:10])
worksheet.write("A5", str(date_now - datetime.timedelta(days=5))[:10])
worksheet.write("A6", str(date_now - datetime.timedelta(days=7))[:10])

worksheet.write("B2", 9)
worksheet.write("B4", 8)
worksheet.write("B5", 7)

worksheet.write("C3", 8)
worksheet.write("C6", 9)

#
# # Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)

# Insert an image.
# worksheet.insert_image('B5', 'logo.png')

workbook.close()