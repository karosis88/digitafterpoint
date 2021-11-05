import time



def binarydivision(n1, n2, x):

	tg = 0
	while float(n1) < float(n2):
		n1 = float(n1)*10
		tg+=1
	n1, n2 = str(n1), str(n2)
	last = False
	m = max((len(n1) - n1.find('.') if '.' in n1 else 0), (len(n2) - n2.find('.') if '.' in n2 else 0))
	n1 = str(int(float(((float((n1)))*10**(m)))))
	n2 = str(int(float(((float((n2)))*10**(m)))))


	result = ''
	point = True
	i1 = 1
	transfer = True
	tointtarget = int(n1)//int(n2)
	while int(n1[:i1]) < int(n2):
		i1+=1
	
	kk = True
	fakecount = False
	count = 0
	afterpoint = False
	while count != x:
		curnum = int(n1[:i1]) if kk else int(n1)
		kk = False

		if curnum >= int(n2):
			last = False
			tominus = curnum//int(n2) * int(n2)
			result += str(tominus // int(n2))
			lastadd = str(tominus // int(n2))
			toadd = curnum - tominus		
			n1 = str(toadd) + n1[i1:]
			if int(n2) > int(n1) and '.' not in result:
				result+='.'
				afterpoint = True
				
		else:
			if last:
				result += '0'
				fakecount+=1
				last=False
			if str(curnum) == '0' * len(str(curnum)):
				return result/10**tg
			i1 += 1
			n1 += '0'
			last = True

		if fakecount and afterpoint:
			count += fakecount
			fakecount = 0
			
	pointind = result.find('.')

	targetpointind = pointind-tg
	result = result[:targetpointind] + '.' + result[targetpointind:pointind] + result[pointind+1:]
	return ('0' if result[0] == '.' else '') + result
	# return result[:pointind] + result[pointind+1:pointind+1+tg] + '.' + result[pointind+1+tg:]

print(binarydivision(20.675747, 30.675747, 5000), 'asd')



