import sys
def get_primos() :
    i = 1
    j = 1
    while True :
        if is_primo(i) : 
            print("Primo numero ", j," : ",i)
            j += 1
        i += 1
        
    
    return True

def is_primo(n) : 
    if n%2 == 0 or is_divisible(n) : return False
    return True

def split_digits_sum(n) :
	sum = 0
	digits = map(int,str(n))
	for i in digits :
		sum = sum + i
	return sum

def is_divisible(n) : 
    for i in range(3,n//2,2) :
        if n%i == 0 :
            return True
    return False


#print('Aquí van unos cuantos números primos...')
#get_primos()
if len(sys.argv) < 2 :
    print("Introduce el número que quieres comprobar")
else : 
    if is_primo(int(sys.argv[1])) :
        print("Primo!!!")
    else :
        print("No primo")
