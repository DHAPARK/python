'''
정수를 하나 읽어서 그 정수의 이진수 표현을 역순으로 출력하는 프로그램 작성
13 입력 시
1
0
1
1
출력
'''

number = int(input("숫자 : "))
def change(number):
    temp = []
    while True:
        one = int(number / 2)
        two = int(number % 2)
        temp.insert(0,two)

        if one != 0:
            number = one
        else:
            break
    result = ''.join(map(str,temp))
    
    return result[::-1]

list = change(number)
for i in list:
    print(i)