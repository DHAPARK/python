from socket import *
from os.path import exists
import sys
import os

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8080))
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'커넥트')

data_move = 0

#디렉토리 전체 파일명 보내기
filenames = os.listdir('../../temp1/')

connectionSock.send(bytes('파일들 '+' '.join(filenames),'utf-8')) #1024바이트 보내고 크기 저장

filename = connectionSock.recv(1024) #클라이언트한테 파일이름(이진 바이트 스트림 형태)을 전달 받는다
print('수신데이터 : ', '../../temp1/'+filename.decode('utf-8')) #파일 이름을 일반 문자열로 변환한다

filename = '../../temp1/'+filename.decode('utf-8')

if not exists(filename):
    print("no file")
    sys.exit()

print("파일 %s 전송중" %filename)
with open(filename, 'rb') as f:
    try:
        data = f.read(1024) #1024바이트 읽는다
        while data: #데이터가 없을 때까지
            data_move += connectionSock.send(data) #1024바이트 보내고 크기 저장
            data = f.read(1024) #1024바이트 읽음
    except Exception as ex:
        pass
print("전송완료 %s 전송량 %d" %(filename, data_move))