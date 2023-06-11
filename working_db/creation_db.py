def primary_creation() -> bool:
    request_user: str = '> Желаете ли вы создать базу данных?\n> '
    if input(request_user).lower().strip() in ('да', 'конечно', 'y', 'yes', '+'):
        from data.data_const import(
            DIR_DB,
            MAIN_DB,
            FIELDS_MAIN_DB,
            SEPARATION,
            SYS_FIELDS,
            SPECIAL_FIELD
        )
        from os.path import  abspath, split, join
        from datetime import datetime as D
        START_SPECIAL_FIELD = 0
        LAST_SPECIAL_FIELD = 0

        try:
            creation_file_path: str = abspath(__file__)
            dir_file = split(split(creation_file_path)[0])[0]

            dir_dbase: str = join(dir_file, DIR_DB)
            path_db_main: str = join(dir_dbase, f'{MAIN_DB}.txt')

            with open(path_db_main, 'wt', encoding='utf-8') as db_file_dis:
                print(SEPARATION.join(FIELDS_MAIN_DB), file=db_file_dis)
                user_data: list[str] = []
                for index, field in enumerate(FIELDS_MAIN_DB):
                    if index in SYS_FIELDS:
                        if index == 0:
                            user_data.append(0)
                        elif index == -1:
                            user_data.append('Admin')
                        else:
                            user_data.append(D.now())
                    elif SPECIAL_FIELD[START_SPECIAL_FIELD] <= index <= SPECIAL_FIELD[LAST_SPECIAL_FIELD]:
                        user_data.append('')
                    else:
                        user_data.append(input(f'\n> Введи <{field}>'))
                print(
                    *map(
                        str,
                        user_data
                    ),
                    SEPARATION,
                    file=db_file_dis,
                    end=''
                )
        except:
            return False
        return True
    return False
