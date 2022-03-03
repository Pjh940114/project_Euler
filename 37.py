def p_test(n): # 소수 판별
    if n < 2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False

    return True

def tp_test(n):
    prime_num = str(n)
    for i in range(len(prime_num)):
        if not p_test(int(prime_num[i:])): # 오른쪽부터 제거 했을 때
            return False

        if not p_test(int(prime_num[:i+1])): # 왼쪽부터 제거 했을 때
            return False

    return True

l = []
x = 10

while len(l) < 11: # 단 11개
    if tp_test(x):
        print(x)
        l.append(x)

    x += 1

print("sum :",sum(l))