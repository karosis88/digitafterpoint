import time

def binarydivision(n1:float, n2:float, x:float):
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
	

while True:
	try:
		num1 = input('Number 1: ')
		num2 = input('Number 2: ')
		digap = input('Digits After Point: ')
		print(binarydivision(num1, num2, int(digap)))
		time.sleep(10)
	except Exception as e:
		print(e)




	



