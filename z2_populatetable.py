import sqlite3 as sql
conn=sql.connect('databasefile.db')
cr=conn.cursor()

def add_movie(title, director,year,genre):
    cr.execute("""
               INSERT INTO movies (title,director,year,genre)
               VALUES (?,?,?,?)""",(title,director,year,genre)
               )
    conn.commit
    print("Movie added :)")

add_movie("Inception","Christopher Nolan",2010,"Sci-Fi")
