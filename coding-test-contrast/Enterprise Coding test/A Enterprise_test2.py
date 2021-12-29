# 문제 2
# ---------------
# 콤마(,)로 구분된 정수들로 이루어진 문자열을 파싱하여
# 정수들의 합을 구하는 함수를 작성하십시오.
# 공백은 무시하면 되고, 형식이 잘못된 입력은 들어오지 않는다고 가정합니다.
#
# * myFunction 대신 적절한 이름으로 함수명을 변경하시면 가산점이 있습니다.


# 해결 아이디어
# 1. 매개 변수의 값이 공백("") 일 경우 0 으로 값 return
# 2. 매개 변수에 값이 콤마가 있다면 replace를 이용해서 "+" 로 바꾼 후 값 계산
def str_to_int(string):

    if string == "" :
        return 0
    
    else :        
        tmp = string.replace(",","+")
        return eval(tmp)


# test inputs and answers
print (str_to_int("")); # 0
print (str_to_int("3,4")); # 7
print (str_to_int(" -1, 1,0,  1, 1")); # 2


