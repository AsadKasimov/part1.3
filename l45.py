import sqlite3

data = sqlite3.connect('db.sqlite3') # создание базы
c = data.cursor() #это курсор
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT  NULL, 
    email TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL
)
''') # создание столбцов

data.close() # надо закрыть
