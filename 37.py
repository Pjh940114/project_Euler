# 37
# 소수 3797에는 왼쪽부터 자릿수를 하나씩 없애거나 (3797, 797, 97, 7) 오른쪽부터 없애도 (3797, 379, 37, 3) 모두 소수가 되는 성질이 있습니다.

# 이런 성질을 가진 소수는 단 11개만이 존재합니다. 이것을 모두 찾아서 합을 구하세요.

# (참고: 2, 3, 5, 7은 제외합니다)

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