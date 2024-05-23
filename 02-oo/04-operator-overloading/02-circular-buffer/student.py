class CircularBuffer:
    def __init__(self, n):
        self.__n = n
        self.__buffer_list = []

    def add(self, item):
        if len(self.__buffer_list) == self.__n:
            self.__buffer_list.pop(0)
            self.__buffer_list.append(item)
        else:
            self.__buffer_list.append(item)

    def __len__(self):
        return len(self.__buffer_list)

    def __getitem__(self, index):
        return self.__buffer_list[index]
