"""Primer Punto"""

# Sueldo_base =500000
# for n in range(3):
#   numeroVenta=0
#   while numeroVenta<=3:
#     numeroVenta+=1
#     venta1=int(input("primera venta "))
#     venta2=int(input("primera venta "))
#     venta3=int(input("primera venta "))
#     comision=int((venta1+venta2+venta3)*0.1)
#     print(f"El empleado {n} tiene un sueldo base de {Sueldo_base} mas las comisiones que son {comision}, su suelto total es {Sueldo_base+comision}")
#   n+=1

# for c in range(4):
#     compra=int(input("De cuanto fue la compra? "))
#     eleccion=int(input("Escoja un numero entre el 1, 2 o 3 "))
#     if eleccion==1:
#         roja=int(compra*0.4)
#         total_D=int(compra*0.6)
#         print(f"Sacaste la bolita roja obtienes un descuento del 40% eso equivale a {roja}, se le descuenta por lo cual tendras que paga {total_D}")
#     elif eleccion==2:
#         Amarilla=int(compra*0.25)
#         total_D=int(compra*0.75)
#         print(f"Sacaste la bolita amarilla obtienes un descuento del 25% eso equivale a ({Amarilla}, se le descuenta por lo cual tendras que paga {total_D}")
#     elif eleccion==3:
#         print(f"Sacaste la bolita blanca obtienes un descuento del 0%, por lo cual tendras que paga {compra}")
#     c+=1


# td=0
# nd=0
# for n in range(3):
#     n+=1
#     n1=int(input("primera nota de 0 a 100 "))
#     n2=int(input("segunda nota  de 0 a 100 "))
#     n3=int(input("tercera nota de 0 a 100 "))
#     n4=int(input("cuarta nota  de 0 a 100 "))
#     n5=int(input("quinta nota de 0 a 100 "))
#     pro=int((n1+n2+n3+n4+n5)/5)
#     print(f"El estudiante {n} tiene estas notas:{n1},{n2},{n3},{n4},{n5} y su promedio fue {pro} ")
#     if pro>=70:
#         nd+=1
#     elif pro<70:
#         td+=1        
    
# print(f"El numero de estudiantes que tienen derecho son: {td} y el numero de estudiantes que no tienen derecho son: {nd} ")

# y=0
# d=0
# j=0

# for n in range(10):
#     e=int(input("Por quien vas a votar? 1.Yeison  2.David  3.Jaider "))
#     if e==1: 
#         y+=1
#     elif e==2:
#         d+=1
#     elif e==3:
#         j+=1
#     print("Su voto se guardo correctamente")

# if y>d and y>j:
#     print(f"Gano el candidato Yeison con {y} votos")
# elif d>y and d>j:
#     print(f"Gano el candidato David con {d} votos")
# elif j>y and j>d:
#     print(f"Gano el candidato Jaider con {j} votos")



# n1=0
# n2=0
# n3=0
# n4=0


# for e in range(10):
#     n=int(input("Cual fue tu calificacion en el examen de fisica? "))
#     if n<50: 
#         n1+=1
#     elif n>=50 and n<70:
#         n2+=1
#     elif n>=70 and n<80:
#         n3+=1
#     elif n>=80:
#         n4+=1

# print(f"{n1} estudiante obtuvieron una calificación menor a 50")
# print(f"{n2} estudiante obtuvieron una calificación entre 50 y 69.")
# print(f"{n3} estudiante obtuvieron una calificación entre 70 y 79")
# print(f"{n4} estudiante obtuvieron una calificación mayor a 80")