import os
import shutil


# функция для создания папки
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Папка с таким именем уже есть')

# функция для создания файла
def create_file(file_name, text=None):
    with open(file_name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

# удаление файлов и папок
def delete_file(file_name):
    if os.path.isdir(file_name):
        try:
           os.rmdir(file_name)
        except OSError:
            prov= input('Папка не пуста. Хотите продолжить? y/n ')
            if prov == 'y':
                shutil.rmtree(file_name, ignore_errors=True)
    elif os.path.isfile(file_name):
        os.remove(file_name)

# копирование файла в папку
def copy_file(file_name,folder_name):
    try:
        shutil.copy(file_name, folder_name)
    except FileNotFoundError:
        print('Такого файла нет')

# переименовать файл
def rename_file(name, new_name):
    try:
        os.rename(name, new_name)
    except FileNotFoundError:
        print('Такого файла нет')

# перемещение файла
def move_file(name, move_name):
    try:
        shutil.move(name, move_name)
    except FileNotFoundError:
         print('Такого файла нет')

# вывод содержимого файла
def print_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

# Запись текста в файл
def write_file(file_name, text):
    with open(file_name, "w") as file:
        file.write(text)

# изменить рабочую папка
def change_directory(new_dir):
    if new_dir == "..":
        os.chdir("..")
    else:
        try:
            os.chdir(new_dir)
        except FileNotFoundError:
            print('Такой папки нет')
    print('Текущая рабочая папка: ', os.getcwd())


