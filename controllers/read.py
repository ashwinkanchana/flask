from utils.db import get_db
from utils.dict_factory import dict_factory

def get_all_task():
    try:
        db = get_db()
        cursor = db.cursor()
        query = '''
        SELECT id, title, description, status, created_at, updated_at
        FROM todo
        ORDER BY created_at DESC
        '''
        cursor.execute(query)
        data = cursor.fetchall()
        res = []
        for row in data:
            print(row)
            res.append(dict_factory(cursor, row))
        return res
    except Exception as e:
        print(e)
        return False


def get_task_by_id(id):
    try:
        db = get_db()
        cursor = db.cursor()
        query = '''
        SELECT id, title, description, status, created_at, updated_at
        FROM todo
        WHERE id = ?
        '''
        cursor.execute(query, [id])
        return dict_factory(cursor, cursor.fetchone())
    except Exception as e:
        print(e)
        return False
