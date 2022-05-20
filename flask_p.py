#import os
import psycopg2 as pg

conn = pg.connect(
    host = 'localhost',
    database = 'estudos',
    user = 'postgres',
    password = 'postgres'
)

cur = conn.cursor()

#cur.execute("DROP TABLE IF EXISTS books;")
cur.execute("CREATE TABLE IF NOT EXISTS books(id SERIAL PRIMARY KEY, title VARCHAR NOT NULL, author VARCHAR NOT NULL, pages_num INTEGER NOT NULL, review TEXT, date_added DATE  DEFAULT CURRENT_TIMESTAMP)")



# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('A Tale of Two Cities',
#              'Charles Dickens',
#              489,
#              'A great classic!')
#             )

# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )

# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('It',
#              'Stephen King',
#              1100,
#              'Thriller class!!!')
#             )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Acasos',
             'joseph Mazur',
             238,
             'História')
            )

conn.commit()

cur.close()
conn.close()