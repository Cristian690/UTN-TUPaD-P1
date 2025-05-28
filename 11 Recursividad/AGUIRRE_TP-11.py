
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario

def factorial_recursiva(num):
     if num == 1:
         return 1
     else:
         return num * factorial_recursiva(num - 1)

# numero_factorial = int(input("Ingrese un numero para calcular su factorial: "))

# print(f'El factorial del número ingresado es: {factorial_recursiva(numero_factorial)}')


#----------------------------------------------------------------------------------



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

def calcular_fibonacci(num):
    if num == 0:               
        return 0 
    elif num == 1:                  
        return 1
    else:
        return calcular_fibonacci(num - 1) + calcular_fibonacci(num -2)

# posicion_fibo = int(input("Ingrese una posición de Fibonacci: "))
# print(f'El número de Fibo en la posición {posicion_fibo} es {calcular_fibonacci(posicion_fibo)}')

# print("La serie completa hasta la posición ingresada es: ")
# for i in range(posicion_fibo + 1):

#     print(calcular_fibonacci(i), end = " ")

#_______________________________________________________________________________________



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

def calcular_potencia(base, expo):
    if expo == 0:
        return 1
    elif base == 1:
        return 1
    else:
        return base * (calcular_potencia(base, expo - 1))



# numero_base = int(input("Ingrese un número base para calcular su potencia: "))
# numero_expo = int(input("Ingrese un exponente: "))

# print("Su potencia calculada es:", calcular_potencia(numero_base, numero_expo))

#_________________________________________________________________________________________




# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def calcular_binario(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"    
    else:
        return calcular_binario(decimal // 2) + str(decimal % 2)

#print(calcular_binario(100))

#____________________________________________________________________________________________





# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#  Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
#print(es_palindromo("reconocer"))

#__________________________________________________________________________________________________




# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(num):
    if num == 0:
        return 0
    elif num <= 0:
        return 0
    else:
        return  num % 10 + suma_digitos(num // 10) 

#print(suma_digitos(527))

#_________________________________________________________________________________________




# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.

def contar_bloques(cant):
    if cant == 1:
        return 1
    else:
        return cant + contar_bloques(cant -1)


#______________________________________________________________________________________





# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(num, digito):
    if num == 0:
        return 0
    else:
        ultimo = num % 10
        
        if ultimo == digito:
            return 1 + contar_digito(num // 10, digito)
        else:
            return contar_digito(num // 10, digito)

#print(contar_digito(252525, 2))