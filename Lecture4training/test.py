a = "100010000101001000001111111111111111"
c = 0
mx = 0
b = False
s = ''
for i in range(len(a)):
    if a[i] == '0':
        mx = max(mx, c)
        c=0
        s+='0'
    else:
        c+=1

print('Zeros: '+s)
print((c))