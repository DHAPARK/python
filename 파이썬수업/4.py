'''
    단어를 하나 읽어서 그 단어의 음절 수를 출력하는 프로그램 작성.
    다음과 같이 음절을 정의. a e i o u y
    모음들이 연속해 나오면 마지막 e를 제외하고
    전체를 하나의 음절로 취급.
    결과가 0이 나오면 1로 바꿈.
    테스트 케이스 ex)
    Harry 2
    hairy 2
    hare 1
    the 1
'''

word=input("문자열 입력 : ")
count=0
checkcnt=0
for w in word:
    if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u' or w=='y'):
        if checkcnt == 0:
            count += 1
        checkcnt += 1
    else:
        checkcnt = 0
if word[len(word)-1] == 'e':
    count -= 1

if count == 0:
    count = 1

print(count)