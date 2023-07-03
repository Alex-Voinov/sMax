def main() -> None:
    from data.data_const import PATH_DATABASE
    from os.path import exists
    from working_db.creation_db import primary_creation
    from Authorization.main_menu import menu
    if exists(PATH_DATABASE) or primary_creation():
        menu()
    else:
        print('приложение завершено успешно')
        exit()



if __name__ == '__main__':
    main()