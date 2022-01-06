N,M = map(int,input().split())
cnt = [0] * (N+M+2) # 눈의 합이 N+M 인데 넉넉하게 +2로 해줌 : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# cnt list에 두 눈 주사위(N,M) 의 합이 2,5,6,7,9 라면?
# cnt = [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0]
# 즉 cnt list에 합들을 count 하기 위함(2중 for문 N(4) * M(6) = 24번 돌아감)
# 4 -> 1~4 
for i in range(1,N+1) :
    # 6 -> 1~6   
    for j in range(1,M+1):
        cnt[i+j] += 1 



# cnt list에서 빈도 횟수 최대값 찾기
max = -2147000000   # min = 2147000000 , max = -2147000000

# 0~24까지 돌기 위함
for i in range(N+M+1):
    # cnt[0] > -2147000000 이라면 max에 cnt[0] 빈도 횟수 넣기, 계속 loop 구조
    if cnt[i] > max :
        max = cnt[i] 



# -----------output--------------
# cnt = [0, 0, 2, 3, 3, 2, 0, 2, 1, 1, 0, 0]
# index 에서 value 3 이라면 3,4 출력
for i in range(N+M+1):
    if cnt[i] == max : # 가장 큰 빈도수(두 눈의 합)
        print(i,end = " ")
