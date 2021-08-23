from utils.db import get_db


def delete_task_by_id(id):
    try:
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM todo WHERE id = ?"
        cursor.execute(query, [id])
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
