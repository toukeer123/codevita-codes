def prime(n):
    if n <=1 :
        return False
    if n <=3:
        return True
    else:
        for x in range(2,n):
            if(n%x==0):
                return False
        return True

d,p=map(int,input().split())
if(d>=10 and d<500):
    if(p>=2 and p<50):
        day_part=d/p
        buff=day_part
        x=0
        while buff>1:
            i=0
            count=0
            for j in range(p):
                num = (i*day_part)+buff

                if(num<=d):
                    if(prime(round((num)))):
                        count=count+1
                    if(i==(p-1)):
                        break
                    i=i+1
            if(count == p): 
                x=x+1       
            buff=buff-1
        print(x)