import sqlite3
conn = sqlite3.connect('student.db')
cursor = conn.cursor()
sql3='''insert into zhiliaotang values(?,?,?,?)'''
cursor.execute(sql3,[3,'zhangsan',18,'66666'])
conn.commit()
conn.close()

info:swjtu.edu.cn
username:2016044858
passwd:swjtu2016