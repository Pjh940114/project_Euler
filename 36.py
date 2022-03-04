# 36
# 대칭수(palindrome)인 585는 2진수로 나타내도 10010010012가 되어 여전히 대칭수입니다.

# 10진법과 2진법으로 모두 대칭수인 1,000,000 미만 수의 합을 구하세요.

# (주의: 첫번째 자리가 0이면 대칭수가 아님)

# print(format(585, 'b')[0])

x = 1
total = 0
while x < 1000000:
    
    binary = format(x,'b')
    
    # print("10진수 :",x, end = ", ")
    # print("2진수 :", b_x)

    # if str(x) == str(x)[::-1]:
    #     print("{} 는 대칭 10진수".format(x))

    # if binary == binary[::-1]:
    #     print("{} 는 대칭 2진수".format(binary))
    
    
    if str(x) == str(x)[::-1] and binary == binary[::-1]: # [::-1] : 뒤집는다.
        # print("x : {}, binary : {}".format(x, binary))
        total += x

    x += 1

print("total :",total)