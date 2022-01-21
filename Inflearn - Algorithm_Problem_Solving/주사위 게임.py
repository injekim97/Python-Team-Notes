# ------------- input ---------------
tmp = [0] * 7
N = int(input())    
for i in range(N) :
    dice = list(map(int,input().split()))           # e.g : 1 2 3

    for j in dice : 
        tmp[j] += 1  # [0, 1, 1, 1, 1, 1, 1]



# ------------- output ---------------
# 해당 로직은 N = 1 일 때만 값이 정상적으로 출력됨 ㅠㅠ 3개를 넣으면 안됨
res = []
for i,v in enumerate(tmp) :
    if v == 3 :
        res.append(10000 + ((i) * 1000))

    elif v == 2 :
        res.append(1000 + (i) * (100))

    # v == 1 이라면 -> 즉 3개의 주사위 중 각 다른 눈이 나온다면
    else :
        last = len(tmp) - tmp[::-1].index(max(tmp)) -1   # 6 - 
        res.append(last * 100)
print(max(res))