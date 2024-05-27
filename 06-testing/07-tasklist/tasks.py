from datetime import date


class Task:
    def __init__(self, descripion, due_date):
        self.__description = descripion
        self.__due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date


class TaskList:
    def __init__(self):
        self.__task_list = []

    def __len__(self):
        return len(self.__task_list)

    def add_task(self, task):
        if task.due_date() < date.today():
            raise RuntimeError("Due date can not be in the past!")
        self.__task_list.append(task)

    def finished_tasks(self):
        return [task for task in self.__task_list if task.finished == True]

    def due_tasks(self):
        return [task for task in self.__task_list if task.finished == False]

    def overdue_tasks(self):
        return [task for task in self.__task_list if task.finished == False and task.due_date < date.today()]
