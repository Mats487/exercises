class Queue:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def next(self):
        return self.__items.pop(0)

    def is_empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
