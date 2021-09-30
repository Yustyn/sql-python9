import psycopg2

from psycopg2 import Error
from settings import *

try:
    connection = psycopg2.connect(user=USER,
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT,
                                  database='py_db'
                                  )

    cursor = connection.cursor()
    # 1. Створити 10 користувачів в БД за допомогою  insert
    create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                            id INT PRIMARY KEY NOT NULL,
                            name TEXT          NOT NULL,
                            email TEXT         NOT NULL,
                            password TEXT      NOT NULL);'''
    cursor.execute(create_table_query)
    connection.commit()

    insert_query = """INSERT INTO users  (id, name, email, password) VALUES
                    (1, 'Bill', 'bill@ukr.net', 'bill_best'),
                    (2, 'Bob', 'bob@gmail.com', 'bob_best'),
                    (3, 'Jack', 'jack@google.com', 'jack_best'),
                    (4, 'Dick', 'dick@mymail.com', 'dick_best'),
                    (5, 'Conrad', 'conrad@super.ua', 'conrad_best'),
                    (6, 'Alex', 'alex@ukr.net', 'alex_best'),
                    (7, 'Michael', 'michael@gmail.com', 'michael_best'),
                    (8, 'Daniel', 'daniel@google.com', 'daniel_best'),
                    (9, 'Enzo', 'enzo@mymail.com', 'enzo_best'),
                    (10, 'Tom', 'tom@super.ua', 'tom_best')"""
    cursor.execute(insert_query)
    connection.commit()
    print('Table was updated')

    # 2. Вивести всіх у кого поштова скринька на gmail
    select_query = "SELECT * FROM users where email like '%gmail%'"
    cursor.execute(select_query)
    connection.commit()
    print('Result:', cursor.fetchall())

    # 3. Змінити пароль користувачу ID 4
    update_query = "UPDATE users SET password = 'best_dick' WHERE id=4"
    cursor.execute(update_query)
    connection.commit()
    print('Information was updated')

    # 4. Видалити користувача під іменем Bill (або якесь інше)
    delete_query = """DELETE from users WHERE name='Jack' """
    cursor.execute(delete_query)
    connection.commit()
    print('Information was deleted')

    # 5. Показати всіх користувачів у який ім'я починається на A
    select_query = "SELECT name, email FROM users where name like 'A%'"
    cursor.execute(select_query)
    connection.commit()
    print('Result:', cursor.fetchall())

except(Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed')
