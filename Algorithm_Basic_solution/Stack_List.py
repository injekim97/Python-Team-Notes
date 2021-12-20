import sys

stack = []
for _ in range(int(sys.stdin.readline().strip())) :
    command = sys.stdin.readline().strip().split()  # split ->  push 1 을 공백으로 나누면 command[0] : push , command[1] : 1
    
    # for 문으로 통한 if 문으로 값을 반환 ---> print 문으로 출력
    # 기존 class에서는 def (사용자 정의함수)를 사용 ---> return 으로 반환
    if command[0] == "push" :
        stack.append(command[1])

    elif command[0] == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :    
            print(stack.pop())

    elif command[0] == "size" :
        print(len(stack))

    elif command[0] == "empty" :
        if len(stack) == 0 :
            print(1)

        else :
            print(0)

    elif command[0] == "top" :
        if len(stack) == 0 :
            print(-1)

        else :
            print(stack[-1])