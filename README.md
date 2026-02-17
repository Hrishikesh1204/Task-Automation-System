Smart Task Manager – Intelligent Productivity & Automation System

Project Overview

Smart Task Manager is a modular, console-based productivity application built using Python and SQLite.

The system helps users manage daily tasks efficiently while implementing intelligent automation features such as overdue detection, smart priority suggestions, and productivity analytics.

The project follows Object-Oriented Programming (OOP) principles and maintains a clean modular architecture separating models, services, database, and application logic.

🏗 Tech Stack

Python 3.10+

SQLite (Relational Database)

Matplotlib (Data Visualization)

Object-Oriented Programming (OOP)

CSV & JSON File Handling

📂 Project Structure
smart_task_manager/
│
├── models/
│   ├── user.py
│   └── task.py
│
├── services/
│   ├── auth_service.py
│   ├── task_service.py
│   ├── analytics_service.py
│   └── file_service.py
│
├── database/
│   └── db_connection.py
│
├── main.py
├── requirements.txt
└── README.md

✨ Core Features
🔐 User Management

Secure user registration

Login authentication

SHA256 password hashing

User data stored in SQLite database

📋 Task Management

Add new tasks

Update existing tasks

Delete tasks

Mark tasks as completed

Assign priority (Low / Medium / High)

Set deadline

Auto-generated Task ID

Created date & completed date tracking

🤖 Smart Automation

Automatic overdue task detection

Smart priority suggestion based on deadline proximity

Daily task completion summary

Completion percentage calculation

Automation Logic:

Tasks are marked overdue if deadline < current date.

Priority is suggested dynamically based on days remaining.

Completion percentage = (Completed Tasks / Total Tasks) × 100.

📊 Productivity Analytics

Weekly completed tasks chart (Matplotlib)

Pending vs Completed ratio visualization

Most productive day identification

Average task completion time calculation

These analytics provide meaningful productivity insights.

📁 File Handling System

Export tasks to CSV

Import tasks from CSV

JSON backup system for data safety
