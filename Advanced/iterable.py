from collections import Iterable, Iterator
#--------------------------------
# 1. Iterable
#--------------------------------
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(10, Iterable))

#--------------------------------
# 2. Iterator
#--------------------------------
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))

#--------------------------------
# 3. Covert from Iterable to Iterator
#--------------------------------
print(isinstance(iter([]), Iterator))

def looop(x):
    x = iter(x)
    while True:
        try:
            yield next(x)
        except StopIteration:
            break

print(looop([1, 3, 5, 7, 9]))



