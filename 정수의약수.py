cnt = int(input(""))

def getMyDivisor(n):
    cnt = 0
    for i in range(1, n + 1):
        if (n % i == 0) :
            cnt += 1
            print("%d "%(i),end="")
    maxlist.append(cnt)
    print("")

numlist = []
maxlist = []
for i in range(0,cnt):
    numlist.append(int(input("")))

for i in range(0,cnt):
    getMyDivisor(numlist[i])

maxnumindex = maxlist.index(max(maxlist))
print("제일많은 약수를 가진 수 : %d"%(numlist[maxnumindex]))



