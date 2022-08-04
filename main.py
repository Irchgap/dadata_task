import sqlite3
from dadata import Dadata


token = input('Введите токен \n')
language = input('Введите язык(русский по умолчанию) \n')
if language != 'en':
    language = 'ru'


def settings(token, language):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users_settings 
    (token text, lan text) ''')
    cursor.execute('INSERT INTO users_settings VALUES (?, ?)', (token, language))
    conn.commit()


def exit():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS users_settings""").fetchall()
    conn.commit()


try:
    settings(token, language)
    while True:
        query = input('Введите адрес, для выхода введите exit \n')
        if query ==exit() or query == '':
            exit()
            break
        else:
            dadata = Dadata(token)
            result = dadata.suggest('address', query, language=language)
            x={}
            for i in range(len(result)-1):
                x[i]=result[i]['value']

            for k, v in x.items():
                print(f"{k} : {v}")

            choice = int(input('Выберете номер интересующего адреса \n'))
            result = dadata.suggest('address', x[choice])
            print('Долгота:', result[0]['data']['geo_lat'], 'Широта:', result[0]['data']['geo_lon'])
except:
    print("Ошибка!")