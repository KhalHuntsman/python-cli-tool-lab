#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/9/2025
# Version:1.1

import argparse
from models import Task, User

# Global dictionary to store users
users = {}

def add_task(args):
    """Add a new task for the given user."""
    username = args.user
    title = args.title

    # Create user if missing
    if username not in users:
        users[username] = User(username)

    user = users[username]
    task = Task(title)
    user.add_task(task)

def complete_task(args):
    """Mark a user's task as complete."""
    username = args.user
    title = args.title

    # Check if user exists
    if username not in users:
        print("⚠️ User not found.")
        return

    user = users[username]
    task = user.get_task_by_title(title)

    if task is None:
        print("❌ Task not found.")
        return

    task.complete()

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Add task command
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Complete task command
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
