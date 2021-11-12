import main


info = """
        Выберите команду:
        1: delete - удалить файл/директорию
        2: copy - скопировать файл/директорию
        3: move - переместить файл/директорию
        4: rename - переименовать файл/директорию
        5: write - запись текста в файл
        6: create_file - создать новый файл
        7: create_folder - создать папку
        8: change_directory - перемещение между папками
        9: exit - выход
    """


print(info)
while True:
    cmd = input('Что вы хотите сделать? ')

    if cmd == 'exit' or cmd == '9':
        exit(print('До свидания.'))

    elif cmd == 'delete' or cmd == '1':
        delete_file_name = input('Введите имя файла, который вы хотите удалить')
        main.delete_file(delete_file_name)

    elif cmd == 'copy' or cmd == '2':
        name = input('Введите имя файла/директории, которую вы хотите скопировать ')
        folder_name = input('Куда скопировать ваш файл? ')
        main.copy_file(name, folder_name)

    elif cmd == 'move' or cmd == '3':
        name = input('Введите имя файла/директории, которую вы хотите переместить ')
        folder_name = input('Куда переместить ваш файл? ')
        main.move_file(name, folder_name)

    elif cmd == 'rename' or cmd == '4':
        name = input('Введите имя файла/директории, которую вы хотите переименовать ')
        new_name = input('Введите новое название ')
        main.rename_file(name, new_name)

    elif cmd == 'write' or cmd == '5':
        name = input('Введите имя файла, в который вы хотите записать текст ')
        text = input('Введите текст ')

        main.write_file(name, text)

    elif cmd == 'create_file' or cmd == '6':
        name = input('Введите название нового файла')

        text = input('Введите текст, если вы хотите записать его в файл')

        main.create_file(name, text=text)

    elif cmd == 'create_folder' or cmd == '7':
        name = input('Введите название новой папки')
        main.create_folder(name)

    elif cmd == 'change_directory' or cmd == '8':
        print("""
        ..  если вы хотите подняться на уровень выше
        <имя папки> если вы хотите перейти в конкретную папку, если нужная папка вложена в другую, нужно указывать полный путь
        """)
        folder = input()
        main.change_directory(folder)



    else:
        print('Неверная команда')