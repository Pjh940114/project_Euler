with open ('words.txt') as data:
    words = data.read().replace('"','').split(',')
    words.sort(reverse=True)

# range 범위 구하기
# max_value=0
# for word in words:
#     summ=0

#     for i in word:
#         summ+=ord(i)-64

#     if summ > max_value:
#         max_value = summ       
# print(max_value)
###########################

# 삼각수 리스트

tri_nums = []
sum_lists = []
count = 0
for n in range(21):
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
    


