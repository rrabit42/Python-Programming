infile = open("phones.txt","r")
lines = infile.read()
print(lines)
infile.close()


infile = open("phones.txt","r")
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()
