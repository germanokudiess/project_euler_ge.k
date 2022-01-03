t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = ((n-1)//3)
    j = ((n-1)//5)
    k = ((n-1)//15)
    print(int
((3*(int(((i)*(i+1)//2))))+
(5*(int(((j)*(j+1)//2))))-
(15*(int(((k)*(k+1)//2))))))
