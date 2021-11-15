from sqlite3 import connect

with connect('school.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE students(name varchar, cpr int)')
    cur.execute('INSERT INTO students(name, cpr) VALUES("Claus", 2121)')
    for row in cur.execute('SELECT * FROM students'):
        print(row)

    #cur.execute('DROP TABLE students')

# setup and teardown action:
# * open connection to db
# * close connection to db
#
# * create a table
# * drop table
