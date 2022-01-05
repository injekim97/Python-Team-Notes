# 최솟값 구하기
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # python 에서 가장 큰 값이 저장됨, inf 무한대를 뜻 함


for i in range(len(arr)):
    if arr[i] < arrMin : # 5 < inf  ---->  3 < 5 ----> 7 < 3 ----> 9 < 3 ----> 2 < 3 ----> 5 < 2 ----> 2 < 2 ---> 6 < 2
        arrMin = arr[i]

print(arrMin)



# 최솟값 구하기 2
arr = [5,3,7,9,2,5,2,6]
arrMin = float('inf') # python 에서 가장 큰 값이 저장됨, inf 무한대를 뜻 함


for i in arr:
    if i < arrMin : # 5 < inf  ---->  3 < 5 ----> 7 < 3 ----> 9 < 3 ----> 2 < 3 ----> 5 < 2 ----> 2 < 2 ---> 6 < 2
        arrMin = i

print(arrMin)




# 최솟값 구하기 3
arr = [5,3,7,9,2,5,2,6]
arrMin = arr[0] 

for i in range(1,len(arr)):
    if arr[i] < arrMin : #  3 < 5 ----> 7 < 3 ----> 9 < 3 ----> 2 < 3 ----> 5 < 2 ----> 2 < 2 ---> 6 < 2
        arrMin = arr[i]

print(arrMin)