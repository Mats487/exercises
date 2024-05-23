class Account:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    def get_password(self):
        return self.__password

    def is_correct_password(self, pw):
        if self.get_password() == pw:
            return True
        else:
            return False
