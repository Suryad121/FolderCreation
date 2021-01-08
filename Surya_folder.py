import os
import getpass
a=getpass.getuser()
a1='C:\\user\\'
a2='\\Desktop'
a3=a1+a+a2
os.chdir(a3)
for i in range(1,21):
	f=str(i)
	os.mkdir(f)
