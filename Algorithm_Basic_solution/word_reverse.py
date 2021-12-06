T = int(input())
for _ in range(T):
    word = list(map(str,input().split())) # ['I', 'am', 'happy', 'today']

    for i in word:
        print(i[::-1] , end = " ") #  I ma yppah yadot
        
    print() # 2개 이상 입력시 공백을 줘서 출력형식에 맞게 나오게 함