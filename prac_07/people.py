class People:

    def __init__(self, first="", last="", age=0):
        self.first_name = first
        self.last_name = last
        self.age = age

    def __str__(self):
        return "{}, {}, {} added.".format(self.first_name, self.last_name, self.age)
