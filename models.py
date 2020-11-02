import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    #connect to database
    con = sql.connect(path.join(ROOT,'database.db'))

    cur = con.cursor()

    #add a row in database
    cur.execute('insert into posts(name,content) values(?,?)',(name,content))
    con.commit() #finalize the database entry
    con.close()  #close connection

def get_posts():
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    #get data from database
    cur.execute('select * from posts') 
    posts = cur.fetchall()
    return posts