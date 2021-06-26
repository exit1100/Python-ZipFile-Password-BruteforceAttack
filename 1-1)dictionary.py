#-*- coding: utf-8 -*-
from itertools import product

chars = input('[*] Input : brute force dictionary chars >> ')
f = open('brute_force.txt','w')
for length in range(4,8):
	to_attempt = product(chars, repeat=length)
	for attempt in to_attempt:
		brute = ''.join(attempt)
		f.write(brute+'\n')rcm
print('[*] Complete : brute force dictionary! ')
f.close()