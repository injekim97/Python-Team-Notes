def isPrime(N):
    for i in range(2, N):
        # N(입력 값) % 2,3,4,5,6~N == 0
        #  즉, 나머지연산자로 나눴을 때 0으로 떨어진다면 약수이므로 소수가 아님 -> False
        if N % i == 0:
            return False

    # 나머지는 소수
    return True
    
    
    

# ----------------------------- main ------------------------------
N = int(input())

# 소수는 2부터 판별하면 되므로 2~N 만큼 for loop 
cnt = 0
for i in range(2,N+1):
    if isPrime(i):
        cnt += 1

print(cnt)