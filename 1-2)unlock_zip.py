from zipfile import *

def unzipfile(filename, password):
	try:
		filename.extractall(pwd = password.encode())
		print("[*] find password! : {0}".format(password))
		exit()
	except:
		pass
		
def main():
	i = input('zip file path >> ')	# 비밀번호가 잠긴 zip파일 경로지정
	if i.find('.zip') == -1:	# zip확장자가 아니면 종료
		print('It is no zip file.')
		exit()
	filename = ZipFile(i)
	li = input('dictionary file path >> ')	# 사전파일 경로지정
	pass_list = open(str(li),'r')	# 파일 모두 읽기
	print('[*] start : brute force attack!')
	for line in pass_list:	# 라인 읽기
		password = line.strip('\n')
		#print(password)
		unzipfile(filename, password)
		
if __name__ == '__main__':
	main()