n=int(input())
s=list(map(int,input().split()))
for _ in range(n-1):
    pa=list(map(int,input().split()))
    cmb=[a+b for a in pa for b in s]
    fs=[float('inf')]*10
    for i in cmb:
        fs[i%10]=min(fs[i%10],i)
    s=[x for x in fs if x!=float('inf')]
q=[x for x in s if x%10!=6]
print(min(q))
