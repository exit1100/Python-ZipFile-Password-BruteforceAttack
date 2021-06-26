#-*- coding: utf-8 -*-
from itertools import product
from zipfile import *

def unzipfile(filename, password):
	try:
		#print(password)
		filename.extractall(pwd = password.encode())
		print("[*] find password! : {0}".format(password))
		return 1
	except:
		pass
	
	
def main():
	
	i = input('zip file path >> ')
	if i.find('.zip') == -1:
		print('It is no zip file.')
		exit()
	filename = ZipFile(i)
	
	static_start_char = input('static_start_char >> ')	# 앞에서 부터 확실한 비밀번호 입력
	static_end_char = input('static_end_char >> ')	# 뒤에서 부터 확실한 비밀번호 입력
	static_char_len = len(static_start_char) + len(static_end_char)	# 고정된 비밀번호 개수
	chars = input('dictionary chars >> ')
	min_length = int(input('password min_length >> ')) - static_char_len	# 고정된 값을 제외
	max_length = int(input('password max_length >> ')) - static_char_len
	
	print('[*] start : brute force attack!')
	for length in range(min_length,max_length+1):
		to_attempt = product(chars, repeat=length)
		for attempt in to_attempt:
			password = ''.join(attempt)
			ret = unzipfile(filename, static_start_char + password + static_end_char)
			if ret == 1:
				exit()
		
if __name__ == '__main__':
	main()