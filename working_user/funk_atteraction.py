
DEFAULT_POSITIVE_LIST: tuple[str] = (
    'да',
    'конечно',
    'y',
    'yes',
    'yep',
    'согласен',
    'хорошо',
    'принимаю'
)

DEFAULT_NEGATIVE_LIST: tuple[str] = (
    'нет',
    'ни в койм случае',
    'n',
    'no',
    'nope',
    'not',
    'отмена',
    'отказываюсь'
)

def getResponce(
        request: str,
        notification: str = '',
        positiveList: str = DEFAULT_POSITIVE_LIST,
        negativeList: str = DEFAULT_NEGATIVE_LIST
) -> bool:
    if notification:
        print(notification)
    print()
    print(request)
    while True:
        user_responce = input('> ').lower().strip()
        if user_responce in positiveList:
            return True
        elif user_responce in negativeList:
            return False
        else:
            print('Ваш ввод неккоректен, пожалуйста дайте ответ из списка:')
            print(*DEFAULT_POSITIVE_LIST, sep='\n')
            print(*DEFAULT_NEGATIVE_LIST, sep='\n')
