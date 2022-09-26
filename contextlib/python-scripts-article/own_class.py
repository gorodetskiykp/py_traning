import sqlite3


class DataConn:

    def __init__(self, db_name):
        """Конструктор"""
        self.db_name = db_name

    def __enter__(self):
        """
        Открываем подключение с базой данных.
        """
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Закрываем подключение.
        """
        self.conn.close()
        if exc_val:
            raise


if __name__ == '__main__':
    db = 'test.db'

    with DataConn(db) as conn:
        cursor = conn.cursor()
