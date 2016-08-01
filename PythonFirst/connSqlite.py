Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('Create table user(id varchar(20) primary key, name vachar(20))')
<sqlite3.Cursor object at 0x0000000003517180>
>>> cursor.execute('insert into user(id, name) values (\'1\', \'Zooee\')')
<sqlite3.Cursor object at 0x0000000003517180>
>>> cursor.rowcount
1
>>> cursor.close()
>>> conn.commit()
>>> conn.close()
>>> conn = sqlite3.connect('tesat.db')
>>> cursor = conn.cu
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cursor = conn.cu
AttributeError: 'sqlite3.Connection' object has no attribute 'cu'
>>> cursor = connn.cursor()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cursor = connn.cursor()
NameError: name 'connn' is not defined
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id=?', ('1'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cursor.execute('select * from user where id=?', ('1'))
sqlite3.OperationalError: no such table: user
>>> cursor.execute('select * from user where id=?', ('1',))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cursor.execute('select * from user where id=?', ('1',))
sqlite3.OperationalError: no such table: user
>>> cursor.execute('select * from user where id=?', '1')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    cursor.execute('select * from user where id=?', '1')
sqlite3.OperationalError: no such table: user
>>> cursor.close
<built-in method close of sqlite3.Cursor object at 0x00000000035479D0>
>>> conn.close()
>>> conn = sqlite3.connect('test.db')
>>> cursor = conn.cursor()
>>> cursor.execute('select * from user where id = ?', ('1'))
<sqlite3.Cursor object at 0x0000000003517180>
>>> values = cursor.fetchall()
>>> values
[('1', 'Zooee')]
>>> cursor.close()
>>> conn.close()
>>> 
