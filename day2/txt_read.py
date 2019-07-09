with open('ssafy_with.txt', 'r') as f:
    # readlines는 라인을 각각 리스트의 원소로 가지고 온다.
    lines = f.readlines()    
    for line in lines:  # lines는 리스트이기 때문에 반복문이 필요하다.
        print(line.strip())  # line.strip() : 개행문자 제거

with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt) 
print(type(txt))