from socket import *
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', 8080))

print('연결완료')

data = clientSock.recv(1024)
if '파' == data.decode('utf-8')[0]:
    print(data.decode('utf-8'))        



filename = input('받을 파일 이름을 입력: ')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(1024)
data_move = 0

cnt = 0

if not data:
    print('파일 %s 없음' %filename)
    sys.exit()

nowdir = os.getcwd()
with open(nowdir+"\\"+filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
    try:
        while data: #데이터가 있을 때까지
            
            f.write(data) #1024바이트 쓴다
            data_move += len(data)
            data = clientSock.recv(1024) #1024바이트를 받아 온다
    except Exception as ex:
        pass
print('파일 %s 받기 완료. 전송량 %d' %(filename, data_move))