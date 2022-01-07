# ------------- function ------------------
def digit_sum(x) :
    sum = 0
    while x > 0 :
        sum = sum + x % 10  # 125 -> 5 + 2 (12 % 10) + 1(1 % 10) 
        x = x // 10 # 125 -> 125 // 10 = 12   -> 12 // 10 = 1 
    
    return sum # e.g : 125 => 5 + 2 + 1 = 8 
    

# ------------- input ---------------
N = int(input())
x = list(map(int,input().split()))

tmp = 0
max = -2147000000
for i in x :
    tmp = digit_sum(i) # e.g : 125 -> 1 + 2 + 5 = 8 

    # 가장 큰 자리수를 찾아야 하기 때문에 임시 변수 tmp 선언 하여
    # 자릿수가 높은걸 계속 갱신 후 마지막에 출력
    if tmp > max :
        max = tmp  # 8
        result = i # 125 저장

print(result)