import sys

S  = list(sys.stdin.readline().strip())

idx = 0  # <,> 에 담겨진 단어들 이후의 인덱스를 저장하기 위한 변수 
location = 0 # e.g : <open>tag<close> -> <> 이후에 tag 에서 t부터 기억하여 tag 값을 뒤집어서 gat를 저장하기 위한 변수 

while idx < len(S) :

    # # 입력한 문자열을 처음부터 돌려 괄호 즉, "<" 를 만나면 ~
    if S[idx] == "<" :
        idx += 1

        # ">" 를 만날 때 까지 idx 증가   --> e.g : <open> 이라면 "open" -> 즉 idx = 2(o),3(p),4(e),5(n) 
        while S[idx] != ">" :
            idx += 1

        # 그런 후 <open 에 ">" 이후에 값을 돌려야 하기 때문에 idx += 1
        idx += 1


    # 괄호가 아닌 문자열 이나 숫자로 된 str 를 만난다면?    
    elif S[idx].isalnum():
        location = idx

        # e.g : <open>tag<close> --> t : 6 , a : 7 , g : 8  idx value 증가
        while idx < len(S) and S[idx].isalnum() :
            idx += 1

        tmp = S[location:idx] # e.g : <open>tag<close> 에 tag 를 뜻함 
        tmp.reverse() # tag -> gat
        S[location:idx] = tmp # <open>tag<close>에 tag에 gat로 바꾼 값을 넣음


    # 괄호도 아니고 알파벳 이나 숫자가 아니라면 ?
    # 그냥 인덱스값 증가
    else :
        idx += 1
        
print("".join(S))