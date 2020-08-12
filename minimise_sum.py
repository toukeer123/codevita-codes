N,K = input().split()
n= int(N)
if(n>=1):
    k = int(K)
    A = list(map(int,input().split()))
    
    if(len(A) == n):
        if(k<=(10**5)):
            A.sort(reverse=True)
            arr = []
            for i in range(k):
                A[0] = int(A[0]/2)
                A.sort(reverse=True)
            print(sum(A))