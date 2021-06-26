#-*- coding: utf-8 -*-
from itertools import product
from zipfile import *

def unzipfile(filename, password):
	try:
		#print(password)
		filename.extractall(pwd = password.encode())
		print("[*] Find password! : {0}".format(password))
		return 1
	except:
		pass
	
	
def main():
	i = input('[*] Input : zip file path >> ')
	if i.find('.zip') == -1:
		print('It is no zip file.')
		exit()
	filename = ZipFile(i)
	
	static_char = str(input("[*] Input : Guess_password (If you don't know : [spacebar] ) >> "))
	static_char_len = len(static_char)

	static_true = []	#공백이 아닌 자리의 인덱스를 저장
	static_false = []	#공백의 자리의 인덱스를 저장 -> 이 부분만 대입하기 위해
	index = 0
	while(index < static_char_len):
		if static_char[index] == ' ':
			static_false.append(index)
		else:
			static_true.append(index)
		index = index+1
		
	static_true_len = len(static_true)	
	static_false_len = len(static_false)

	chars = input('[*] Input : bruteforce chars >> ')
	
	print('[*] Start : bruteforce Attack!')
	
	for length in range(static_false_len,static_false_len+1):	# 만들어지는 비밀번호 자리수 == 공백의 수 
		to_attempt = product(chars, repeat=length)
		for attempt in to_attempt:
			password_list = []
			for char in attempt:
				password_list += char
				
			for s_word in static_true:	# 공백이 아니었던 자리를 insert를 이용해서 채워준다.
				password_list.insert(s_word,static_char[s_word])
				
			password = ''.join(password_list)
			ret = unzipfile(filename, password)	# 비밀번호 해제 시도
			if ret == 1:
				exit()
		
	print('[*] Exit : bruteforce Attack is failure.')
		
if __name__ == '__main__':
	main()
