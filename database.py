import mysql.connector
conn=mysql.connector.connect(user='root',password='Benben^2011',database='shareluddage')
cursor=conn.cursor()
#cursor.execute('create table userTest (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into userTest (id, name) values (%s, %s)', ['4', 'Michael'])
cursor.rowcount
conn.commit()
cursor.close()
cursor=conn.cursor()
cursor.execute('select * from userTest where id=%s',('1',))
values=cursor.fetchall()
print(values)
cursor.close()
conn.close()