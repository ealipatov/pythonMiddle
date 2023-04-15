import os.path
import shutil


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("Привет медвед!\n")


def create_folder(path_folder):
    if not os.path.exists(path_folder):
        os.makedirs(path_folder)


create_folder(r"test_files")
create_file("test_files/test_files.txt")

# shutil.copy("test_files/test_files.txt", "test_files/test_files_1.txt")

shutil.make_archive("compressed", "zip", "test_files/")