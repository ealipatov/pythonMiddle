# Запись/перезапись информации в файл (перезапишет существующий)
with open("info.txt", "w") as file:
    file.write("Привет медвед!\n")

# Добавляем запись в файл
with open("info.txt", "a") as file:
    file.write("DDDDDDDDDDDD")

# Чтение из файла
with open("info.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.replace("\n", ""))