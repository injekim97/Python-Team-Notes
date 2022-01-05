# ---------- input --------------
N = int(input())  # N명의 학생의 수학점수
arr = list(map(int,input().split()))  #  각 학생의 수학점수인 N개
 
 
 
# Python 에서 round 함수 사용 X -> round_half_up 방식이 아닌 round_half_even 방식 이므로 값이 다름
# ★★★★★ 그렇기 때문에 아래와 같은 방법으로 0.5를 더한 후 int로 자료형 변환 -> 반올림 해줌 ★★★★★
ave=sum(arr)/N
ave=ave+0.5
ave=int(ave)



# ---------- output --------------
min = 2147000000
for i,v in enumerate(arr) :
    tmp = abs(v-ave) # 거리 구하기 위해서 list value - ave(평균)


    # e.g : avg : 74 == 73 75 75 75 라고 가정
    # tmp : 73-74 = 1 
    if tmp < min :
        min = tmp    # 1<21470000 이니 min 도 1 
        score = v    # score 변수에 그 해당 성적 점수 저장 73  
        res = i + 1  # 학생번호 

    
    # tmp : 다음 list의 값인 75-74 = 1 
    # tmp(1) == min(1)
    # v > score 로 하면 답이 여러개 있어도 75(O) 75 75 즉, 맨 처음에 나온 학생 번호가 값이 됨
    # 단,  v >= score로 하면  75 75 75(O) 즉, 마지막 학생 번호가 값이 됨
    elif tmp == min :
        if v > score : 
            score = v    # score 변수에 그 해당 성적 점수 저장 75  
            res = i + 1  # 학생번호 

print(ave,res)