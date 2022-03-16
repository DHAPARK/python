import pandas as pd
import sys
import numpy

sheet_path = sys.argv[2]
sheet_name = sheet_path

df = pd.read_excel('Anyang.xlsx',sheet_name=sheet_path,header=1,nrows=4041,names=['일번','이번','삼번'],usecols=[1])
df.set_index("이번",inplace=True)


print(df.index[0])
#총 자료갯수
dataCnt = numpy.size(df.index)

for i in range(0,dataCnt):
    
    lineList = df.index[i].split(',')
    x1 = float(lineList[0])
    y1 = float(lineList[1])
    x2 = float(lineList[2])
    y2 = float(lineList[3])
    w = x2-x1
    h = y2-y1
    x = (x1+x2)/2*(1/1920)
    y = (y1+y2)/2*(1/1080)
    yolov4 = [x, y , w * (1/1920) ,h*(1/1080)]
    print(yolov4)
