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

# 리스트 컴프리헨션은 반복문 과 조건문을 동시에 병행해서 사용 가능 
arr = [i for i in range(20) if i % 2 == 1]
arr

# +
a = 4
b = 5

# 리스트 컴프리헨션은 코딩 테스트에서 2차원 리스트 초기화 할 때 매우 자주 사용함
arr2 = [[0] * a for _ in range(b)]
arr2
