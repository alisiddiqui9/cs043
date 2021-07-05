
from lesson06 import database

database.insert('data2.txt','ali@gmail.com', 'Ali')
print(database.select_one('data2.txt','max@gmail.com'))