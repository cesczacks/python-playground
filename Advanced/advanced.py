from functools import reduce
#--------------------------------
# 1. Map
#--------------------------------
def f(x):
    return x ** 2

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5])))

#--------------------------------
# 2. Reduce
#--------------------------------
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

#--------------------------------
# 3. Filter
#--------------------------------
nums = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(lambda x: x % 2 == 1, nums)))

#--------------------------------
# 4. Sort
#--------------------------------
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

# Practice 1
def normalize(name):
    return str(name[0]).upper() + str(name[1:]).lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(lambda name: str(name[0]).upper() + str(name[1:]).lower(), L1))
print(L2)

# Practice 2
def prod(L):
    return reduce(lambda x, y: x * y, L)

print(prod([3, 5, 7, 9]))

# Practice 3
def is_palindrome(n):
	n=str(n)
	if n==n[::-1]:
		return True
	else:
		return False

# Practice 4
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda x: x[0]))
print(sorted(L, key=lambda x: x[1], reverse=True))

