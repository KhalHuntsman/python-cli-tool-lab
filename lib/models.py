#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/9/2025
# Version: 1.1

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        """Mark the task as completed and print confirmation."""
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """Add a task to the user and print confirmation."""
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        """Return a task matching the given title, or None."""
        for task in self.tasks:
            if task.title == title:
                return task
        return None
