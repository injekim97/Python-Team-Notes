import sys

# sys.stdin.readline().strip()을 변수 2개에 저장하기 위해선 map 함수를 사용해야함
# e.g: map(자료형,sys.stdin.readline().strip().split()) 
N,K = map(int,sys.stdin.readline().strip().split())



arr = [i for i in range(1,N+1)]   # 1부터 N까지의 number list  /  [1, 2, 3, 4, 5, 6, 7]


ans = []
index = 0
for i in range(N) :    
    # 인덱스를 통해 pop 하기 위해 e.g : N : 7 , K  : 3 
    # index = index + K - 1 즉, 3 -1 = 2 가 저장된다. arr[2] = 3이므로 삭제될 값이 맞다.
    index += K-1

    
    # arr : [1,2,4,5,7] 의 len 길이가 5, index 값이 6이라면, index 값을 재수정해서 한바퀴 돌아가게 함
    # index = 6 % 5 = 1 , index 값을 1로 수정함 그리고 나서 loop 돌다가 다 끝나면 종료
    # ★★★ 즉, 인덱스 번호가 arr 리스트 길이보다 클 때 %를 나눠서 다시 사이클을 돌리기 위함 ★★★
    if index >= len(arr) :
        index %= len(arr)
        
        
    # arr.pop(index)  , 인덱스는 0번째 부터 시작
    # e.g arr : [1, 2, 3, 4, 5, 6, 7]  ---> arr.pop(2) : arr 배열 2번 인덱스 삭제 
    # 즉, [3] 삭제후 [1,2,4,5,6,7]로 됨 --> arr.pop(4) : 3이 삭제되고 4번째 인덱스 삭제 [6]
    ans.append(str(arr.pop(index)))
    # print(ans) # ['3', '6', '2', '7', '5', '1', '4']


# ★★★ ", ".join(list) 명으로 하나씩 값을 꺼내어 output 조작 가능 ★★★
# print(", ".join(ans)) # 3, 6, 2, 7, 5, 1, 4
print("<", ", ".join(ans), ">", sep='')