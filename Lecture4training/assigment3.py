a = "0000000100001001110001010000000000"
c = 0
mx = 0
b = False
for i in range(len(a)):
    if a[i] == '1':
        mx = max(c, mx)
        c = 0
        b = True
    else:
        if b:
            c += 1
print(mx)
for i in range(mx):
    print('0', end='')
