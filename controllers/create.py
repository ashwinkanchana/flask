from utils.db import get_db


def create_task(title, description):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO todo(title, description) VALUES (?, ?)"
        cursor.execute(query, [title, description])
        db.commit()
        return cursor.lastrowid
    except Exception as e:
        print(e)
        return False
