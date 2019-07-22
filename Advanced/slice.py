# slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('Michael' in L)

# Get first three
print(L[0:3])
# Get 2 and 3
print(L[1:3])
# Get last one
print(L[-1])

numbers = list(range(100))
print(numbers[1:11:2])

# Practice
def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s

print(trim("   sss   "))
