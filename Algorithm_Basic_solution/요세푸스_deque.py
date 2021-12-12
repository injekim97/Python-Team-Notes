import sys
from collections import deque

N,K = map(int,sys.stdin.readline().strip().split())
people = deque([i for i in range(1,N+1)]) # deque([1, 2, 3, 4, 5, 6, 7])


ans = []
while people:

    # deque.rotate(num): 데크를 num만큼 회전한다 (양수면 오른쪽, 음수면 왼쪽).
    #  K-1만큼 왼쪽으로 회전 하기 위해 -(K-1) = -K+1  
    # e.g : K : 3, -K + 1 = -3 + 1 = -2 왼쪽으로 두개의 원소가 오른쪽으로 이동
    # deque([3, 4, 5, 6, 7, 1, 2])  


    # while loop logic
    # deque([3, 4, 5, 6, 7, 1, 2])  -> 3 ans에 넣고 pop , 맨 왼쪽 원소 2개 맨뒤로 보냄(rotate -2)라서
    # deque([6, 7, 1, 2, 4, 5,]) -> 6 ans에 넣고 pop, 왼쪽 두 개 맨 뒤로 보냄(rotate -2)
    # deque([2, 4, 5, 6, 7,1]) -> 2 ans에 넣고 pop, 왼쪽 두 개 맨 뒤로 보냄(rotate -2)
    # deque([7, 1, 4, 5,6]) -> 7 ans에 넣고 pop, 왼쪽 두 개 맨 뒤로 보냄(rotate -2)
    # deque([5,6,1, 4, ]) -> 5 ans에 넣고 pop, 왼쪽 두 개 맨 뒤로 보냄(rotate -2)
    people.rotate(-K+1)



    # e.g : deque([3, 4, 5, 6, 7, 1, 2])
    # ans에 인덱스 0인 3이 들어감
    ans.append(str(people[0]))   


    # ans에 값을 넣었으니까 popleft{}로 인덱스 0번째 pop 
    people.popleft()

print("<%s>" % (", ".join(ans)))


