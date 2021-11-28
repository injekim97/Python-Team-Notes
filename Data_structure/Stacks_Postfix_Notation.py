#!/usr/bin/env python
# coding: utf-8

# ### 스택의 응용 수식의 후위 표기법
# 
# 
# 중위 표기법(infix notation)
# * 연산자가 피연산자들의 사이에 위치
# * e.g : (A + B) * (C + D)
# 즉 (A+B)(C+D)(*) 가 순서
# 
# 
# 
# 후위 표기법(postfix notation)
# * 연산자가 피연산자들의 뒤에 위치
# * 즉 A B + C D + *  (+ : 1, + : 2, * : 3)

# ### 중위 표현식 -> 후위 표현식 (스택 자료구조 이용)
# 
# 1) A * B + C 수식을 후위 표현식으로는 ?
# * [후위] A B * C +
# 
# 
# 2) A + B * C 수식을 후위 표현식으로는 ?
# * [후위] A B C * +

# ### 1) 중위 표현식을 후위 표현식으로 바꾸는 방법?
# 
# e.g  A * B + C 
# 
# * 왼쪽 부터 시작해서 피연산자들을 쭉 적음
# * 연산자(*,+,-,/)를 만나면 스택에 push
# 
# 후위 A B *  
# * 스택에는  S.push(*) ,  S.push(+)
# 
# * 우선 순위는 * 이 + 보다 높기 때문에 * pop 후
# * +는 스택에 넣음
# 
# 즉, 후위 A B * C +

# ### 2) 중위 표현식을 후위 표현식으로 바꾸는 방법?
# 
# e.g  A + B * C 
# 
# * 왼쪽 부터 시작해서 피연산자들을 쭉 적음
# * 연산자(*,+,-,/)를 만나면 스택에 push
# 
# 후위 A B C  
# * 스택에는  S.push(+) ,  S.push(*)
# 
# * 우선 순위는 * 이 + 보다 높기 때문에 스택에 +,*(맨 위에) 쌓여 있음
# 
# 
# 즉, 후위 A B C * +

# #### 3) 중위 표현식을 후위 표현식으로 바꾸는 방법? (동일한 연산자 일 경우)
# 
# e.g  A + B + C 
# * 왼쪽 부터 시작해서 피연산자들을 쭉 적음
# 
# 후위 A B +(스택에 먼저 들어 가 있는 것을 pop)
# 
# * 스택에는  S.push(+) 한 것을 먼저 pop 한 후
# * S.push(+) 동일한 연산자를 푸쉬함
# 
# 
# 즉, 후위 A B + C +

# ## 괄호의 처리
# 
# 중위 (A + B) * C   
# * 후위 AB + C *
# 
# 
# * 여는 괄호는 스택에 push
# * 닫는 괄호를 만나면 여는 괄호가 나올 때 까지 pop
# 
# 
# 
# 중위 A * (B + C)   
# * 후위 A B C + *
# * 연산자를 만났을 때, 여는 괄호 너머까지 pop 하지 않도록 
# * 여는 괄호의 우선순위는 가장 낮게 설정
# * 스택 맨 밑에는 * , ( , + 들어가 있음
# 

# ## 또 다른 예제 (중위 표현식을 후위 표현식으로)
# 1) (A + B) * (C + D) 
# * 후위 A B + C D + *
# 
# 
# 
# 2) (A + (B - C)) * D
# * 후위 A B C D + - *
# 
# 

# ### 알고리즘의 설계
# * 연산자의 우선순위 설정 (사칙연산 및 소괄호만 사용)

# In[5]:


# 사전(dict) 사용
# 3이 가장 높은 우선순위임 (3 > 2 > 1)

prec = {
    "*" : 3, "/" : 3,
    "+" : 2, "-" : 2,
    "(" : 1
}

print(prec)


# * 중위 표현식을 왼쪽부터 한 글자씩 읽어서
# * 피연산자(ABC) 라면 그냥 출력
# * '(' 이면 스택에 push
# * ')' 이면 '(' 이 나올 때까지 스택에서 pop, 출력
# * 연산자이면 스택에서 이보다 높(거나 같)은 우선 순위 것들을 pop으로 출력
# * 그리고 이 연산자는 스택에 push
# * 스택에 남아 있는 연산자는 모두 pop 로 출력

# ## 코드의 구현 - 힌트
# 
# 1) 스택의 맨 위에 있는 연산자와의 우선순위 비교
# * peek() 연산 이용 (꺼내지 않고 우선순위 높은지 낮은지 판단 가능)
# 
# 
# 2) 스택에 남아 있는 연산자 모두 pop() 하는 순환문
# * while not opStack.isEmpty():

# ## 연습문제 중위표현 수식 ---> 후위표현 수식

# In[7]:


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
   
    for c in S:
        if c == '(':
            opStack.push(c)
        
        elif c == ')':
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
    
        else:
            if c in prec:
                if opStack.isEmpty():
                    opStack.push(c)
               
                elif prec[opStack.peek()] >= prec[c]:
                    while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                        answer += opStack.pop()
                    opStack.push(c)
                else:
                    opStack.push(c)
            else:
                answer += c 
    
    while not opStack.isEmpty():
        answer += opStack.pop()
    
    return answer

