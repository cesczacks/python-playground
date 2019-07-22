print(type(123))
print(type(abs))
print(dir("123"))

for n in dir("123"):
    if n == 'lower':
        print(n)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        global count
        count += 1

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')