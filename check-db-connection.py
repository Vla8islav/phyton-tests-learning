import pymysql.cursors

connection = pymysql.connect(host='localhost', database='addressbook', user='root', password='', port=9906)

try:
    cursor = connection.cursor()
    cursor.execute('select * from group_list')
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()