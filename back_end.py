import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY, 
    title TEXT, author TEXT, year INTEGER, isbn INTEGER)
    """)
    conn.commit()
    conn.close()


def insert(title: str, author: str, year: int, isbn: int):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO books VALUES (NULL, ?, ?, ?, ?)
    """, (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM books
    """)
    rows = cur.fetchall()
    conn.close()

    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM books
    WHERE title=? OR author=? OR year=? or isbn=?
    """, (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()

    return rows


def delete(book_id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM books 
    WHERE book_id=?
    """, (book_id,))
    conn.commit()
    conn.close()

def update(book_id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE books 
        SET title=?, author=?, year=?, isbn=?
        WHERE book_id = ?
        
        """, (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()


connect()
