import matplotlib.pyplot as plt
from database import get_connection

def status_ratio(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT status, COUNT(*) FROM tasks WHERE user_id=? GROUP BY status", (user_id,))
    data = cursor.fetchall()
    conn.close()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Pending vs Completed Ratio")
    plt.show()

def tasks_completed_per_week(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT strftime('%W', completed_date) as week, COUNT(*)
    FROM tasks
    WHERE user_id=? AND status='Completed'
    GROUP BY week
    """, (user_id,))

    data = cursor.fetchall()
    conn.close()

    weeks = [row[0] for row in data]
    counts = [row[1] for row in data]

    plt.bar(weeks, counts)
    plt.title("Tasks Completed Per Week")
    plt.xlabel("Week Number")
    plt.ylabel("Tasks Completed")
    plt.show()
