import sys
import codecs
import binascii
import ast
input_filepath = sys.argv[1]
output_filepath = sys.argv[2]
result_filepath = './result_file.txt'
if len(sys.argv) != 3:
	print("Insufficient arguments")
	sys.exit()

print("input File path : " + input_filepath)
print("ouput File path : " + output_filepath)

dec_dic = { '.-' : 'A',
'-...' : 'B',
'-.-.' : 'C',
'-..'  : 'D',
'.'    : 'E',
'..-.' : 'F',
'--.'  : 'G',
'....' : 'H',
'..'   : 'I',
'.---' : 'J',
'-.-'  : 'K',
'.-..' : 'L',
'--'   : 'M',
'-.'   : 'N',
'---'  : 'O',
'.--.' : 'P',
'--.-' : 'Q',
'.-.'  : 'R',
'...'  : 'S',
'-'    : 'T',
'..-'  : 'U',
'...-' : 'V',
'.--'  : 'W',
'-..-' : 'X',
'-.--' : 'Y',
'--..' : 'Z',
'.----' : '1',
'..---' : '2',
'...--' : '3',
'....-' : '4',
'.....' : '5',
'-....' : '6',
'--...' : '7',
'---..' : '8',
'----.' : '9',
'-----' : '0',
' ':' ',
'(':'(',
')':')',
':':':',
'+':'+',
'\n' :'\n'  
}

enc_dic = {}
for k, v in dec_dic.items():
	enc_dic[v] = k


choose = input("어떤 타입으로 인코딩하시겠습니까? 1:모스식 부호 2.시저+3 3. 16진수")



if choose == '1':
	f = open(input_filepath,'r',encoding='utf-8')
	f2 = open(output_filepath,'w',encoding='utf-8')
	f3 = open(result_filepath,'w',encoding='utf-8')
	file_contents = f.read()
	words = str(file_contents)
	allstr = []
	#암호화 기능
	for j in words:
		j = f'{j}'
		if j == '\n':
			allstr.append(j)
		else: 
			allstr.append(str(enc_dic[j.upper()]))
	str1 = ''.join(allstr)
	f2.write(str1)
	#복호화 기능
	allstr2 =[]
	for k in allstr:
		k = f'{k}'
		if k == '\n':
			allstr2.append(k)
		else:
			allstr2.append(str(dec_dic[k]).lower())
	str2 = ''.join(allstr2)
	f3.write(str2)
	f.close()
	f2.close()
	f3.close()
#############시저암호부분
elif choose=='2':
	f = open(input_filepath,'r',encoding='utf-8')
	f2 = open(output_filepath,'w',encoding='utf-8')
	f3 = open(result_filepath,'w',encoding='utf-8')
	file_contents = f.read()
	words = str(file_contents)
	allstr = list(words)
	for j in range(len(allstr)):
		if allstr[j] == ' ':
			allstr[j] = ' '
			continue
		if allstr[j] == '\n':
			allstr[j] = '\n'
			continue
		if allstr[j].isupper():
			allstr[j] = chr((ord(allstr[j])-ord('A')+3)%26+ord('A'))
		elif allstr[j].islower(): 
			allstr[j] = chr((ord(allstr[j])-ord('a')+3)%26+ord('a'))
	str1 = ''.join(allstr)
	f2.write(str1)


	#복호화 기능
	allstr2 =[]
	for j in range(len(allstr)):
		if allstr[j] == ' ':
			allstr2.append(' ')
			continue
		if allstr[j] == '\n':
			allstr2.append('\n')
			continue
		if allstr[j].isupper():
			allstr2.append(chr((ord(allstr[j])-ord('A')-3)%26+ord('A')))
		elif allstr[j].islower(): 
			allstr2.append(chr((ord(allstr[j])-ord('a')-3)%26+ord('a')))
		else:
			allstr2.append(allstr[j])
	str2 = ''.join(allstr2)
	f3.write(str2)
	f.close()
	f2.close()
	f3.close()
# 모든 출력이 끝나면 개행을 한다.



#16진수로 암/복호화
if choose == '3':
	f = open(input_filepath,'r',encoding='utf-8')
	f2 = open(output_filepath,'w',encoding='utf-8')
	f3 = open(result_filepath,'w',encoding='utf-8')
	file_contents = f.read()

	words = str(file_contents)
	
	#allstr = []
	allstr = list(words)
	#암호화 기능
	for j in range(len(allstr)):
		str1 = allstr[j]
		str11 = ord(str1)
		str111 = hex(str11)
		allstr[j] = str111
	str1 = ''.join(allstr)
	f2.write(str1)


	#복호화 기능
	allstr2 =[]
	for j in range(len(allstr)):
		str12 = ast.literal_eval(allstr[j])
		str2 = chr(str12)
		allstr2.append(str2)
	str2 = ''.join(allstr2)
	f3.write(str2)
	f.close()
	f2.close()
	f3.close()


