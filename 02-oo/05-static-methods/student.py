class Duration:
    def __init__(self, *, seconds):
        self.__seconds = seconds

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__seconds / 60

    @property
    def hours(self):
        return self.__seconds / 3600

    @staticmethod
    def from_seconds(amount):
        return Duration(seconds=amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(seconds=amount * 60)

    @staticmethod
    def from_hours(amount):
        return Duration(seconds=amount*3600)
