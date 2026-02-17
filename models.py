class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Task:
    def __init__(self, title, description, deadline, priority):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.status = "Pending"
