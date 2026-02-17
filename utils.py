import csv
import json
from database import get_connection

def export_to_csv(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()

    with open("tasks_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

def import_from_csv(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    with open("tasks_export.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            cursor.execute("""
            INSERT INTO tasks (user_id, title, description, created_date, deadline, priority, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (user_id, row[2], row[3], row[4], row[5], row[6], row[7]))

    conn.commit()
    conn.close()

def backup_json(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()

    with open("backup.json", "w") as file:
        json.dump(tasks, file)
