# 49

# 1487, 4817, 8147은 3330씩 늘어나는 등차수열입니다. 이 수열에는 특이한 점이 두 가지 있습니다.

# 세 수는 모두 소수입니다.
# 세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.
# 1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위엣것 말고도 또 다른 수열이 존재합니다.

# 그 수열의 세 항을 이었을 때 만들어지는 12자리 수는 무엇입니까?

# a,b,c 차가 같음
# b-a = c-b
# a,b,c 소수
# a b c 는 숫자 네개를 조합해서 만들 수 있음

from sympy import isprime

# 4자리 소수 리스트
prime_lists = []
for i in range(1000,10000):
    if isprime(i):
        prime_lists.append(i)

prime_lists.sort()

# 순열 확인, 정렬했을때 값이 같음
def is_sequence(a,b,c):
    sub_a = list(str(a))
    sub_a.sort()
    sub_b = list(str(b))
    sub_b.sort()
    sub_c = list(str(c))
    sub_c.sort()
    if sub_a == sub_b == sub_c:
        return True
    else:
        return False

# li = []
for a in prime_lists:
    for b in prime_lists:
        for c in prime_lists:
            if b-a == c-b and b-a != 0:
                if is_sequence(a,b,c):
                    if a < b < c:
                        print(str(a)+str(b)+str(c))
                        break

# print(max(li))
    