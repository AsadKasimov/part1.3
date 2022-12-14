import sqlite3

data = sqlite3.connect('db.sqlite3')  # создание базы
c = data.cursor()  # это курсор
ema = "vasia@mail.com"
#c.execute('SELECT * FROM users WHERE email = ? OR name = ?', (ema, 'Dru',))
#rese = c.fetchone()
#print(rese)
c.execute('SELECT * FROM users')
ree= c.fetchall()
for i in ree:
    print(i[1], i[2])
data.close()