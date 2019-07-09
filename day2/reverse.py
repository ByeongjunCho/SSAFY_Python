# number.txt를 읽어서
# 리스트 (readlines)
with open('numbers.txt', 'r') as f:
    num = f.readlines()

print(num)


with open('number_reverse.txt', 'w') as f:
    for n in range(len(num)):
        f.write(num[len(num)-n-1])


with open('number_reverse.txt', 'w') as f:
    # 리스트를 뒤집는다.
    num = reversed(num)
    # num.reverse()
    for n in num:
        f.write(n)



# number_reverse.txt로 저장한다.
# 4
# 3
# 2
# 1
# 0
