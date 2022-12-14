import sqlite3

data = sqlite3.connect('db.sqlite3')  # создание базы
c = data.cursor()  # это курсор
#c.execute('INSERT INTO users (name, email, password) VALUES ("Иван", "ivan@mail.com", "12345678")')
# одним разом одни данные
#c.executescript('''
#INSERT INTO users (name, email, password) VALUES ("Абу", "abu@mail.com", "12ar45678");
#INSERT INTO users (name, email, password) VALUES ("Василиса", "vasia@mail.com", "87654321");
#''') # добавил одним разом много данных

dobavka=[
    ('Fleks', 'Fleks@mail.ru', 'liauvzdj'),
    ('Dru', 'Dru@mail.com', '76sgbhk')
]

c.executemany('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', dobavka)  # добавляем только
# действие отдельно от данных

data.commit() # отпровляет в базу данные
data.close()
