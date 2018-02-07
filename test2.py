minimum=None
maximum=None
while True:
	test=input('Enter a number: ')
	if test=="done":
		break
	try:
		num=float(test)
	except:
		print("invalid input")
		continue
	if minimum is None or num<minimum:
		minimum = num
	if maximum is None or num>maximum:
		maximum = num
	print("maximum is", maximum)
	print("minimum is", minimum)
	
	