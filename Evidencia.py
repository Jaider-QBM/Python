""" Primer punto """
"""
nu1 = int(input("Ingrese el primer numero "))
nu2 =int(input("Ingrese el segundo numero "))

if nu1==nu2:
    multiplique = nu1*nu2
    print("Los dos numero son iguales, se van a multiplicar, el resultado es ", multiplique)
elif nu1>nu2:
    restar = nu1-nu2
    print("El primer numero es mayor que el segundo, se van a restar, el resultado es ", restar)
else:
    suma = nu1+nu2
    print("El segundo numero es mayor que el primero, se van a sumar, el resultado es ", suma)

"""

"""Segundo Punto"""
"""
precio = 15000
cantidad = int(input("Cual es la cantidad de computadores que quiere llevar"))
subtotal = cantidad*precio

if cantidad<5:
    descuento1 = int(subtotal*0.1)
    total = subtotal - descuento1
    print("Tienes un descuento a su compra por el 10% ", descuento1," total a pagar es", total)
elif cantidad<10:
    descuento2 = int(subtotal*0.2)
    total = subtotal - descuento2
    print("Tienes un descuento a su compra por el 20% ", descuento2," total a pagar es", total)
elif cantidad>=10:
    descuento3 = int(subtotal*0.4)
    total = subtotal - descuento3
    print("Tienes un descuento a su compra por el 40% ", descuento3," total a pagar es", total)

"""
""" Tercer Punto 
cantidad = int(input("Cual es la cantidad de llantas va a llevar"))

if cantidad<5:
    precio = 300
    total = precio*cantidad
    print("El precio de cada llanta es de 300, el total de pagar es ", total)
elif cantidad<=10:
    precio = 250
    total = precio*cantidad
    print("El precio de cada llanta es de 250, el total de pagar es ", total)
elif cantidad>10:
    precio = 200
    total = precio*cantidad
    print("El precio de cada llanta es de 200, el total de pagar es ", total)

"""
""" Cuarto punto 
P1 = int(input("¿Colon descubrió América? 1 Si o No"))
if P1 == 1:
    P2 = int(input("¿La independencia de México fue en el año 1810? 1 Si o No"))
    if P2 ==1:
        P3 = int(input("¿The Doors fue un grupo de rock americano? 1 Si o No"))
        if P3 == 1:
            print("Has ganado")
        else:
            print("Respondi mal, a terminado el juego")
    else:
        print("Respondi mal, a terminado el juego")      
else:
    print("Respondi mal, a terminado el juego")
"""

""" Cinco Punto
n1 = int(input("Ingrese el primer numero"))
n2 = int(input("Ingrese el Segundo numero"))
n3 = int(input("Ingrese el tercer numero"))

if n1> n2 and n1>n3:
    print("El numero mayor es ", n1)
elif n2> n1 and n2>n3:
    print("El numero mayor es ", n2)
elif n3> n1 and n3>n2:
    print("El numero mayor es ", n3)
"""
