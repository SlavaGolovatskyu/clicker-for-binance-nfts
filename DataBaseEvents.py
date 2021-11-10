import sqlite3

class DataBase: 
    def __init__(self) -> None:
        self.db = sqlite3.connect('data.db')
        self.s = self.db.cursor()

    def create_table_if_not_ex(self) -> None:
        self.s.execute("""CREATE TABLE IF NOT EXISTS coordinates(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                          x INT, y INT)""")
        self.db.commit()

    def clear_all_positions(self) -> None:
        self.s.execute("""DELETE FROM coordinates""")
        self.db.commit()

    def get_all_positions(self) -> list:
        positions = self.s.execute("""SELECT x, y FROM coordinates""").fetchall()
        pos = []
        for x, y in positions:
            pos.append(x)
            pos.append(y)
        return pos
        
    def delete_last_elem(self) -> str:
        try:
            last_elem = self.s.execute("""SELECT id FROM coordinates ORDER BY id DESC LIMIT 1""").fetchone()[0]
            self.s.execute("DELETE FROM coordinates WHERE id = (?)", (last_elem,))
            self.db.commit()
            msg = 'Success deleted'
        except TypeError:
            msg = 'Coords was not found in database. Coords not deleted.'

        return msg
