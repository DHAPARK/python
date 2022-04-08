import random
class VocaExam:
    voca={}
    score=0
    number_answers=0
    def __init__(self):
        while(True):
            sen = input("단어입력 ex)단어,뜻 :  프로그램 종료 : '끝' 입력")
    
            if(sen == '끝'):break
            eng=""
            mean=""
            try:
                (eng,mean) = sen.split(",")
            except:
                print("단어,뜻 사이에 ,를 넣어 입력해주세요 다시.")
                continue
            self.voca[eng] = mean
            
            
    def test(self):
        vocaKeyList = list(self.voca.keys())
        for i in range(10):
            randnum = random.randint(0,len(vocaKeyList)-1)
            question = vocaKeyList[randnum]
            answer = input("English to Korean: %s : ?"%(question))
            self.number_answers += 1
            if answer == self.voca[question]:
                print("정답입니다.")
                self.score+=1
            else:
                print("오답입니다.")
    
    def update_voca_from_user_input(self):
        new_voca = {}
        while(True):
            sen = input("단어입력 ex)단어,뜻 :  프로그램 종료 : '끝' 입력")
    
            if(sen == '끝'):break
            eng=""
            mean=""
            try:
                (eng,mean) = sen.split(",")
            except:
                print("단어,뜻 사이에 ,를 넣어 입력해주세요 다시.")
                continue
            new_voca[eng] = mean
        self.voca = new_voca
        print('새로운 단어장으로 업데이트 완료')
        


while(True):
    chNum = int(input("1 . 단어 입력 2 . 테스트 3 . 새로운 단어장 업데이트\n"))
    if chNum == 1:
        vocaexam = VocaExam()
    if chNum == 2:
        vocaexam.test()
    if chNum == 3:
        vocaexam.update_voca_from_user_input()
    
    
    
    
    