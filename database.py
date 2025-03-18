import sqlite3

# Conexão com o banco de dados
def get_db():
    conn = sqlite3.connect('portfolio.db')
    conn.row_factory = sqlite3.Row
    return conn

# Cria a tabela (executado uma vez)
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Funções CRUD
def create_task(description: str, category: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (description, category) VALUES (?, ?)', (description, category))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def read_tasks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return [dict(task) for task in tasks]

def delete_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT task_id FROM tasks WHERE task_id = ?', (task_id,))
    task = cursor.fetchone()
    if task is None:
        conn.close()
        return False
    
    cursor.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
    conn.commit()
    conn.close()
    return True