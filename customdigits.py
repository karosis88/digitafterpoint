import time



def binarydivision(n1, n2, x):
	beforepotoints = len(str(int(n1)//int(n2)))
	n1, n2 = str(n1), str(n2)

	m = max((len(n1) - n1.find('.') if '.' in n1 else 0), (len(n2) - n2.find('.') if '.' in n2 else 0))
	print(float((int(float((n1)))*10**(m-1))))
	n1 = str(int(float((int(float((n1)))*10**(m-1)))))
	n2 = str(int(float((int(float((n2)))*10**(m-1)))))
	print(n1, n2, 3)

	result = ''
	point = True
	i1 = 1
	transfer = True

	tointtarget = int(n1)//int(n2)

	while int(n1[:i1]) < int(n2):
		i1+=1
		

	kk = True
 
	while len(result) + beforepotoints != x:
		curnum = int(n1[:i1]) if kk else int(n1)
		kk = False

		if curnum >= int(n2):

			tominus = curnum//int(n2) * int(n2)
			result += str(tominus // int(n2))
			toadd = curnum - tominus
		
			n1 = str(toadd) + n1[i1:]

			if int(n2) > int(n1) and '.' not in result:
				result+='.'
			
		else:
			if str(curnum) == '0' * len(str(curnum)):
				return result
			i1 += 1
			n1 += '0'
	return result

print(binarydivision(100.7, 17, 30))
print(format(100.12512512489/17, '.30f'))


