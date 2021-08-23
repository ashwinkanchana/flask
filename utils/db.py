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
        created_at      DATETIME, 
        updated_at      DATETIME,    
        CHECK (status >= 0 AND status <= 1) 
        )
        '''
    )
    cursor.execute(
        '''
            CREATE TRIGGER IF NOT EXISTS created_at_trigger
                AFTER INSERT
                ON todo
                FOR EACH ROW 
            BEGIN
                UPDATE todo SET created_at=CURRENT_TIMESTAMP WHERE id=NEW.id;
            END;
            '''
    )

    cursor.execute(
        '''
        CREATE TRIGGER IF NOT EXISTS updated_at_trigger
        AFTER UPDATE
        ON todo
        FOR EACH ROW
        BEGIN
            UPDATE todo SET updated_at=CURRENT_TIMESTAMP WHERE id=OLD.id;
        END;
        '''
    )
    print("Table created successfully")


    if cursor.execute('SELECT COUNT(1) FROM todo').fetchone()[0] == 0:
        insert_mock_data()


def insert_mock_data():
    try:
        with open('./utils/data.json') as mock_data:
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
        print(e)
        return False


    
