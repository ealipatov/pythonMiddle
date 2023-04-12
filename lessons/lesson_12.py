import os.path

INFO_FILE_TXT = "info.txt"


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("Привет медвед!\n")


def create_folder(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)


def move_file(from_folder, to_folder):
    os.rename(from_folder, to_folder)


create_file(INFO_FILE_TXT)
create_folder(r"new_folder")

move_file(INFO_FILE_TXT, f"new_folder/{INFO_FILE_TXT}")
