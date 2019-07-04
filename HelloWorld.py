import sys
import hashlib

file = []
lines = []
for i in range(2):
    # open the files named in the command line
    file.append(open(sys.argv[1+i], 'r'))
    # stores the hash value and the line number for each line in file i
    lines.append({})
    # assuming you like counting lines starting with 1
    counter = 1
    while 1:
        # assuming default encoding is sufficient to handle the input file
        line = file[i].readline().encode()
        if not line: break
        hashcode = hashlib.sha512(line).hexdigest()
        lines[i][hashcode] = sys.argv[1+i]+': '+str(counter)
        counter += 1
unique0 = lines[0].keys() - lines[1].keys()
unique1 = lines[1].keys() - lines[0].keys()
result = [lines[0][x] for x in unique0] + [lines[1][x] for x in unique1]