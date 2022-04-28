'''
    단어를 하나 읽어서 그 단어에 나오는 모음 수를 출력
    모음 : a e i o u y
    ex) 사용자가 "Harry"입력 시 2 vowels 를 출력
'''

list1 = ["a","e","i","o","u","y"]
str1 = input("단어 하나를 입력:")
cnt = 0
for i in range(0,len(str1)):
    if str1[i] in list1:
        cnt+=1
print('%d vowels'%(cnt))