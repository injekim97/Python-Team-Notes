# https://leetcode.com/problems/rotate-image/
# 위 참고용 링크는 2차원 숫자배열 형태의 이미지 데이터를 시계방향으로 90도 회전하는 문제입니다.
#
# 이번 테스트에서는 시계방향이 아니라 반시계방향으로 90도 회전시키는 코드를 작성하십시오.
# 원본 문제와 달리 새 배열을 추가로 선언해도 괜찮습니다.
# 원본 문제와 달리 가로와 세로 크기가 서로 다를 수 있습니다. (즉, 정사각형이 아닐 수 있습니다)



def rotate90ccw(matrix):    
    if len(matrix) == 3 :
        arr = [[0] * len(matrix) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                arr[len(matrix)-1-j][i] = matrix[i][j]  

        return arr


    elif len(matrix) == 2 :
        arr = [[0] * len(matrix) for _ in range(3)]

        # 0 1 
        for i in range(len(matrix)):
            
            idx = 0
            # 0 1 2 
            for j in range(len(matrix),-1,-1):
                arr[idx][i] = matrix[i][j]  
                idx +=1

        return arr


    else :
        return matrix

print(rotate90ccw([[1]])); # [[1]]
print(rotate90ccw([[1, 2, 3], [4, 5, 6]])); # [[3, 6], [2, 5], [1, 4]]
print(rotate90ccw([[1, 2, 3], [4, 5, 6], [7, 8, 9]])); # [[3, 6, 9], [2, 5, 8], [1, 4, 7]]