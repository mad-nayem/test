import platform,os
os.system('git pull')
os.system('clear')


arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("litex").login()
elif 'aarch' in arc:
	__import__("lite").login()
else:
	__import__("litexx").login()
