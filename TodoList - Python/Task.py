from _datetime import datetime
import threading


class Task:
    def __init__(self, name, description, deadline, status="In Process"):
        self.name, self.description, self.deadline, self.status = name, description, deadline, status
        self.deadline_check()

    def __str__(self):
        return "-->Task name: " + self.name + "\n   Task description: " + self.description + "\n   Task deadline " \
               + str(self.deadline) + "\n   Status: " + self.status

    def deadline_check(self):
        threading.Timer(1.0, self.deadline_check).start()
        if self.deadline < datetime.now() and self.status != "Accomplished":
            self.status = "Failed"

    def mark_task_complete(self):
        self.status = "Accomplished"
