a = [1, 2, 50, 3, 5, 7]
l = len(a)
print(len)

for i in range(l):
    print(a[i])
    if(a[i] > 3):
        a.append(0)
        l = len(a)
        print("len:", l)
print(a)
