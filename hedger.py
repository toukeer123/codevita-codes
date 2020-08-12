def hedger(n,k,a,profit,price,capita_inc,result):
    idx = profit.index(max(profit))
    val = price[idx]
    i=0
    for j in range(int(k)):
        if(a>capita_inc):
            if(a>=capita_inc+val):
                capita_inc = capita_inc+val
                result = result + ((val*profit[idx])/100)
        i+=1
    profit.pop(idx)
    price.pop(idx)
    print(i)
    if(profit != []):
        hedger(n,k,a,profit,price,capita_inc,result)
    else:
        print(int(result))
    
n , k , a = input().split()
N = float(n)
K = float(k)
A = float(a)
if(A>=0 and A<=(10**6)):
    if(K>=1 and K<=100):
        if(N>=1 and N<=(10**4)):
            price = list(map(float,input().split()))
            profit = list(map(float,input().split()))
            if(len(price)==N and len(profit)==N):
                capita_inc = 0
                result = 0
                hedger(N,K,A,profit,price,capita_inc,result)


