# 40
# 소수점 뒤에 양의 정수를 차례대로 붙여 나가면 아래와 같은 무리수를 만들 수 있습니다.

# 0.123456789101112131415161718192021...

# 이 무리수의 소수점 아래 12번째 자리에는 1이 옵니다 (위에서 붉게 표시된 숫자).

# 소수점 아래 n번째 숫자를 dn이라고 했을 때, 아래 식의 값은 얼마입니까?

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

i=1;string=''
total = 1
pow_num = 6
while len(string)<10**pow_num: 
    string += str(i)
    i+=1

for i in range(pow_num+1):
    d_num = pow(10,i)

    print(d_num, string[d_num-1])
    total *= int(string[d_num-1])

print("total :",total)
