from zipfile import *

def unzipfile(filename, password):
	try:
		filename.extractall(pwd = password.encode())
		print("[*] find password! : {0}".format(password))
	except:
		pass
		
def main():
	i = input('zip file path >> ')
	if i.find('.zip') == -1:
		print('It is no zip file.')
		exit()
	filename = ZipFile(i)
	li = input('dictionary file path >> ')
	pass_list = open(str(li),'r')
	print('[*] start : brute force attack!')
	for line in pass_list:
		password = line.strip('\n')
		#print(password)
		unzipfile(filename, password)
		
if __name__ == '__main__':
	main()