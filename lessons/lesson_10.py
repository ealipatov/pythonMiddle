# Запись/перезапись информации в файл (перезапишет существующий)
with open("test_files/info.txt", "w") as file:
    file.write("Привет медвед!\n")

# Добавляем запись в файл
with open("test_files/info.txt", "a") as file:
    file.write("DDDDDDDDDDDD")

# Чтение из файла
with open("test_files/info.txt") as file:
    lines = file.readlines()
    for line in lines:
        print(line.replace("\n", ""))