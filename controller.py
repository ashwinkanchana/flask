from db import get_db


def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d


def get_all_task():
    try:
        db = get_db()
        cursor = db.cursor()
        query = '''
        SELECT id, title, description, status, created_at
        FROM todo
        ORDER BY created_at DESC
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        res = []
        for row in data:
            res.append(dict_factory(cursor, row))
        return res
    except:
        return False


def get_task_by_id(id):
    try:
        db = get_db()
        cursor = db.cursor()
        query = '''
        SELECT id, title, description, status, created_at
        FROM todo
        WHERE id = ?
        '''
        cursor.execute(query, [id])
        return dict_factory(cursor, cursor.fetchone())
    except:
        return False


def create_task(title, description):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO todo(title, description) VALUES (?, ?)"
        cursor.execute(query, [title, description])
        db.commit()
        return cursor.lastrowid
    except:
        return False


def update_task_by_id(id, title, description, status):
    try:
        db = get_db()
        cursor = db.cursor()
        query = '''
        UPDATE todo
        SET title = ?, description = ?, status = ?
        WHERE id = ?
        '''
        status = 1 if status else 0
        cursor.execute(query, [title, description, status, id])
        db.commit()
        return True
    except:
        return False


def delete_task_by_id(id):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM todo WHERE id = ?"
        cursor.execute(query, [id])
        db.commit()
        return True
    except:
        return False
