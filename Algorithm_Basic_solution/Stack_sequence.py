# constraint
# 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
# 위의 의미는 push 순서는 현재 만들어야 할 수열보다 작아질 수 없고 오직 current = target 혹은 current > target 의 뜻을 가짐
# 또, current는  current += 1씩 증가하면서 값을 넣으면 된다.



# input
# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 
# 단, 물론 같은 정수가 두 번 나오는 일은 없다.


# output 
#  필요한 연산을 한 줄에 한 개씩 출력한다. 
#  push연산은 +로, pop 연산은 -로 표현 , 불가능한 경우 NO를 출력한다.


# 입력값에 따른 출력값
# 1 2 3 4 + + + + 4까지 쌓임
# 1 2 (3 4) - - 4, 3 순으로 빠진다
# 1 2 5 6 + + 5, 6이 추가됨
# 1 2 5 (6) - 6이 빠짐
# 1 2 5 7 8 + + 7, 8이 추가됨
# 1 2 5 7 (8) - 8이 빠짐
# 1 2 5 (7) - 7이 빠짐
# (1 2 5) - - - 5, 2, 1 순으로 빠짐


max_num = 1 
stack , ans = [] , [] # ans = operation list 
flag = True  

n = int(input())
for i in range(n) :
    num = int(input())

    # 0 <= 4 일 경우 push 한 후, ans list에 "+" 저장
    while max_num <= num : 
        stack.append(max_num) # stack에 max_num을 넣어줌
        ans.append("+") # + + + + 
        max_num += 1 # +1씩 증가하여 e.g : 4 -> 1,2,3,4 저장 


    # stack에 있는 마지막 값이 num 값과 같다면 
    # e.g : stack = [1,2,3,4]  num = 4 -> 4를 pop 연산 후 ans list에 "-" 저장
    # stack의 마지막 값과 num을 비교 하여 같다면 pop
    if stack[-1] == num :
        stack.pop()
        ans.append("-")


    # stack의 마지막 값이 num과 같지 않다면 수열 성립 X
    else :
        flag = False

if flag == False :
    print("NO")

else :
    for i in ans: 
        print(i)        