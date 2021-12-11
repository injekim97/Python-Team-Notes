import sys

left = list(sys.stdin.readline().strip().lower()) # 왼쪽 stack , 문자열 입력시 바로 리스트에 넣음
                                                  # e.g: abcd 입력 시 ['a', 'b', 'c', 'd']
right = []  # 오른쪽 stack 


N = int(sys.stdin.readline().strip())
for i in range(N) :
    command = sys.stdin.readline().strip()

    # 만약 명령문이 L(왼쪽으로 커서 한칸 이동) , left 스택이 비어 있지 않다면?
    # 즉, 왼쪽 스택 pop을 한 값(left.pop())을 오른쪽 스택에 추가한다.
    if command == "L" and left :
        right.append(left.pop())


    # 만약 명령문이 D(오른쪽으로 커서 한칸 이동) , right 스택이 비어 있지 않다면?
    # 즉, 오른쪽 스택 pop을 한 값(right.pop())을  왼쪽 스택에 추가한다.   
    elif command == "D" and right :
        left.append(right.pop())


    # 만약 명령문이 B(왼쪽 문자 삭제), left 스택이 비어 있지 않다면?  
    # 왼쪽 스택에서 pop 해준다. 
    elif command == "B" and left :
        left.pop()


    # 만약 명령문이 P(왼쪽에 문자 삽입), 왼쪽에 문자 삽입 OK
    else :
        # e.g : command : P X 라면 ?
        # print(command[0]) # p 
        # print(command[1]) # 공백
        # print(command[2]) # X 
        if command[0] == "P" :
            left.append(command[2])  
            
# print(left)  # ['a', 'b', 'c', 'd', 'y']
# print(right) # ['x']

# ★★★ stack에서 right stack은 reverse 해야 정상적으로 문자열이 출력되므로 [::-1] 로 뒤집어 준 후 출력 ★★★
print("".join(left + right[::-1]))   