import sys
from collections import deque


# deque 사용
queue = deque([])

for _ in range(int(sys.stdin.readline().strip())):
    command = sys.stdin.readline().strip().split() # push 명령어 입력시 공백으로 split 구분 후 뒤에 정수만 넣기 위함

    if command[0] == "push" :
        queue.append(command[1])


    elif command[0] == "pop":
        if len(queue) == 0 :
            print(-1)
    
        # 가장 앞에 있는 정수를 빼고, 그 수를 출력
        # ★★★ deque 에서 pop 할땐 popleft()를 사용해야 함 ★★★
        else :
            print(queue.popleft())


    elif command[0] == "size" :
        print(len(queue))


    elif command[0] == "empty" :
        if len(queue) == 0 :
            print(1)
        
        else : 
            print(0)


    elif command[0] == "front":
        if len(queue) == 0 :
            print(-1)
    
        # 가장 앞에 있는 정수 출력하려면 큐에서 인덱스 0에 위치
        else :
            print(queue[0])


    elif command[0] == "back":
        if len(queue) == 0 :
            print(-1)

        # 가장 뒤에 있는 정수 출력하려면 큐에서 인덱스 -1에 위치
        else :
            print(queue[-1])