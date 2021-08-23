from utils.db import get_db


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
    except Exception as e:
        print(e)
        return False
