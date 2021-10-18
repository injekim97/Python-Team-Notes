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
# 코딩 테스트 기본 입출력 양식

# 입력 예시 : 1 2 3 4 5
a = list(map(int,input().split()))
print(a)

# +
# 코딩 테스트 빠르게 입력 받기(시간 줄이는 것)
import sys

data = input(sys.stdin.readline().rstrip())
print(data)
