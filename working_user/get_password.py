def get_hash_password() -> str:
    '''Начинает диалог с пользователем, заставляет
          его ввести корректный пароль, хеширует его и 
          возвращает результат хеша.'''

    from getpass import getpass
    from data.data_const import ( 
        MIN_LENGTH_PASS,
        MAX_LENGTH_PASS,
        SSET,
        MAX_REPEAT_CHAR,
        DENIED_COMBO,
    )
        

    def check_num_in_pas(pas: str) -> bool:
        for char in pas:
            if char.isdigit():
                return True
        return False
    
    def check_ss_in_pas(pas: str) -> bool:
        for ss in SSET:
            if ss in pas:
                return True 
        return False

    def additional_check(pas: str) -> bool:
        for combo in DENIED_COMBO:
            if combo.lower() in pas.lower():
                return False
        return True

    def check_repeat_char(pas: str) -> bool:
        repeatCounter: int = 1
        if not pas:
            return False
        for num, char in enumerate(pas[:-1]):
            if char == pas[num + 1]:
                repeatCounter += 1
                if repeatCounter == MAX_REPEAT_CHAR:
                        return False
            else:
                repeatCounter = 1
        return True

    check_case = lambda pas: pas.upper() != pas != pas.lower()
    check_len = lambda pas: MIN_LENGTH_PASS<=len(pas)<=MAX_LENGTH_PASS

    get_hash = lambda pas:  __import__('hashlib').md5(pas.encode()).hexdigest()

    while True:
        print('введи пароль:')
        user_response: str= getpass() 
        result = (
            check_case(user_response),
            check_num_in_pas(user_response),
            check_ss_in_pas(user_response),
            check_len(user_response),
            additional_check(user_response),
            check_repeat_char(user_response)
        )
        if all(result):
            return get_hash(user_response)
        for num, seccesfull_code in enumerate(result):
            if not seccesfull_code:
                error = [
                    'Нет разных регистров в пароле',
                    'Нет цифры в пароле',
                    'Нет специального символа в пароле',
                    f'Длинна пароля должна быть в дипозоне от {MIN_LENGTH_PASS} до {MAX_LENGTH_PASS}',
                    'В пароле не должны присутсвовать популярные сочетания сиволов',
                    f'В пароле не должно быть больше {MAX_REPEAT_CHAR} подряд идущих символов'   
                ][num] 
                print(error)
     