class Student(object):

    def __init__(self, name, score, gender = "male"):
        # private class variables (__XXX)
        self.__name = name
        self.__score = score
        self.gender = gender

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score

bart = Student("bart Simpson", 59)
cesc = Student("cesc Fabregas", 99)
# public variable
print(cesc.gender)
# call get method
print(cesc.get_score())
# call set method
cesc.set_score(100)
print(cesc.get_score())

## Practice
class Player(object):
    
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


