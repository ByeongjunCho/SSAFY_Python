'''
# 문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str_ex = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.
print(f'문자열의 첫 부분: {str_ex[0]}, 문자열의 마지막 부분: {str_ex[-1]}') # -1 인덱스 접근은 가장 마지막이다.
# 0
# apple
#     -1
'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
# print(num+1) or range(1, numbers + 1)
for num in range(1, numbers+1):
    print(num, end='\n')

'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
def check_num(num):
    if num%2: # num%2 == 0
        print(f'숫자 {num}는 홀수입니다.')
    else:
        print(f'숫자 {num}는 짝수입니다.')
    # if not num%2: # num%2 == 0
    #     print(f'숫자 {num}는 짝수입니다.')
    # else:
    #     print(f'숫자 {num}는 홀수입니다.')
check_num(number)
'''
문제 4.
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))
# 위의 4줄의 주석을 풀고 아래에 코드를 작성해 주세요.

def check_pass(kor, eng, mat, sci):
    if kor >= 90 and eng > 80 and mat > 85 and sci >= 80:
        print(True)
    else: 
        print(False)

check_pass(a, b, c, d)
'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램100을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 위의 주석을 풀고 아래에 코드를 작성해 주세요.
prices = prices.split(';')  # split('기준값')

# 1. 반복문
prices_int = []
for string in prices:
    prices_int.append(int(string))
print(sorted(prices_int))
# 2. list comprehension
prices = [int(x) for x in prices]

# 3. map : 첫번째 인자의 함수를 두번째 인자를 반복하며 적용.
# 반복가능한 객체에 함수를 각각 적용.
prices = map(int, prices)  # 객체형 반환, 즉 메모리에 올라가 있는 것이 아니라 주소만 가지고 있음.
print(sorted(prices, reverse=True))
# prices.sort()
# print(prices)
# prices_int.reverse()
# reversed(prices)
# .sort() : return이 None. 원본 리스트 자체를 변경
# sorted(list) : return이 정렬된 리스트. 원본 자체는 변경하지 않음.