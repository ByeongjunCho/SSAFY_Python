# dictonary
# key - value
# key : string, interger, float, boolean
# list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.

lunch = {'중국집': '02-971-2312'}
print(lunch)
dinner = dict(한식='02-898-9585')
print(dinner)
bf = {}
bf['분식'] = '012-1252-5489'
print(bf)

menu = {'bf': bf, 'lunch': lunch, 'dinner': dinner}
# print(menu)
print(menu['bf']['분식'])

ssafy = dict(김은정='학생', 김인성='학생', 메시='축구선수')
for key in ssafy:
    print(ssafy[key])

# print(ssafy.items()) # (key, value)형태의 튜플로 이루어진 리스트를 반환한다.
for key, value in ssafy.items():
    print(key, value)

for value in ssafy.values():
    print(value)

for key in ssafy.keys():
    print(key)