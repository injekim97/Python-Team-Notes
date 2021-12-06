# 빠르게 입력하기 위한 sys 모듈 호출
import sys 


# stack 클래스 선언
# class 에선 무조건 self.stack.pop() 로 해줘야 한다. (stack.pop() X) : 런타임 에러 발생
# 또한 마찬가지로 print 할 때도 print(isEmpty()) 가 아닌 print(self.isEmpty())로 해줘야 함
class stack():

    # 빈 스택 초기화
    def __init__(self):
        self.stack = []

    # 스택에 원소(x) 삽입
    def push(self, x):
        self.stack.append(x)
        
    # 데이터 원소 삭제 (return)
    def pop(self):

        # 스택의 길이가 0이면 -1 출력
        if len(self.stack) == 0:
            return -1

        # 아니라면 stack에서 원소 꺼냄
        else:
            return self.stack.pop()

    
    # stack에 원소가 얼만큼 들어있는지 len으로 길이 체크
    def my_size(self):
        return len(self.stack)


    # stack이 비어있는지 확인하는 func
    def isEmpty(self):
        # 스택의 길이가 0(비어 있다면) 1을 호출
        if len(self.stack) == 0:
            return 1

        # 아니라면 0 
        else:
            return 0

    # 스택의 가장 위에 있는 정수 출력
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]




# ---------------------  main -----------------
# ★★★★★ class 호출하기 위해선 if __name__ == '__main__': 을 꼭 써줘야 한다 ★★★★★

if __name__ == '__main__':
    stack = stack()  # stack 이라는 변수명에 빈 스택 초기화

    
    # n = 명령의 수를 빠르게 입력받기 위해 sys 모듈 사용
    n = int(sys.stdin.readline())
    for i in range(n):
    
        command = sys.stdin.readline().split() # 명령어를 입력할 때 e.g: push 1 이면 split으로 공백을 나눠 push[0], 1[1]로 분리 
        if command[0] == 'push':
            stack.push(command[1])  # push 일때 e.g: push 1 이면 1의 값을 stack 에 저장하기 위함
            
        elif command[0] == 'pop':
            print(stack.pop())

        elif command[0] == 'size':
            print(stack.my_size())

        elif command[0] == 'empty':
            print(stack.isEmpty())

        elif command[0] == 'top':
            print(stack.top())