n=int(input())
frst=0
scnd=1
for i in range(n):
    print(scnd,end=" ")
    temp=frst
    frst=scnd
    scnd=temp+scnd
