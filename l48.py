import zipfile
import os.path

start = os.path.dirname(__file__)
a = os.path.abspath(r'folder\pod_foldtr\1.txt')
t = os.path.relpath(a, start)
print(t)
with zipfile.ZipFile('spam.zip', 'w') as myzip:
    myzip.write(t)
    print(myzip.namelist())

# ну в принципе я засунул в zip, но думаю это неправильное решение