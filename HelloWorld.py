class Student:
    def __init__(self, name, job=None, time=0.00, time_effective=0.80): 
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective

    def count_time(self, hour, rate = 0.8):
        self.time += hour
        self.time_effective += hour * rate

# 请你完成子类的定制（包括初始化方法和count_time函数）
class Programmer(Student):
    job = 'programmer'

    def count_time(self, hour, rate = 1):
        self.time += hour
        self.time_effective += hour * rate



# 通过两个实例，完成子类和父类的对比（可自行验证）
student1 = Student('韩梅梅')
student2 = Programmer('李雷')

student1.count_time(10, 0.8)
print('%s - %s' %(student1.time, student1.time_effective))

student2.count_time(10, 1)
print('%s - %s' %(student2.time, student2.time_effective))