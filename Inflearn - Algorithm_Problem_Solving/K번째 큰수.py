# ----------- input ------------
N,K = map(int,input().split())
arr = list(map(int,input().split())) # [13, 15, 34, 23, 45, 65, 33, 11, 26, 42]


# ---------------output----------------
res = set()    # 중복 제거
for i in range(N) : # list index 0을 i부터 시작하여~  i(0 번쨰 index)
    for j in range(i+1,N): # 뒤에 부터 돌려야 하기 때문에 j(1 번쨰 index)
         for m in range(j+1,N) : # m (2 번쨰 index)
             res.add(arr[i]+arr[j]+arr[m])  # ★★★★★ set 자료형에 추가는 set.add(element) ★★★★★  
             

# sort 해야 하기 때문에 set -> list -> 내림차순 
res = list(res)
res.sort(reverse=True)
print(res[K-1])  