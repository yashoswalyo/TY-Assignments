from time import sleep
def table(n,mSquare:dict):
	c=''
	num = 0
	for i in range(n):
		a='|'
		b='+'
		for j in range(n):
			if mSquare.get(i)[j] == 0: var = ''
			else: var = mSquare.get(i)[j]
			a = a+' {:<2} |'.format(var)
			b = b+'----+'
			num+=1
		print(b)
		print(a)
		c=b
	print(c)

n = int(input("Enter number of colums: "))
if n%2==0:
	print("Enter valid length")
	exit(0)

else: 
	mSquare = {}
	for i in range(n):
		arr = []
		for j in range(n):
			arr.append(0)
		mSquare.update({i:arr})
	print("Adding: 1")
	x = n-1
	y = int((n-1)/2)
	mSquare.get(y)[x] = 1
	table(n,mSquare)
	print("\n\n")
	sleep(1)
	c=0
	while c<(n*n)-1:
		print(f"Adding: {c+2}")
		x = (x+1)%n
		y = (y-1)%n
		print("[+] Going Up and Right")
		if mSquare.get(y)[x] == 0:
			sleep(3)
			mSquare.get(y)[x] = c+2
			table(n,mSquare)
		else:
			print("[-] Already taken\n[+] Going Left")
			sleep(3)
			x = (x-2)%n
			y = (y+1)%n
			mSquare.get(y)[x] = c+2
			table(n,mSquare)
		print("\n")
		sleep(1)
		c+=1
