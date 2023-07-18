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

LANGUAGE_LIST: tuple[str] = (
    'Русский язык',
    'English language',
    '中文'
)

UNKNOW: int = -1
KEY_LAN: int = UNKNOW

SEPARATION: str = '\t' * 4
DIR_DB: str = 'DataBase'
MAIN_DB: str = 'main_data'

MIN_LENGTH_PASS: int = 5
MAX_LENGTH_PASS: int = 15
     
SSET: str = '~`!@#$%^&*()_+=-[];\\/|<>'
MAX_REPEAT_CHAR: int = 5
DENIED_COMBO: tuple[str] = (
    'QWER',
    'ABC',
    'ZXC',
    '1234',
    '9876',
    '0000',
    '1111',
    'pas',
)
