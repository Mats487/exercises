import re

class Book:
    def __init__(self, title, isbn):
        if not Book.__is_valid_title(title):
            raise RuntimeError("Invalid Title!")
        else: self.title = title
        if not Book.__is_valid_isbn(isbn):
            raise RuntimeError("Invalid ISBN!")
        else: self.isbn = isbn

    def __repr__(self):
        return f"title: {self.title}, isbn: {self.isbn}"

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value
    
    @staticmethod
    def __is_valid_title(value):
        if len(value) > 0:
            return True
        else: return False

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value
        
    @staticmethod
    def __is_valid_isbn(value):
        new_isbn = re.sub(r'\D', '', value)
        if len(new_isbn) == 13:
            checksum_array = [int(num) for num in new_isbn]
            multiplied_array = [checksum_array[i] * 3 if i % 2 ==
                                1 else checksum_array[i] for i in range(len(checksum_array))]
            if sum(multiplied_array) % 10 == 0:
                return True
            else:
                return False
        else:
            return False
        
print(Book('But You Have Friends', '978-1-60309-527-3'))