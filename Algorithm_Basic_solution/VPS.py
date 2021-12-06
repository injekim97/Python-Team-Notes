# vps  두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있음
# 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO


T = int(input())
for i in range(T) :
    vps = input()
    ans = 0

    for i in vps:
        if i == "(":
            ans += 1
    
        elif i == ")":
            ans -= 1

        # ans 값이 음수일 경우, 즉 괄호가 아닌 다른 것이 들어 왔을때-
        if ans < 0:
            break
    
    # (  -> 1
    # )  -> -1
    # ()를 더했을때 1 + -1 = 0 즉 정상적인 괄호일 때 0임
    # 그러므로 0일 땐 yes 
    if ans == 0:
        print("YES")
    
    # 아니면 NO
    else:
        print("NO")