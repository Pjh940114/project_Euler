with open ('names.txt') as data:
    names = data.read().replace('"','').split(',')
    names.sort()


total = 0
for idx, name in enumerate(names):
    sum = 0
    
    for i in name:
        sum += ord(i)-64 # 알파벳에 해당하는 수의 합

    total += sum * (idx + 1)

print(total)

