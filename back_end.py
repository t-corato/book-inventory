import sqlite3


class BooksDatabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY, 
        title TEXT, author TEXT, year INTEGER, isbn INTEGER)
        """)
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("""
        INSERT INTO books VALUES (NULL, ?, ?, ?, ?)
        """, (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("""
        SELECT * FROM books
        """)
        rows = self.cur.fetchall()

        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("""
        SELECT * FROM books
        WHERE title=? OR author=? OR year=? or isbn=?
        """, (title, author, year, isbn))
        rows = self.cur.fetchall()

        return rows

    def delete(self, book_id):
        self.cur.execute("""
        DELETE FROM books 
        WHERE book_id=?
        """, (book_id,))
        self.conn.commit()

    def update(self, book_id, title, author, year, isbn):
        self.cur.execute("""
            UPDATE books 
            SET title=?, author=?, year=?, isbn=?
            WHERE book_id = ?
            
            """, (title, author, year, isbn, book_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
