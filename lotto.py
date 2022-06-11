import sys
import random

myLotList = []
comLotList = []
bonus = 0
correctList = []
# 1. 호출할 함수 구현
# 복권 메뉴 기능을 구현한 부분
#복권 수기 뽑기
def lottery_hand():
    global myLotList
    myLotList = []
    '''코드 작성, 해당 주석 부분은 삭제'''
    for i in range(6):
        while True:
            num = int(input('{0} 번쨰 숫자를 입력하시오 : '.format(i+1)))
            if checkMine(num) == True:
                break    
        myLotList.append(num)
    print('구매한 복권 : ',myLotList)

def checkMine(num):
    global myLotList

    '''코드 작성, 해당 주석 부분은 삭제'''
    if num in myLotList:
        print("이미 입력한 숫자입니다")
        return False
    if num < 1 or num > 45:
        print("1 이상 45 이하의 정수가 아닙니다.")
        return False
    return True

def checkCom(num):
    global comLotList

    '''코드 작성, 해당 주석 부분은 삭제'''
    if num in comLotList:
        print("이미 입력한 숫자입니다")
        return False
    if num < 1 or num > 45:
        print("1 이상 45 이하의 정수가 아닙니다.")
        return False
    return True


#복권 추첨
def lottery_draw():
    global comLotList
    global bonus
    comLotList = []
    '''코드 작성, 해당 주석 부분은 삭제'''
    for i in range(7):
        while True:
            num = random.randint(1,45)
            if checkCom(num) == True:
                break    
        comLotList.append(num)
    bonus = comLotList.pop()
    print('복권번호 : ',comLotList)
    print('보너스번호 : ',bonus)


#당첨 결과 조회
def lottery_result():
    global myLotList
    global comLotList
    global bonus

    if (bonus == 0) or (len(myLotList) == 0) or (len(comLotList) == 0):
        print("복권 구매 또는 복권 추첨이 이루어지지 않았습니다")
        return False

    cnt = 0
    flag = False

    print('보유 복권 : ',myLotList)
    print('당첨 번호 : ',comLotList)
    print('보너스 번호 : ',bonus)
    

    for i in range(6):
        
        if myLotList[i] in comLotList:
            cnt = cnt+1
            correctList.append(myLotList[i])
    if bonus in myLotList:
        cnt = cnt+1
        flag = True
        correctList.append(myLotList[i])
    
    print('일치 번호 : ',correctList)
    if flag == True:
        print('보너스 일치 여부 : 일치')
    else:
        print('보너스 일치 여부 : 불일치')

    if flag and (cnt == 6):
        print('축하합니다,2등입니다.')

    if (not flag) and (cnt == 5):
        print('축하합니다,3등입니다')

    if (not flag) and (cnt == 6):
        print('축하합니다,1등입니다')
    
    if cnt < 5 :
        print("다음 기회에..")
    '''코드 작성, 해당 주석 부분은 삭제'''


# 2. 메인 프로그램 구현
# 반복문, 조건문 등을 사용하여 각 기능에 해당하는 함수를 호출하는 부분
while True:
    chNum = input("————————\n1. 수동 복권 사기\n2. 복권 추첨하기\n3. 당첨 결과 조회하기\n4. 프로그램 종료하기\n————————\n메뉴를 선택하시오 :\n")
    if chNum == '1':
        lottery_hand()
    elif chNum == '2':
        lottery_draw()
    elif chNum == '3':
        lottery_result()
    elif chNum == '4':
        sys.exit(0)
    else:
        print("다시 입력하시오.")
