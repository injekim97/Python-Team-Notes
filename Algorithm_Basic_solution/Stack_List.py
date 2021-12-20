# 클래스를 사용하지 않고 풀면 사용자 정의 함수(def)에서 매개변수에 self 없이 넣어주면 된다.
# main에서 push나 pop등 각 명령어를 통한 수행을 할때 그냥 print(pop()), print(size())를 하면 된다.

import sys


def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        return -1
    else :
        return stack.pop()
        
def size():
    return len(stack)

def empty():
    if len(stack)==0:
        return 1
    else:
        return 0

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]





# ------------------------ main ------------------------
stack = []

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(command[1])
        
    elif command[0] == 'pop':
        print(pop())
        
    elif command[0] == 'size':
        print(size())
        
    elif command[0] == 'top':
        print(top())
        
    elif command[0] == 'empty':
        print(empty())