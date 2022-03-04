# 35
# 소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 원형 소수(circular prime)라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.

# 이런 소수는 100 미만에 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.

# 그러면 1,000,000 미만에는 모두 몇 개나 있을까요?

from sympy import isprime

x = 1
count = 0
circular_prime_list = []

while x < 1000000:
    if isprime(x):
        prime_string = str(x) # 문자로 변환
        is_circular_prime = True
        prime_len = len(prime_string)

        for i in range(1,prime_len):
            new_prime_string = prime_string[i:] + prime_string[:i]

            if not isprime(int(new_prime_string)):
                is_circular_prime = False
        
        if is_circular_prime:
            circular_prime_list.append(x)
            count += 1


    x += 1
    
print(circular_prime_list)
print("count :", count)