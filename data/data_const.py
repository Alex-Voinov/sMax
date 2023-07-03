PATH_CONST_FILE: str = __import__('os').path.abspath(__file__)

PATH_DATABASE: str = r'c:\Users\Voino\Maxim\sMax\DataBase\main_data.txt'
FIELDS_MAIN_DB: tuple[str] = (
    'id',
    'login',
    'name',
    'last_name',
    'password',
    'number',
    'email',

    'country',
    'city',
    'bday',

    'LSO',
    'role',
)

SYS_FIELDS: tuple[int] = (0, 10, 11)
SPECIAL_FIELD: tuple[int, int] = (7, 9)

SEPARATION: str = '\t' * 4
DIR_DB: str = 'DataBase'
MAIN_DB: str = 'main_data'
