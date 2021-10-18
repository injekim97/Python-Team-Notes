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

# ## <문제> 시각
# #### 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성해라. 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
#
# * 00시 00분 03초
# * 00시 13분 30초
#
# * 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각입니다.
# * 00시 02분 55초
# * 01시 27분 45초

# +
# 해결아이디어
# 24H * 60M * 60S = 86,400
# 즉, 3중 for 문을 이용해서 1씩 증가하여 86400에 까지 가면서 3이 있는지 확인 하면 된다.



hour = int(input())
cnt = 0


# 3중 for문 코드 돌아가는 순서는 i = 0, j = 0 k = 0~59 돈 후에, i = 0 j =1 , k = 0~59 순서
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
                    
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                
print(cnt)
