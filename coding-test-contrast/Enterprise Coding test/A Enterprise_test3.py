# 문제 3
# ---------------
# base3은 자연수를 3진수 문자열로 변환하는 미완성 함수입니다. TODO 대신 들어갈 한 줄 코드를 재귀호출을 포함하여 작성하십시오.

def base3(n):
    quotient = n // 3
    remainder = n % 3
    
    if quotient > 0:
        return str(base3(quotient)) + str(base3(remainder))
    else:
        return str(remainder)

# test inputs and answers
print (base3(0)) # "0"
print (base3(5)) # "12"
print (base3(10)) # "101"