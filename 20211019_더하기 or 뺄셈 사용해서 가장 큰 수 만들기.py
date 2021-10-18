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

# ## <문제> 곱하기 혹은 더하기: 문제 설명
# #### 각 자리가 숫자(0~9)로만 이루엉진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' or '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수 프로그램을 작성해라
#
# * 단 +보다 x를 먼저 계산하는 방식이 아닌, 모든 연산은 왼쪽에서 부터 순서대로 이루어진다
# * e.g : 02984라는 문자열로 만들 수 있는 가장 큰수 는 ((((0+2) x 9) x 8) x 4) = 576이다.

# +
# 해결 아이디어 '+' 보단 'x'가 큰 수를 만들 수 있다.(그러나 0,1 즉 1이하 일 경우 '+'로 계산할 것)
# 어떻게든 아래의 솔루션 코드를 갈아 엎으려고 하였으나, 현재로썬 위에 코드가 최선이었다.


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])


for i in range(1,len(data)):
    
    # 두 수 중에서 하나라도 '0'  or '1' 인경우 '+' 수행
    num = int(data[i])
    
    if num <= 1 or result <= 1:
        result += num
        
    else :  result *= num
print(result)


