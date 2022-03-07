# 46

# 크리스티안 골드바흐는 모든 홀수인 합성수를 (소수 + 2×제곱수)로 나타낼 수 있다고 주장했습니다.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# 그러나 이 추측은 잘못되었음이 밝혀졌습니다.

# 위와 같은 방법으로 나타낼 수 없는 가장 작은 홀수 합성수는 얼마입니까?

from sympy import isprime

# 홀수인데  k 식으로 만들수 없는 홀수

odd_list = [] # 홀수 리스트
prime_list = [] # 소수 리스트
goldbach_list = [] #  k 리스트

# 소수 리스트
for n in range(1,10000):
    if n == 1 or isprime(n):
        prime_list.append(n)    

# k 리스트
for i in range(50):

    for n in prime_list:
        k = n + (2*(i**2))
        goldbach_list.append(k)

# k 리스트에 없는 홀수 찾기
for x in range(1,10000,2):
    # odd_list.append(x)
    if x not in goldbach_list:
        print(x)
        break # 가장 작은 수만 출력


