b=input()
c=0
d=0
for i in range(len(b)):
    if(b[i].isalpha() or b[i].isdigit()):
        c=c+1
    else:
        d=d+1
print(d)
