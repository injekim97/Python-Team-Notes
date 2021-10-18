#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 코딩 테스트 기본 입출력 양식

# 입력 예시 : 1 2 3 4 5
a = list(map(int,input().split()))
print(a)


# In[1]:


# 코딩 테스트 빠르게 입력 받기(시간 줄이는 것)
import sys

data = input(sys.stdin.readline().rstrip())
print(data)

