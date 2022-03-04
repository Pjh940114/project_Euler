# 42
# n번째 삼각수는 tn = ½ n (n + 1) 이라는 식으로 구할 수 있는데, 처음 10개는 아래와 같습니다.

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# 어떤 영어 단어에 대해서, 각 철자의 알파벳 순서(A=1, B=2, ..., Z=26)를 모두 더한 값을 '단어값'이라 부르기로 합니다. 예를 들어 'SKY'의 단어값은 19 + 11 + 25 = 55가 되는데, 이것은 우연히도 t10과 같습니다.
# 이렇게 어떤 단어의 단어값이 삼각수일 경우에는 이 단어를 '삼각단어'라 부르기로 합니다.

# 약 16KB의 텍스트 파일 words.txt에는 2000개 정도의 영어 단어가 수록되어 있습니다. 이 중에서 삼각단어는 모두 몇 개입니까?


with open ('words.txt') as data:
    words = data.read().replace('"','').split(',')
    words.sort()

# range 범위 구하기
max_value=0
for word in words:
    summ=0

    for i in word:
        summ+=ord(i)-64

    if summ > max_value:
        max_value = summ

# print(max_value)

x = 1
while max_value > x*(x+1)/2:
    x += 1

# 삼각수 리스트

tri_nums = []
sum_lists = []
count = 0
for n in range(x+1):
    tri_nums.append(n*(n+1)/2)

# 알파벳 합 구하기
for word in words:
    sum = 0
    
    for i in word:
        sum += ord(i)-64 # 알파벳에 해당하는 수의 합
    
    # 삼각수 리스트에 알파벳 함이 포함될 경우
    if sum in tri_nums:
        sum_lists.append(sum)
        count += 1

print("sum_lists :",sum_lists)
print("count :", count)
    


