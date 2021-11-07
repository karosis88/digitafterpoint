
def superdivision(n1:float, n2:float, x:float):
	count = 0
	last = False

	h = max([((len(str(i)) - str(i).find('.') - 1 ) if '.' in str(i) else 0) for i in (n1, n2)])

	n1pointind = n1.find('.')
	n2pointind = n2.find('.')

	if '.' in n1 and '.' in n2:
		if len(n1.split('.')[1]) < len(n2.split('.')[1]):
			n1 += (len(n2.split('.')[1]) - len(n1.split('.')[1])) * '0'
		else:
			n2 += (len(n1.split('.')[1]) - len(n2.split('.')[1])) * '0'


	n1 = (n1[:n1pointind] + n1[n1pointind+1 : n1pointind + h + 1] + '.' + n1[n1pointind + h+1:] if '.' in n1 else str(int(n1) * 10**(h)))
	n2 = (n2[:n2pointind] + n2[n2pointind+1 : n2pointind + h + 1] + '.' + n2[n2pointind + h+1:] if '.' in n2 else str(int(n2) * 10**(h)))
	
	if n1[-1] == '.': n1 = n1[:-1]
	if n2[-1] == '.': n2 = n2[:-1]

	n1, n2 = int(n1), int(n2)

	startresult =n1//n2
	result = str(startresult) + '.'
	n1= int(n1) - startresult* (int(n2))
	n2 = int(n2)

	while count != x:
		if n1 >= n2 or last:
			addres = n1//n2
			result += str(int(addres))
			count += 1
			n1 -= n2*addres
			last = False
		else:
			n1*=10
			last = True

	return result

def superx(n1, n2):
	if '.' not in n1: n1+='.'
	if '.' not in n2: n2+='.'

	pointind = len(n1.split('.')[1]) + len(n2.split('.')[1])

	newsum = str(int(n1.replace('.', '')) * int(n2.replace('.', '')))

	while len(newsum) <= pointind:
			newsum = '0' + newsum

	return newsum[:-pointind] + '.' + newsum[-pointind:]

def supersum(n1, n2):
	if '.' not in n1 and '.' not in n2:
		return str(int(n1) + int(n2))
	if '.' not in n1: n1+='.'
	if '.' not in n2: n2+='.'

	n1 += '0' * (h if (h:=(len(n2.split('.')[1]) - len(n1.split('.')[1]))) > 0 else 0)
	n2 += '0' * (h if (h:=(len(n1.split('.')[1]) - len(n2.split('.')[1]))) > 0 else 0)

	pointind = len(n1.split('.')[1])

	newsum = str(int(n1.replace('.', '')) + int(n2.replace('.', '')))

	while len(newsum) < pointind+1:
		newsum = '0' + newsum
	
	return newsum[:-pointind] + '.' + newsum[-pointind:]




	



