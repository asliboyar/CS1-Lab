num = input()
s = ''
for i in range (0, len(num)):
    if i!= 0:
        if num[i]==num[i-1]:
            continue
    
    p = 0
    for j in range (i, len(num)):
        if num[i]==num[j]:
            p+=1
        else:
            break
    s+='('+str(p)+', '+num[i]+')'+' '
print(s)
