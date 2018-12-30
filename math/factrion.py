import sys

sys.setrecursionlimit(100000000)
def factorial(n) :
	if n < 0 : 
		return "Eres un capullo!!! Wrong number"
	if n == 0 :
		return 1
	
	if n==1 :
		result = 1
	else :
		result = n*factorial(n-1)
	return int(result)

def show_factrions() :
	for i in range(1,100000) :
		if is_factrion(i) : 
			print("Hemos encontrado el factrion: " + str(i))

	return 'Hemos llegado al infinito'

def is_factrion(n) :
	return n==split_digits_factorial(n)

def split_digits_factorial(n) :
	sum = 0
	digits = map(int,str(n))
	for i in digits :
		sum = sum + factorial(i)
	return sum



print("Hola caraculo")
#print(factorial(1))
print(show_factrions())
#print(is_factrion(3))
