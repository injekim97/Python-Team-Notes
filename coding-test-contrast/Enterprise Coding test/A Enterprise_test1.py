# 문제 1
# ---------------
# 수 a, b, x를 받아서 a, b 중에서 x와 더 가까운 수를 리턴하는 함수를 작성하십시오. 동률이면 a를 리턴합니다.
#
# * myFunction 대신 적절한 이름으로 함수명을 변경하시면 가산점이 있습니다.


# -----------------------------------------------------------------------------------------------------
# 해결 아이디어
# 1. 임시 변수 tmp 1, tmp2  2개 선언
# 2. 그런 후 if 문에서 tmp , tmp2 와 x를 비교하여 해당 값의 차이가 최솟값일 때의 데이터를 return 
def near_to_x(a, b, x):

    # tmp  TC1 : 0 , TC2 : 0.5 , TC3 : 0.6000000000000001
    tmp = abs(a-x)   
    
    # tmp2  TC1 : 1 , TC2 : 0.5 , TC3 : 0.3999999999999999
    tmp2 = abs(b-x)
    
    
    if tmp <= tmp2 :
        return a
    
    else :
        return b

# test inputs and answers
print (near_to_x(1, 2, 1)) # 1            
print (near_to_x(1, 2, 1.5)) # 1
print (near_to_x(1, 2, 1.6)) # 2