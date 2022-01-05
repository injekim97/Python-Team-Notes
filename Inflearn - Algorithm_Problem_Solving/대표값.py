# ---------- input --------------
N = int(input())  # N명의 학생의 수학점수
arr = list(map(int,input().split()))  #  각 학생의 수학점수인 N개
 

# ---------- output -----------------
# Python 에서 round 함수 사용 X -> round_half_up 방식이 아닌 round_half_even 방식 이므로 값이 다름
# ★★★★★ 그렇기 때문에 아래와 같은 방법으로 0.5를 더한 후 int로 자료형 변환 -> 반올림 해줌 ★★★★★
avg = sum(arr) / N # 73.9
avg = avg +0.5
avg = int(avg)


ans = [i+1 for i,v in enumerate(arr) if avg > v]
idx = ans.pop()
print(avg,idx+1)