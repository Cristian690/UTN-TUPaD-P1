

# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

lista_frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

#def numeros_tel():
def num_telefonico():
    agenda = {}
    for i in range(5):
        nombre = input("Ingrese el nombre de contacto: ")
        telefono = int(input("Ingrese el numero telefónico: "))
        agenda[nombre] = telefono
    print(agenda)

# num_telefonico()

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
def frase():
    frase = input("Escriba una frase: ")
    palabras = set(frase.split())

    contador = {}

    for palabra in frase.split():
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    print(contador)

# frase()

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

def notas_alumnos():
    notas_alumnos = {}
    for i in range(3):
        nombre = input("Ingrese el nombre del alumno: ")
        nota1 = int(input("Ingrese la nota 1: "))
        nota2 = int(input("Ingrese la nota 2: "))
        nota3 = int(input("Ingrese la nota 3: "))
        tupla_notas = (nota1, nota2, nota3)
        promedio = (nota1 + nota2 + nota3)/3
        notas_alumnos[nombre] = tupla_notas
    # print(f'El promedio de {nombre} es: {promedio}')


    for nombre, notas in notas_alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {nombre} es: {promedio:.2f}")

# notas_alumnos()

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


# Listas de alumnos que aprobaron cada parcial (representados por su número de legajo)
def alumnos_aprobados():
    parcial1 = [101, 102, 103, 104]
    parcial2 = [102, 104, 105, 106]

    ambos = []
    for alumno in parcial1:
        if alumno in parcial2:
            ambos.append(alumno)

    solo_uno = []
    for alumno in parcial1:
        if alumno not in parcial2:
            solo_uno.append(alumno)
    for alumno in parcial2:
        if alumno not in parcial1:
            solo_uno.append(alumno)

    al_menos_uno = []
    for alumno in parcial1:
        if alumno not in al_menos_uno:
            al_menos_uno.append(alumno)
    for alumno in parcial2:
        if alumno not in al_menos_uno:
            al_menos_uno.append(alumno)

    print("Aprobaron ambos parciales:", ambos)
    print("Aprobaron solo uno de los dos:", solo_uno)
    print("Aprobaron al menos un parcial:", al_menos_uno)

# alumnos_aprobados()

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

def gestionar_stock():
    stock = {
        "manzanas": 10,
        "peras": 5,
        "bananas": 8
    }

    producto = input("Ingrese el nombre del producto: ").lower()

    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]}")
        agregar = input("¿Desea agregar unidades al stock? (s/n): ").lower()
        if agregar == "s":
            unidades = int(input("¿Cuántas unidades desea agregar?: "))
            stock[producto] += unidades
            print(f"Nuevo stock de {producto}: {stock[producto]}")
        else:
            print("No se modificó el stock.")
    else:
        print("Producto no encontrado.")
        agregar_nuevo = input("¿Desea agregar este nuevo producto? (s/n): ").lower()
        if agregar_nuevo == "s":
            unidades = int(input("¿Cuántas unidades desea agregar?: "))
            stock[producto] = unidades
            print(f"Producto '{producto}' agregado con stock {unidades}.")
        else:
            print("No se agregó el nuevo producto.")

    print("\nStock actual completo:")
    for producto, cantidad in stock.items():
        print(f"{producto}: {cantidad}")


gestionar_stock()

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
def crear_agenda():
    agenda = {}

    while True:
        dia = input("Ingrese el día del evento (ej: lunes): ")
        hora = input("Ingrese la hora del evento (ej: 14:00): ")
        evento = input("Ingrese el nombre del evento: ")

        clave = (dia, hora)
        agenda[clave] = evento

        continuar = input("¿Desea agregar otro evento? (s/n): ")
        if continuar != "s":
            break

    print("\nAgenda completa:")
    for clave, evento in agenda.items():
        print(f"{clave[0].capitalize()} a las {clave[1]} → {evento}")

#crear_agenda()


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

def invertir_diccionario():
    paises_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Francia": "París",
        "Japón": "Tokio"
    }

    capitales_paises = {}

    for pais, capital in paises_capitales.items():
        capitales_paises[capital] = pais

    print("Diccionario original:")
    print(paises_capitales)

    print("\nDiccionario invertido:")
    print(capitales_paises)

invertir_diccionario()