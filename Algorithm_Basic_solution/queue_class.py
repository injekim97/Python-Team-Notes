import sys
from collections import deque



class queue():
    def __init__(self):
        self.queue = deque([])

    # ★★★ push 에서는 return 사용 X ★★★
    # 그냥 self.변수명.append(값) 으로 넣어줌
    def push(self, x):
        self.queue.append(x)


    # deque에서 가장 앞에 있는 정수 출력 하려면 popleft()
    def pop(self) :
        if len(self.queue) == 0 :
            return -1

        else :
            return self.queue.popleft()


    def size(self):
        return len(self.queue)


    def empty(self):
        if len(self.queue) == 0 :
            return 1

        else :
            return 0


    def front(self) :
        if len(self.queue) == 0 :
            return -1
        
        else :
            return self.queue[0]
            

    def back(self) :

        if len(self.queue) == 0 :
            return -1
        
        else :
            return self.queue[-1]



# --------------------- class을 호출하기 위한 main ------------ 
if __name__ == "__main__" :    

    # ★★★★★★ 클래스명으로 선언하지 않고 계속 queue2 = deque()로 해서 1시간동안 고생함. ★★★★★★
    queue2 = queue() # 꼭 ★★ 변수명 = 클래스명으로 해야함 ★★


    for _ in range(int(sys.stdin.readline().strip())):
        command = sys.stdin.readline().strip().split() # push 명령어 입력시 공백으로 split 구분 후 뒤에 정수만 넣기 위함
   
        if command[0] == "push" :
            queue2.push(command[1]) 

        elif command[0] == "pop":
            print(queue2.pop())

        elif command[0] == "size" :
            print(queue2.size())

        elif command[0] == "empty" :
            print(queue2.empty())

        elif command[0] == "front":
            print(queue2.front())

        elif command[0] == "back":
            print(queue2.back())