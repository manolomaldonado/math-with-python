import decimal

def calcula_pi(n) :
    result = decimal.Decimal(2)
    for i in range(1,n) :
        i = decimal.Decimal(i)
        new = ((4*i**2) / (4*i**2 - 1))
        result = result * new
    print(result)




calcula_pi(10000000)
print('Hola caraculo')