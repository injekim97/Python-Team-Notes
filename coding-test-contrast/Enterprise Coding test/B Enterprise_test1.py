# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def merge_sort(arr):
    N = len(arr)

    # 종료 조건: list length 1개 이하 시 종료 
    if N <= 1:
        return arr


    # 전체 arr list 을 그룹으로 나눠서 merge-sort  
    mid = N // 2       # 중간을 기준 -> 2개 list 나눔 
    left = arr[:mid]   # e.g  arr : 7 6 5 2 3 1 4   즉, left list -> arr[0:3] -> [7, 6, 5]
    right = arr[mid:]  # e.g  arr : 7 6 5 2 3 1 4   즉, right list -> arr[3:] -> [2, 3, 1, 4]
		
		
    # 재귀 호출로 left,right 나눈 값들 sort 정렬 
    merge_sort(left)  # 재귀 호출로 첫 번째 그룹을 정렬 -> [5,6,7]
    merge_sort(right)  # 재귀 호출로 두 번째 그룹을 정렬 -> [2.3.1.4]



    # ----------------two group merge sort -------------------------
    i, j, idx = 0, 0, 0

    # left list , right list 의 길이가 1 이상 일 때
    while i < len(left) and j < len(right) :
        
        if left[i] < right[j] :
            arr[idx] = left[i]   # arr list[0] = left[0]
            i += 1     # 다음 것을 비교하기 위해
            idx += 1   # 다음 것을 비교하기 위해

        else :
            arr[idx] = right[j]
            j += 1
            idx += 1
            
        
    # 남아 있는 data가 있으면 arr list에 add
    while i < len(left) :
        arr[idx] = left[i]
        i += 1
        idx += 1
    
    while j < len(right) :
        arr[idx] = right[j]
        j += 1
        idx += 1

# ------------------------- main --------------------------
N =  int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
merge_sort(arr)
print(*arr,end=" ")