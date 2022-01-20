def isPrime(x): 

    # 100 받으면 1이고, 1은 소수가 아니므로 False 
    if x == 1 :
        return False

    # e.g : 16 = 16 // 2 -> 8 
    # 2 ~ x(가져온 값을) // 2 나누는 것 까지 돌음
    for i in range(2,x//2) :
        if x % i == 0 :
            return False

    return True


# e.g : x = 9010 
def reverse(x):
    res = 0 

    # x 가 0보다 클 때 까지
    while x > 0 :
        t = x % 10    # 9010-> 901 -> 90 -> 9  
        res = res * 10 + t   # 0 * 10 + t(0) = 0 -> 0 * 10 + t(1) = 1, 1 * 10 + t(0) = 10, 10 * 10 + t(9) = 109
        x = x // 10 # 901 -> 90 -> 9 
    return res



# ---------------- main -------------------
N = int(input())

arr = list(map(int,input().split()))
for i in arr :
    tmp = reverse(i)

    if isPrime(tmp) :
        print(tmp, end= " ")