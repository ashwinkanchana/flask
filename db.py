import sqlite3
import json


DATABASE_NAME = "TODO.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS todo(
        id              INTEGER     PRIMARY KEY AUTOINCREMENT,
        title           TEXT        NOT NULL,
        description     TEXT,
        status          TINYINT     DEFAULT 0,
        created_at      DATETIME    DEFAULT CURRENT_TIMESTAMP,
        CHECK (status >= 0 AND status <= 1) 
        )
        '''    
    )
    print("Table created successfully")

    if not cursor.execute('SELECT COUNT(1) FROM todo').fetchone()[0]:
        fill_data()


def fill_data():
    try:
        with open('data.json') as mock_data:
            data = json.load(mock_data)
            db = get_db()
            cursor = db.cursor()
            for item in data:
                cursor.execute(
                    '''
                    INSERT INTO todo
                    (title, description, status)
                    VALUES (?, ?, ?);
                    ''',
                    [item['title'], item['description'], item['status']])
            db.commit()
            return True
    except Exception as e:
        print(str(e))
        return False
