
def get_primos() :
    i = 4
    while True :
        if is_primo(i) : 
            print(i)
        i = i + 1
    
    return True

def is_primo(n) : 
    primo = True
    if n%2 == 0 :
        primo = False
    if n%5 == 0 :
        primo = False
    if split_digits_sum(n)%3 == 0 : 
        primo = False
    if is_divisible(n) : 
        primo = False
    return primo

def split_digits_sum(n) :
	sum = 0
	digits = map(int,str(n))
	for i in digits :
		sum = sum + i
	return sum

def is_divisible(n) : 
    return True

print('Hola de nuevo caraculo')
get_primos()
