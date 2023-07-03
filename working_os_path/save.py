def refresh_DB_path(new_path: str) -> bool:
    try:
        from data.data_const import PATH_CONST_FILE
        with open(PATH_CONST_FILE, 'rt', encoding='utf-8') as constFile:
            context: list[str] = constFile.readlines()
        for number, row in enumerate(context):
            if row.startswith('PATH_DATABASE: str = '):
                context[number] = f"PATH_DATABASE: str = r'{new_path}'"
        with open(PATH_CONST_FILE, 'wt', encoding='utf-8') as constFile:
            print(*context, sep='', end='', file = constFile)
        print('Новая база данных усешно заристрирована в системе')
        exit()
        return True
    except:
        return False
