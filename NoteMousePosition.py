from DataBaseEvents import DataBase

def note_mouse_position(position: tuple):
    db = DataBase().db
    s = db.cursor()
    s.execute("""INSERT INTO coordinates(x, y) VALUES (?, ?)""", position)
    db.commit()


