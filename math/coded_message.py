def media(numeros) :
    sum = 0
    for i in numeros :
        sum = sum + i

    return sum/len(numeros)

print(media([7,8,9,1,3,4,5,67,567,56,77,888,34,56,67,888,9]))


def mayor(a,b) :
    if a > b :
        return a
    else :
        return b


print(mayor(7,10))


def codifica_mensaje(mensaje) :
    alfabeto = ['A','C','E','I','L','M','N','O','P','S', 'U','X',' ']
    codigo = ['4','C','3','1','7','W','N','0','b','5', 'n','%','#']
    codificado = ''
    for i in mensaje :
        x = alfabeto.index(i)
        codificado = codificado + codigo[x]
    return codificado

def descodifica_mensaje_codificado(mensaje_codificado) :
    alfabeto = ['A','C','E','I','L','M','N','O','P','S', 'U','X',' ']
    codigo = ['4','C','3','1','7','W','N','0','b','5', 'n','%','#']
    mensaje = ''
    for i in mensaje_codificado :
        x = codigo.index(i)
        mensaje = mensaje + alfabeto[x]
    return mensaje


x = codifica_mensaje('MAXI ES UN CAPULLO')
print(x)
y = descodifica_mensaje_codificado(x)
print(y)

