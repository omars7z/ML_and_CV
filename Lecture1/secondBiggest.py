a = []
l = int(input("Num of elements in  the array: "))
for i in range(0, l):
    a.append(int(input()))


mx = a[0]
mx2 = 0
for i in range(1, len(a)):
    if(a[i]>mx):
        mx2 = mx
        mx = a[i]
    elif(a[i]>mx2 and a[i]!=mx):
        mx2 = a[i]
print(mx2)