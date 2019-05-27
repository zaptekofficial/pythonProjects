import Task
from _datetime import datetime
total_tasks = []


def create_task():
    name = input("Enter the name of your task")
    description = input("Enter the description of your task")
    deadline = datetime.strptime(input("Enter the deadline of your task "
                                       "in format Day-Month-Year Hour:Minute:Second"), "%d-%m-%Y %H:%M:%S")
    total_tasks.append(Task.Task(name, description, deadline))


answer = None

while answer != "EXIT":
    answer = input("For adding a new task: Enter T\n"
                   "For marking a task complete: Enter M\n"
                   "For viewing all tasks: Enter A\n"
                   "For exiting the program: Enter Exit\n"
                   "Input:").upper()
    if answer == "T":
        create_task()
    if answer == "M":
        user_input = input("Enter the name of the task:").upper()
        for i in total_tasks:
            if i.name.upper() == user_input:
                i.mark_task_complete()
    if answer == "A":
        for i in total_tasks:
            print(i)
        input("Enter any key to continue")


