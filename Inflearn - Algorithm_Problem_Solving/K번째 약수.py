# input
N,K = map(int,input().split())

arr = [] 
for i in range(1,N+1) :
    if N % i == 0 :
        arr.append(i) # [1, 2, 3, 6]


# output
if len(arr) < K :
    print(-1)
    
else :
    print(arr[K-1])