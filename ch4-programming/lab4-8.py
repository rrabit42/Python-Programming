for i range(4):
    for j in range(3):
        print("i = ", i, ",j = ", j)


for i in range(4):
    for j in range(3):
        print("i = ", i, ",j = ", j)
    print()


count = 0
for i in range(4):
    for j in range(3):
        count += 1
    print("count = ", count)


for i in range(4):
    count = 0
    for j in range(3):
        count += 1
    print("count = ", count)


count = 0
for i in range(4):
    for j in range(3):
        count += 1
print("count = ", count)