a = "00000001000100111000101"
c = 0
mx = 0
# b = False
for i in range(len(a)):
    if a[i] == '1':
        if a[i] == '0':
            c+=1
        else:
            mx = max(mx, c)
            c=0
print(mx)
for i in range(mx):
    print('0', end='')