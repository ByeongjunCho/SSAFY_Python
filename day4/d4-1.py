"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}


# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# 기본 풀이
result = 0
count = 0
for score_value in score.values():
    result += score_value
    count += 1
print(result/len(score))

# sum 함수 활용하기
result2 = sum(score.values())
count = len(score)
print(result2/count)
print(sum(score.values())/len(score))


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

total_score = 0
count = 0
for person_scores in scores.values():
    for score in person_scores.values():
        total_score += score
        count += 1

print(total_score/count)

sum_avg_stu = 0
for key in scores.keys():
    print(len(scores[key]))
    sum_avg_stu += sum(list(scores[key].values())) / len(scores[key])

print(sum_avg_stu)
print(sum_avg_stu/len(scores))
    


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
for name, temp in city.items():
    avg = sum(temp) / len(temp)
    print(avg)
    print(f'{name} : {avg: .2f}') # f-string : 3.6+
    print('{} : {:.2f}'.format(name, avg)) # format-string
    print(name + ' : ' + str(avg))

for avg_temp in city.items():
    print(f'{avg_temp[0]} : {sum(avg_temp[1])/len(avg_temp[1])}')



# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# 모든 지역의 온도를 모두 확인하면서, 
# 가장 낮은 온도라면, 해당 도시와 기온을 기록하고
# 더울때도, 해당 도시와 기온을 기록


min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
count = 0
for name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장하자. ~~중요하다.
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1
    if min(temp) < min_temp:
        min_city = name
        min_temp = min(temp)

    if max(temp) > max_temp:
        max_city = name
        max_temp = max(temp)

print(f'추운 곳은 {min_city}, 더운 곳은 {max_city}')





dict_max = {key : max(value) for key, value in city.items()} # 각 도시의 max온도
dict_min = {key : min(value) for key, value in city.items()} # 각 도시의 min온도

max_city = ""
min_city = ""
temp = 0


for key, value in dict_max.items():
    if value > temp:
        max_city = key
        temp = value
    else:
        max_city = max_city
        temp = temp


temp = 0
for key, value in dict_min.items():
    if value < temp:
        min_city = key
        temp = value
    else:
        min_city = min_city
        temp = temp

print(max_city)
print(min_city)
print(max(dict_max, key = dict_max.get))
print(min(dict_min, key = dict_min.get))


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

# in요소를 이용한 확인
if 2 in city['서울']:
    print('네')
else:
    print('아니오')

for temp in city['서울']:
    if temp == 2:
        seoul_2 = True
    else:
        seoul_2 = False

print(seoul_2)
