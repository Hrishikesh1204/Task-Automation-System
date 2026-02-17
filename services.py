from database import get_connection
from exceptions import InvalidDateFormat, TaskNotFound
import hashlib
from datetime import datetime

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, hash_password(password)))
        conn.commit()
        print("User registered successfully.")
    except:
        print("Username already exists.")
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise InvalidDateFormat("Date must be YYYY-MM-DD format")

def add_task(user_id, title, description, deadline, priority):
    validate_date(deadline)
    conn = get_connection()
    cursor = conn.cursor()
    created_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO tasks (user_id, title, description, created_date, deadline, priority, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, title, description, created_date, deadline, priority, "Pending"))

    conn.commit()
    conn.close()

def update_task(task_id, title, description, deadline, priority):
    validate_date(deadline)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET title=?, description=?, deadline=?, priority=?
    WHERE id=?
    """, (title, description, deadline, priority, task_id))

    if cursor.rowcount == 0:
        raise TaskNotFound("Task not found.")

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    if cursor.rowcount == 0:
        raise TaskNotFound("Task not found.")

    conn.commit()
    conn.close()

def mark_completed(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    completed_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    UPDATE tasks
    SET status='Completed', completed_date=?
    WHERE id=?
    """, (completed_date, task_id))

    if cursor.rowcount == 0:
        raise TaskNotFound("Task not found.")

    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def check_overdue(user_id):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM tasks
    WHERE user_id=? AND deadline < ? AND status='Pending'
    """, (user_id, today))

    overdue = cursor.fetchall()
    conn.close()
    return overdue

def completion_percentage(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE user_id=?", (user_id,))
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE user_id=? AND status='Completed'", (user_id,))
    completed = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        return 0

    return round((completed / total) * 100, 2)
