import sqlite3

# Conexão com o banco de dados
def get_db():
    conn = sqlite3.connect('portfolio.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicialização do banco de dados
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            active BOOL DEFAULT True
        );
                         
        INSERT INTO categories (name, color, active)
        SELECT 'General', '#fff', 1
        WHERE NOT EXISTS (
            SELECT 1 FROM categories WHERE name = 'General'
        );
        
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories (category_id)
        );
    ''')

    conn.commit()
    conn.close()

# Funções CRUD Tasks (ToDoList)
def create_task(description: str, category_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO tasks (description, category_id) VALUES (?, ?)', (description, category_id))
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

# Funções CRUD Categories (ToDoList)
def create_category(name: str, color: str):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO categories (name, color, active) VALUES (?, ?, 1)', (name, color))
    conn.commit()
    category_id = cursor.lastrowid

    conn.close()
    return category_id

def read_categories():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM categories')
    categories = cursor.fetchall()

    conn.close()
    return [dict(category) for category in categories]

def update_category(category_id: int, active: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT category_id FROM categories WHERE category_id = ?', (category_id,))
    category = cursor.fetchone()

    if category is None:
        conn.close()
        return "NotFound"

    cursor.execute('UPDATE categories SET active = ? WHERE category_id = ?', (active, category_id))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return "NotUpdated"

    conn.close()
    return "Success"