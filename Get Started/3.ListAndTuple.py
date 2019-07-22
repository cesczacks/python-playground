#--------------------------------
# 1. List
#--------------------------------
classmates = ['Michael', 'Bob', 'Tracy']
# Print list
print(classmates)
# Get length
print(len(classmates))

# Get value from list
print(classmates[1])
print(classmates[-1])
print(classmates[0:2])

# Add
classmates.append("Adam")
print(classmates)
classmates.insert(1, "Jack")
print(classmates)

# Remove last
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)

# Replace with other values
classmates[1] = "Sarah"
print(classmates)

# List store different types
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

#--------------------------------
# 2. Tuple
#--------------------------------
# Similar to List, but cannot be changed
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

#--------------------------------
# 3. Practice
#--------------------------------
list_1 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(list_1[0][0])
print(list_1[1][1])
print(list_1[2][2])



















