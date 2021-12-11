import sys
from collections import deque


deque_left = list(sys.stdin.readline().strip())  # deque - left , 문자열 입력시 바로 넣음
                                                 # ['a', 'b', 'c', 'a', 's', 'c']

deque_right = deque([])   # deque - right 



N = int(sys.stdin.readline().strip())
for i in range(N):
    command = sys.stdin.readline().strip()

    # 만약 명령문이 L(왼쪽으로 커서 한칸 이동) , deque_left 가 비어 있지 않다면?
    # 즉, 왼쪽 deque에서 pop을 한 값(deque_left.pop())을 ★★★ 오른쪽 deque에 append가 아닌 appendleft 로 추가 ★★★
    if command == "L" and deque_left :
        deque_right.appendleft(deque_left.pop())


    # 만약 명령문이 D(왼쪽으로 커서 한칸 이동) , deque_right 가 비어 있지 않다면?
    # 즉, 오른쪽 deque에서 pop을 한 값(deque_right.popleft())을 ★★★ 왼쪽 deque에 append로 추가 ★★★
    elif command == "D" and deque_right :
        deque_left.append(deque_right.popleft())


    # 만약 명령문이 B(왼쪽 문자 삭제), deque_left가 비어 있지 않다면?  
    # deque_left 에서 pop 해준다.  
    # 삭제하는 기능은 pop() 사용
    elif command == "B" and deque_left :
       deque_left.pop()
 
    # 추가하는 기능은 append 사용
    else:
        if command[0] == "P" :
            deque_left.append(command[2])
 

# print(deque_left) # ['a', 'b', 'c', 'd', 'y']
# print(deque_right) # deque(['x'])
print(''.join(deque_left + list(deque_right))) # abcdyx