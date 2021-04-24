def f(s,p):
    if (p==3 or p==5) and s<10:
        return True
    elif s>10 and p==5:
        return False
    elif s<10:
        return False
    if(p%2==1):
        if s%2==0:
            return f(s-1,p+1) and f(s-2,p+1) and f(s-3,p+1)and f(s-4,p+1) and f(s-5,p+1) and f(s//2,p+1)
        else:
            return f(s-1,p+1) and f(s-2,p+1) and f(s-3,p+1)and f(s-4,p+1) and f(s-5,p+1)
    else:
        if s%2==0:
            return f(s-1,p+1) or f(s-2,p+1) or f(s-3,p+1)or f(s-4,p+1) or f(s-5,p+1) or f(s//2,p+1)
        else:
            return f(s-1,p+1) or f(s-2,p+1) or f(s-3,p+1)or f(s-4,p+1) or f(s-5,p+1)
def ef(s,p):
    if p==3 and s<10:
        return True
    elif s>10 and p==3:
        return False
    elif s<10:
        return False
    if(p%2==1):
        if s%2==0:
            return ef(s-1,p+1) and ef(s-2,p+1) and ef(s-3,p+1)and ef(s-4,p+1) and ef(s-5,p+1) and ef(s//2,p+1)
        else:
            return ef(s-1,p+1) and ef(s-2,p+1) and ef(s-3,p+1)and ef(s-4,p+1) and ef(s-5,p+1)
    else:
        if s%2==0:
            return ef(s-1,p+1) or ef(s-2,p+1) or ef(s-3,p+1)or ef(s-4,p+1) or ef(s-5,p+1) or ef(s//2,p+1)
        else:
            return ef(s-1,p+1) or ef(s-2,p+1) or ef(s-3,p+1)or ef(s-4,p+1) or ef(s-5,p+1)

for i in range(10,1000):
    if f(i,1):
        print(i)
print("-----")
for i in range(10,1000):
    if ef(i,1):
        print(i)
