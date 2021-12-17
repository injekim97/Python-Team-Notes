# 10866 
import sys

class Deque():

    def __init__(self) :
        self.deque = []


    # 정수 X를 덱의 앞에 넣는다.
    def push_front(self,x):
        self.deque.insert(0,x)


    # 정수 x를 덱의 뒤에 넣는다. -> ★★★ append 사용하면 맨뒤에 붙음 ★★★
    def push_back(self,x):
        self.deque.append(x)


    # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop_front(self):

        if len(self.deque) == 0 :
            return -1
        
        else :
            return self.deque.pop(0)

    # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.
    # 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop_back(self):

        if len(self.deque) == 0 :
            return -1
        
        else :
            return self.deque.pop(-1)

    
    # 덱에 들어있는 정수의 개수를 출력한다.
    def size(self) :
        return len(self.deque)
    

    # 덱이 비어있으면 1을, 아니면 0을 출력한다.
    def empty(self):
        if len(self.deque) == 0 :
            return 1

        else :
            return 0

    
    # 덱의 가장 앞에 있는 정수를 출력한다. 
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def front(self):
        if len(self.deque) == 0 :
            return -1

        else :
            return self.deque[0]

    # 덱의 가장 뒤에 있는 정수를 출력한다. 
    # 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def back(self):
        if len(self.deque) == 0 :
            return -1

        else :
            return self.deque[-1]




# --------------------- class을 호출하기 위한 main ----------------------
if __name__ == "__main__" :    

    deque = Deque() # 꼭 ★★ 변수명 = 클래스명으로 해야함 ★★

    for _ in range(int(sys.stdin.readline().strip())):
        command = sys.stdin.readline().strip().split() # push 명령어 입력시 공백으로 split 구분 후 뒤에 정수만 넣기 위함
   
        if command[0] == "push_front" :
            deque.push_front(command[1]) 

        elif command[0] == "push_back" :
            deque.push_back(command[1]) 

        elif command[0] == "pop_front":
            print(deque.pop_front())

        elif command[0] == "pop_back":
            print(deque.pop_back())

        elif command[0] == "size" :
            print(deque.size())

        elif command[0] == "empty":
            print(deque.empty())

        elif command[0] == "front":
            print(deque.front())

        elif command[0] == "back":
            print(deque.back())