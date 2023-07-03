def menu():
    from typing import Callable
    def signUp(): print('папали в регистрацию')
    def signIN(): print('папали в авторизацию')
    def setOption(): ...
    def mailHelp(): ...


    POINT_NUMBER_TITLE: dict[int, str]= {
        1: 'Авторизоваться',
        2: 'Зарегестрироваться',
        3: 'Общие настройки приложения',
        4: 'Сервис поддержки',
        5: 'Выход,'
    }


    TITLE_FUNCTION: dict[str, Callable]={
        'Авторизоваться': signIN,
        'Зарегестрироваться': signUp ,
        'Общие настройки приложения': setOption,
        'Сервис поддержки': mailHelp,
        'Выход': exit,
    }

    print()
    print('Меню:')
    for number, name in POINT_NUMBER_TITLE.items():
        print(f'\t{number}) {name}\n')
    print()

    user_responce: str = ''
    while True:
        print('Выберите номер действия')
        user_responce = input('>')
        if user_responce in (tuple(map(str, POINT_NUMBER_TITLE.keys())) + tuple(POINT_NUMBER_TITLE.values())): break
    

    if user_responce in map(str,POINT_NUMBER_TITLE.keys()):
        number: int = int(user_responce)
        title: str = POINT_NUMBER_TITLE[number]
        TITLE_FUNCTION[title]()
    else:
        TITLE_FUNCTION[user_responce]()


