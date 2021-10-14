s = "for n = "
c = ", count = "
for n in range(1, 11):
    count = 0
    for i in range(1, n+1, 1):
        for j in range(1, i+1, 1):
            for k in range(1, j+1, 1):
                count+=1
    print(s + str(n) + c + str(count))
