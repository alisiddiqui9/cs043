
import database

db = database('data2.txt')
print(db.select_one('ali@gmail.com'))
