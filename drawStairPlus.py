#계단 1
#더하기 2

while(True):
    chNum = int(input("도형을 선택하세요"))
    if chNum == 3:break
    if chNum == 1:
        stNum = int(input("계단의 높이입력 2이상 5 이하의 높이 입력"))
        stNum2 = int(input("계단의 칸 수 입력 2 이상 5이하의 칸 수 입력"))
        
        if stNum <2 or stNum >5:continue
        if stNum2 <2 or stNum2 >5:continue
        for i in range(1,stNum2+1):
            for j in range(stNum):
                for k in range(stNum*i):
                    print("■",end="")
                print("")
        continue
    elif chNum == 2:
        
        plNum = int(input("더하기의 길이입력"))
        if plNum <2 or plNum >10:continue
        for i in range(plNum):
            for q in range(plNum):
                print("   ",end="")
            for j in range(plNum):
                print(" ★ ",end="")
            print("")
        for i in range(plNum):
            for j in range(plNum*3):
                print(" ★ ",end="")
            print("")
        for i in range(plNum):
            for n in range(plNum):
                print("   ",end="")
            for j in range(plNum):
                print(" ★ ",end="")
            print("")
        continue