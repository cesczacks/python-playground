#--------------------------------
# 1. Function as return value
#--------------------------------
def calc_sum(*args):
    ax = 0
    for n in args:
        ax += n
    return ax

print(calc_sum(1, 3, 5))

# return a function in a function
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1, 3, 5)
print(f())

#--------------------------------
# 2. Closure
#--------------------------------
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())

#--------------------------------
# 3. Practice
#--------------------------------
def createCounter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
