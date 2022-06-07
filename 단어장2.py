import random
import sys
import os
class VocaExam:
    #영어 문제 한글 답안 작성을위해 만들어둔 list입니다
    voca={}
    #한글 문제 영어 답안 작성을위해 만들어둔 list입니다
    voca2={}
    #정답갯수를 기록하기위한 변수
    score=0
    #문제의 답안을 가리키게 되는 변수
    number_answers=0
    #class의 생성자
    def __init__(self):
        while(True):
            #단어와 뜻을 (단어,뜻) 과 같이 입력하게되면
            sen = input("단어입력 ex)단어,뜻 :  프로그램 종료 : '끝' 입력")
            if(sen == '끝'):break
            
            eng=""
            mean=""
            try:
                #바로위에서 만들어진 eng,mean 변수에 각각 담겨서
                (eng,mean) = sen.split(",")
            except:
                print("단어,뜻 사이에 ,를 넣어 입력해주세요 다시.")
                continue
            #dictionary형태로 클래스 내부 리스트에 담기게 된다
            self.voca[eng] = mean
            #위는 영어 문제/ 한글답안 아래는 한글문제/영어답안을 위한 list이다
            self.voca2[mean] = eng
            
    def engKorTest(self):
        cnt = 0
        #영어문제 한글답안같은경우 voca list의 key들만 뽑아서 vocaKeyList에 담아둔다
        vocaKeyList = list(self.voca.keys())
        #단어의 갯수만큼 for문을 도리며
        for i in range(len(vocaKeyList)):
            randnum = i
            #바로위에서 만들어진 변수 randnum에 따라 문제가 출제된다
            question = vocaKeyList[randnum]
            #answer안에 내가입력한 답변이 들어가고
            answer = input("English to Korean: %s : ?"%(question))
            self.number_answers += 1
            #입력한 답변이 vocaKeyList dictionary의 해당 단어(key)의 value이면 참이다
            if answer == self.voca[question]:
                print("정답입니다.")
                cnt = cnt+1
                self.score+=1
            else:
                print("오답입니다.")
            #os모듈을 이용하여 console창을 clean해준다
            os.system('cls')
            #정답갯수를 출력하고 메서드가 끝난다
        print('정답갯수 : ',cnt ," / ",len(vocaKeyList))
    
    def korEngTest(self):
        #위와 동일
        cnt = 0
        vocaKeyList = list(self.voca2.keys())
        for i in range(len(vocaKeyList)):
            randnum = i
            
            question = vocaKeyList[randnum]
            answer = input("English to Korean: %s : ?"%(question))
            self.number_answers += 1
            if answer == self.voca2[question]:
                print("정답입니다.")
                cnt = cnt+1
                self.score+=1
            else:
                print("오답입니다.")
            os.system('cls')
        print('정답갯수 : ',cnt, " / " ,len(vocaKeyList))
        
        
    def update_voca_from_user_input(self):
        #새로운 단어장을 만들기 위해
        #영 - 한  ,   한 - 영 단어장 둘을 위한 list 2개를 만든다
        new_voca = {}
        new_voca2 = {}
        while(True):
            sen = input("단어입력 ex)단어,뜻 :  프로그램 종료 : '끝' 입력")
            #내가 '끝'을 입력하기 전까진 새로운 단어장 제작이 끝나지 않게 만들었으며
            #단어를 입력할때에는 (mean,eng) 역시나 콤마로 구분하게 해놓았다
            if(sen == '끝'):break
            eng=""
            mean=""
            try:
                #split 메서드로 ,로 mean 과 eng를 구분해주고
                (eng,mean) = sen.split(",")
            except:
                print("단어,뜻 사이에 ,를 넣어 입력해주세요 다시.")
                continue
            #하나하나 입력값들을 저장해준다
            new_voca[eng] = mean
            new_voca2[mean] = eng
        #class 내부 list에 직접적으로 새로만든 list의 인스턴스를 넣어준다.
        self.voca = new_voca
        self.voca2 = new_voca2
        print('새로운 단어장으로 업데이트 완료')
    
    
    def showAllList(self):
        #단어장의 모든 단어를 보여주기위해 self.voca.keys를 담아둔다
        keys = self.voca.keys()
        #key를 하나씩 꺼내어 key와 그 key와 대응되는 value를 출력한다
        for key in keys:
            print(key," : ",self.voca[key])

#6번을 누르기전까지는 문자열로 된 안내를 따라 단어장을 이용하게 된다
while(True):
    chNum = int(input("1 . 단어 입력 2 . 영 - 한 테스트 3 . 한 - 영 테스트 4 . 새로운 단어장 업데이트 5 . 모든 단어 보기 6 . 종료\n"))
    if chNum == 1:
        vocaexam = VocaExam()
    if chNum == 2:
        vocaexam.engKorTest()
    if chNum == 3:
        vocaexam.korEngTest()
    if chNum == 4:
        vocaexam.update_voca_from_user_input()
    if chNum == 5:
        vocaexam.showAllList()
    if chNum == 6:
        print("프로그램 정상적으로 종료")
        sys.exit(0)
