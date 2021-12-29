# 문제 4
# ---------------
# 자연수 배열과 목표 자연수값(targetDiff) 하나를 입력으로 받아,
# 배열에서 임의의 두 원소를 골랐을 때 둘 간의 차이(절대값)이 목표 자연수값이 되는 두 원소를 찾는 효율적인 함수를 작성하십시오.
# 답이 여러 개면 하나만 리턴하면 되고, 답이 없으면 null을 리턴합니다.
#
# 예를 들어 배열이 [9, 7, 6, 4, 3]이고 targetDiff=4이면,
# 7과 3의 차이가 4이므로 7, 3을 출력하면 됩니다.
#
# 입력으로 들어온 array 외에 추가적인 컬렉션(해시맵, 해시셋, 딕셔너리 등)을 선언하지 않고 구현하면 가산점이 있습니다.
# 이 때, 단순 이중루프 전수조사보다 효율적인 알고리즘을 사용해 주세요.


# 해결 아이디어
# 우선 오름차순으로 배열을 정렬 -> sort 이용
# 임시 변수에 절대값으로 (fakeAnswer[0] - fakeAnswer[1]) 저장 후
# 2중 loop 선언

# 무차별대입이 아닌 fakeAnswer[0] + fakeAnswer[1] , fakeAnswer[0] + fakeAnswer[2] , fakeAnswer[0] + fakeAnswer[3] , fakeAnswer[0] + fakeAnswer[4] 
# fakeAnswer[1] + fakeAnswer[0] , fakeAnswer[1] + fakeAnswer[2], fakeAnswer[1] + fakeAnswer[3] , fakeAnswer[1] + fakeAnswer[4] (총 20번)


# fakeAnswer[1] + fakeAnswer[2], fakeAnswer[1] + fakeAnswer[3] , fakeAnswer[1] + fakeAnswer[4] 
# fakeAnswer[2] + fakeAnswer[3] , fakeAnswer[2] + fakeAnswer[4]
# fakeAnswer[3] + fakeAnswer[4] 로 총 10번만 loop 돌림 
def findPairOfDifference(array, targetDiff):
    array.sort()  
    fakeAnswer = array  # [3,4,6,7,9]

    # i = 0 -> 1 -> 2 -> 3 -> 4 (안에 for문에 의해 range 범위가(4,4) 이므로 종료)
    for i in range(0,len(fakeAnswer)):
  
        # j = 1 2 3 4 -> 2 3 4 -> 3 4 -> 4
        for j in range(i+1,len(fakeAnswer)) :
            tmp = abs(fakeAnswer[i] - fakeAnswer[j])

            if tmp == targetDiff :
                return fakeAnswer[i],fakeAnswer[j]
    

# test inputs and answers
print (findPairOfDifference([9, 6, 7, 4, 3], 4)) # 7, 3
print (findPairOfDifference([9, 6, 7, 4, 3], 1)) # 6, 7
print (findPairOfDifference([9, 6, 7, 4, 3], 7)) # null