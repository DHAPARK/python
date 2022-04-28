'''
단어를 하나 읽어서 단어의 각 문자를 다른줄에 출력하는 프로그램 작성.ex) 사용자가 "Apple"면
A
p
p
l
e
와 같이 출력
'''

str1 = input("단어 하나 입력:")
for i in range(0,len(str1)):
    print(str1[i])