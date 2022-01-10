N = int(input())
                    # index  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 115 16 17 18 19 20 
check_list = [0] * (N+1)  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 소수는 2부터 N까지 돌아야 함.
cnt = 0
for i in range(2,N+1):
    # check_list[2~N] 의 value 가 0이라면 소수 이므로 cnt += 1 
    if check_list[i] == 0 :
        cnt += 1

		# range(start,end,step(건너뜀)) , step 배수라고 생각
        # 2~20 까지의 2의 배수들을 전부 1로 값 지정함 -> 1은 소수가 아니라는 것을 뜻함
        for j in range(i,N+1,i) :
            check_list[j] = 1        

print(cnt)