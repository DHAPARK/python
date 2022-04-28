'''
단엉를 하나 읽어서 그 단어의 모든 부분 문자열을 길이 순서대로 출력.
ex) rum 을 입력 시 
r
u
m
ru
um
rum
출력
'''

str1 = input("문자열 : ")
def get_all_sub(input_string):
    length = len(input_string)
    return [input_string[i:j + 1] for i in range(length) for j in range(i,length)]

list1=get_all_sub(str1)

for k in range(1,len(str1)+1):
    for i in list1:
        if len(i) == k:
            print(i)