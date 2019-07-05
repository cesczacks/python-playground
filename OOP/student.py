# (object) => extend
class Student(object):

    # constructor
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # public method
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        else:
            return "C"

bart = Student("bart", 11)
bart.gender = "male"

print(bart)
print(Student)
print(bart.gender)
bart.print_score()
print(bart.get_grade())
