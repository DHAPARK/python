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
'\n' :'\n',
'/':' ',
'':''  
}
#'-':'-',
#'.':'.',
enc_dic = {}
for k, v in dec_dic.items():
	enc_dic[v] = k

f = open(input_filepath,'r',encoding='utf-8')
how = f.read()
f.seek(0)
f.close()

if 'Morse Code' in how:
	f = open(input_filepath,'r',encoding='utf-8')
	f.seek(11)
	f2 = open(output_filepath,'w',encoding='utf-8')
	f3 = open(result_filepath,'w',encoding='utf-8')
	file_contents = f.read()
	words = file_contents
	
	allstr = []
	allstr = words.split('/ ')
	#print(allstr[0].strip())
	allstr2 = []
	str1 = []
	for i in allstr:
		str1 = i.split(' ')
		#print(str1[0])
		for j in str1:
			print(j)
			#j = j.strip()
			allstr2.append(dec_dic[j])
		allstr2.append(' ')
	str123 = ''.join(allstr2)
	f2.write(str123)
	f.close()
	f2.close()
	f3.close()
#############시저암호부분
elif 'Caesar' in how:
	f = open(input_filepath,'r',encoding='utf-8')
	f.seek(18)
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
			allstr[j] = chr((ord(allstr[j])-ord('A')-3)%26+ord('A'))
		elif allstr[j].islower(): 
			allstr[j] = chr((ord(allstr[j])-ord('a')-3)%26+ord('a'))
	str1 = ''.join(allstr)
	f2.write(str1)

	f.close()
	f2.close()
	f3.close()
# 모든 출력이 끝나면 개행을 한다.



# 16진수로 암/복호화
if 'Hex' in how:
    f = open(input_filepath, 'r', encoding='utf-8')
    f.seek(4)
    f2 = open(output_filepath, 'w', encoding='utf-8')
    f3 = open(result_filepath, 'w', encoding='utf-8')
    file_contents = f.read()

    words = file_contents.split(' ')

    for word in words:
        f2.write(chr(int(word, 16)))

    f.close()
    f2.close()
    f3.close()