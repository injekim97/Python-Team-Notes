# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
n = 1260
cnt = 0 # 동전 개수 count 변수


arr = [500,100,50,10] # 그리디 알고리즘은 큰 단위부터 작은 단위로 해야 최적의 해를 구할 수 있음


# 1260원 --> 500원으로 먼저 최대한 나눠서 500원 2개, 260원을 100원으로 최대한 나눠서 2개, 남은 60원은 50원 1개, 10원 1개 
for coin in arr:
    cnt += n // coin 
    n %= coin # % 나머지 연산자로 1260원에 대해 리스트로 나눠줘야 정확한 동전의 개수가 나옴.
    
print("n을 동전으로 거슬러 줄 수 있는 동전 개수:",cnt)     

# +
n = 1260
cnt = 0

test_arr = [100,500,50,10] # 만약에 리스트 선언 시 작은 단위에서 큰 단위로 적는다면?

for coin in test_arr:
    cnt += n // coin
    n %= coin
    
print("n을 동전으로 거슬러 줄 수 있는 동전 개수:",cnt) # 같은 로직이지만 위의 코드와 달리 동전 개수가 달라짐
# -

# ## <문제> 1이 될 때까지 
# ##### 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려 한다.
# ##### 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다
#
# * 1. N에서 1을 뺀다
# * 2. N을 K로 나눈다.
#
#
# ##### 예를 들어 N = 17,K = 4 라고 가정. 이때 1번의 과정을 한 번 수행하면 N은 16, 이후에 2번 과정 수행하면 N은 1
# ##### 결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 됨. 이는 N을 1로 만드는 최소 횟수
# ##### N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프포그램 작성해라.
#
#
#
# + 입력 조건 : 첫째 줄에 N(1<=N<=100000)과 K(2<=K<=100000) 공백 기준으로 하여 각각 자연수가 주어짐
# + 출력 조건 : 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번 과정을 수행하는 최솟값 횟수 출력
#
#
# * 입력 예시 25 5
# * 출력 예시 2

# +
# 주어진 N 최대한 많이 나누기
# N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1 빼는 것 보다 횟수를 많이 줄일 수 있음

import time
start_time = time.time() # 측정 시작



n,k = 25,5
#n,k = list(map(int,input().split()))
result = 0


while True :    
    # N이 k로 나누어 떨어지는 수가 될 떄까지만 -1 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break
        
    result += 1
    n //= k

result += (n - 1)
print(result)


end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

# +
# 주어진 N 최대한 많이 나누기
# N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1 빼는 것 보다 횟수를 많이 줄일 수 있음
# 내가 푼 소스코드


import time
start_time = time.time() # 측정 시작


N,K = 25,5
#N,K = list(map(int,input().split()))
result = 0

while True :    
    
    target = (N // K) * K # 25 5 -> 25
    result += (N - target)  # 25 - 25 = 0, 5-5= 0  즉 항상 0이 되므로 전혀 지장이 없음, 그렇기 때문에 아래 result += 1 이 계속 증가됨
    
    # N이 K보다 작다면 종료
    if N < K:
        break
        
    result += 1
    N =  N // K # 25 // 5  = 5 , 5 // 5 = 0

print(result-1)

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
