#-*- coding: utf-8 -*-
from itertools import product

chars = input('[*] Input : brute force dictionary chars >> ')	# 조합할 문자들 입력
f = open('brute_force.txt','w')
for length in range(5,6):	# 만들고 싶은 사전의 자릿수. 5자리 -> range(5,6)
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		brute = ''.join(attempt)
		f.write(brute+'\n')
print('[*] Complete : brute force dictionary! ')
f.close()