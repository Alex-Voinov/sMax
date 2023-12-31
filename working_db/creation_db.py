def primary_creation() -> bool:
    from working_user.funk_atteraction import getResponce
    from working_os_path.save import refresh_DB_path
    if getResponce('Желаете ли вы создать базу данных?', notification='Базад данных не найдена'):
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
        from working_user.get_password import get_hash_password
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
                    elif field=='password':
                        user_data.append(get_hash_password())
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
                refresh_DB_path(path_db_main)
        except:
            return False
        return True
    return False
