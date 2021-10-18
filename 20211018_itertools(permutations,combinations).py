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
# 순열(permutations) : r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)

from itertools import *

data = ['A','B','C']
result = list(permutations(data,3))
print(result)

# +
# 중복순열(product) :
from itertools import *

data = ['A','B','C']
result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

# +
# 중복조합(combinations_with_replacement
from itertools import *

data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)
