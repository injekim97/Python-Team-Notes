import sys

# input 
sys.stdin = open("input.txt","rt") # txt file -> 6(N) 3(K)
N,K = map(int,input().split())


# output 
cnt = 0
for i in range(1,N+1) :
    # 6 % 1,2,3,4,5,6 == 0 이라면 약수 이므로 cnt += 1 증가
    if N % i == 0 :
        cnt += 1

    # K번째 약수가 발견 됐다면 ~
    if cnt == K :
        print(i)
        break

# 약수를 발견하지 못했다면 ~
else :
    print(-1)