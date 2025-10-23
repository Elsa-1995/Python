class User:

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_fl(self):
        return f'user: {self.first} {self.last}'
