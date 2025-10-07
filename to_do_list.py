"""
this is a todolist to be able to add,remove,show,save to do.
"""

import csv


class Task:
    """
    this class explaine simple to do
    """

    def __init__(self):
        self.my_dict = {
            "high priority": [],
            "medium priority": [],
            "low priority": [],
        }

    def information(self):
        "information what words how to work"
        print("welcome to my list")
        print("you can choise a level priority")
        print("level priority include high,medium,low")
        print("we can do (ADD, REMOVE, SHOW, LOAD, EXIT):")

    def __len__(self):
        return sum(len(tasks) for tasks in self.my_dict.values())


class Todolist:
    """This class handles the requests."""

    def __init__(self):
        self.task = Task()

    def add(self, tasks, priority):
        "this methode add tasks and priority to dictionery"
        if priority == "HIGH":
            self.task.my_dict["high priority"].append(tasks)
        elif priority == "MEDIUM":
            self.task.my_dict["medium priority"].append(tasks)
        elif priority == "LOW":
            self.task.my_dict["low priority"].append(tasks)
        else:
            print("invalid priority enter high medium low")
            return

        print("your task is added")

    def remove_task(self, tasks):
        "this methode remove what you say"
        found = False
        for priority_level, activity in self.task.my_dict.items():
            if tasks in activity:
                activity.remove(tasks)
                print(f"Task '{tasks}' removed from '{priority_level}'")
                found = True
                break
        if not found:
            print(f"Task '{tasks}' not found in any priority level.")

    def show_mywork(self):
        "this methode show all of the task"
        for priority, activity in self.task.my_dict.items():
            print(f"{priority}:")
            if activity:
                for tasks in activity:
                    print(f"  - {tasks}")
                print("")
            else:
                print("  No activity")
                print("")

    def save_to_csv(self, filename="to_do_list_csv.csv"):
        "this methode all task to save in csv file"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer_file = csv.writer(file)
            writer_file.writerow(["Priority", "Task"])
            for priority_level, tasks in self.task.my_dict.items():
                for tasks_name in tasks:
                    writer_file.writerow([priority_level, tasks_name])
        print(f"Tasks saved to {filename}")

    def load_from_csv(self, filename="to_do_list_csv.csv"):
        "this method loads tasks from csv file"
        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for key in self.task.my_dict:
                    self.task.my_dict[key] = []
                print("Priority".ljust(20), "Task")
                print("-" * 35)
                for row in reader:
                    if len(row) == 2:
                        priority, tasks = row
                        if priority in self.task.my_dict:
                            self.task.my_dict[priority].append(tasks)
                        print(priority.ljust(20), tasks)
            print(f"Tasks loaded from {filename}")
        except FileNotFoundError:
            print(f"No such file: {filename}")


my_list = Todolist()
my_list.task.information()
while True:
    print("")
    awn = input("what whoud you like do? ").upper()

    if awn == "ADD":
        task = input("write you task: ")
        priority = input("write your priority task: ").upper()
        my_list.add(task, priority)
        my_list.save_to_csv()

    elif awn == "REMOVE":
        task_name = input("write task name to remove: ").strip()
        my_list.remove_task(task_name)
        my_list.save_to_csv()

    elif awn == "SHOW":
        my_list.show_mywork()

    elif awn == "SAVE":
        my_list.save_to_csv()

    elif awn == "LOAD":
        my_list.load_from_csv()

    elif awn == "EXIT":
        print("have a good day")
        break

    else:
        print("invaild option. try again")

