
from database import create_tables
from services import (
    register_user, login_user, add_task, get_tasks,
    update_task, delete_task, mark_completed,
    check_overdue, completion_percentage
)
from analytics import status_ratio, tasks_completed_per_week
from utils import export_to_csv, import_from_csv, backup_json
from exceptions import InvalidDateFormat, TaskNotFound

create_tables()

def display_tasks(tasks):
    print("\n--- Your Tasks ---")
    for task in tasks:
        print(f"""
ID: {task[0]}
Title: {task[2]}
Description: {task[3]}
Created: {task[4]}
Deadline: {task[5]}
Priority: {task[6]}
Status: {task[7]}
Completed Date: {task[8]}
        """)


while True:
    print("\n===== Task Automation System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        user = login_user(username, password)

        if user:
            print("Login successful.")
            user_id = user[0]

            while True:
                print("\n----- Dashboard -----")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Update Task")
                print("4. Delete Task")
                print("5. Mark Completed")
                print("6. Check Overdue Tasks")
                print("7. Show Completion %")
                print("8. Status Analytics")
                print("9. Weekly Completion Chart")
                print("10. Export to CSV")
                print("11. Import from CSV")
                print("12. Backup JSON")
                print("13. Logout")

                option = input("Choose option: ")

                try:
                    if option == "1":
                        title = input("Title: ")
                        desc = input("Description: ")
                        deadline = input("Deadline (YYYY-MM-DD): ")
                        priority = input("Priority (Low/Medium/High): ")
                        add_task(user_id, title, desc, deadline, priority)
                        print("Task added successfully.")

                    elif option == "2":
                        tasks = get_tasks(user_id)
                        display_tasks(tasks)

                    elif option == "3":
                        task_id = input("Task ID to update: ")
                        title = input("New Title: ")
                        desc = input("New Description: ")
                        deadline = input("New Deadline (YYYY-MM-DD): ")
                        priority = input("New Priority: ")
                        update_task(task_id, title, desc, deadline, priority)
                        print("Task updated successfully.")

                    elif option == "4":
                        task_id = input("Task ID to delete: ")
                        delete_task(task_id)
                        print("Task deleted successfully.")

                    elif option == "5":
                        task_id = input("Task ID to mark completed: ")
                        mark_completed(task_id)
                        print("Task marked as completed.")

                    elif option == "6":
                        overdue = check_overdue(user_id)
                        print("\n--- Overdue Tasks ---")
                        display_tasks(overdue)

                    elif option == "7":
                        percent = completion_percentage(user_id)
                        print(f"Completion Percentage: {percent}%")

                    elif option == "8":
                        status_ratio(user_id)

                    elif option == "9":
                        tasks_completed_per_week(user_id)

                    elif option == "10":
                        export_to_csv(user_id)
                        print("Exported successfully.")

                    elif option == "11":
                        import_from_csv(user_id)
                        print("Imported successfully.")

                    elif option == "12":
                        backup_json(user_id)
                        print("Backup completed.")

                    elif option == "13":
                        break

                except InvalidDateFormat as e:
                    print("Error:", e)

                except TaskNotFound as e:
                    print("Error:", e)

        else:
            print("Invalid credentials.")

    elif choice == "3":
        print("Exiting system...")
        break
