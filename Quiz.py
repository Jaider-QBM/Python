"""Primer Punto"""

"""Una persona desea iniciar un negocio, para lo cual piensa verificar cuánto dinero le
prestara el banco por hipotecar su casa. Tiene una cuenta bancaria, pero no quiere
disponer de ella a menos que el monto por hipotecar su casa sea muy pequeño.

  a.Si el monto de la hipoteca es menor que $1.000.000, entonces invertirá el 50% de
  la inversión total y un socio invertirá el otro 50%.
  
  b.Si el monto de la hipoteca es de $ 1.000.000 o más, entonces invertirá el monto
  total de la hipoteca y el resto del dinero que se necesite para cubrir la inversión
  total se repartirá a partes iguales entre el socio y el.
"""


invertir = int(input("Ingrese lo que va invertir"))
Hipoteca=int(input("Ingrese la hipoteca"))
if Hipoteca<1000000:
    invertira = (invertir * 0.5)
    total = invertir- invertira
    print(f"Va a invertir ud 50% de la inversion total {total} y su socio invirtira el otro 50% {total} ")
elif Hipoteca>=1000000:
    resta = invertir-Hipoteca
    repart =  resta/2
    totalP = resta + repart
    print(f"Va a pagar toda la hipoteca {Hipoteca} mas {repart}  y el socio va a pagar  {repart}")
elif invertir <Hipoteca:
    print("Monto de la hipoteca es mayor de lo que vas a invertir ")
    

"""Segundo Punto"""

"""
El gobierno de Colombia, desea reforestar un bosque que mide determinado número de
hectáreas. Si la superficie del terreno excede a 1 millón de metros cuadrados, entonces
decidirá sembrar de la siguiente manera:
"""

hectareas = int(input("Ingrese las Hectareas"))
multi = hectareas *10000

if multi>1000000:
    t1 = (multi*0.7)
    t2 = (multi *0.2)
    t3 = (multi * 0.1)
    print(f"Se sembrara un 70% de pino eso equivale a {t1}, y se sembrara el 20% de oyamel eso equivale a {t2}, se sembrara 10% de cedro y eso equivale a {t3}")
elif multi<=1000000:
    t1 = (multi*0.5)
    t2 = (multi *0.3)
    t3 = (multi * 0.2)
    print(f"Se sembrara un 50% de pino eso equivale a {t1}, y se sembrara el 30% de oyamel eso equivale a {t2}, se sembrara 20% de cedro y eso equivale a {t3}")


"""Tercer Punto"""

"""Una persona debe realizar un muestreo con 50 personas para determinar el promedio de
peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional. Se
determinan las categorías con base en la siguiente tabla:"""


Cn = 0
Cj =0
Ca =0
Cv = 0

Cpn =0
Cpj =0
Cpa =0
Cpv =0

for n in range(10):
  edad = int(input("Ingrese la edad que ud tiene "))
  if edad<=12:
      Pn = int(input("Ingrese el peso que tiene el niño"))
      Cpn = Cpn + Pn
      Cn +=1
  elif edad<=29:
      Pj = int(input("Ingrese el peso que tiene el joven"))
      Cpj = Cpj + Pj
      Cj +=1
  elif edad<=59:
      Pa = int(input("Ingrese el peso que tiene el adulto"))
      Cpa = Cpa + Pa
      Ca +=1
  elif edad>=60:
      Pv = int(input("Ingrese el peso que tiene el viejo"))
      Cpv = Cpv + Pv
      Cv +=1

PmN = Cpn / Cn
PmJ = Cpj / Cj
PmA = Cpa / Ca
PmV = Cpv / Cv

print(f"El promedio de los niños son {PmN}")
print(f"El promedio de los jovenes son {PmJ}")
print(f"El promedio de los adulto son {PmA}")
print(f"El promedio de los Viejo son {PmV}")

"""Cuarto Punto"""

"""En una empresa se requiere calcular el salario semanal de cada uno de los n obreros que
laboran en ella. El salario se obtiene de la sig. forma: Si el obrero trabaja 40 horas o menos
se le paga $20 por hora, Si trabaja más de 40 horas se le paga $20 por cada una de las
primeras 40 horas y $25 por cada hora extra."""

for n in range(3):
    horas_trabajadas = int (input("Cuantas horas trabajas?"))
    if horas_trabajadas<=40:
      total = horas_trabajadas*20
      print(f"tu salario era de {total}")
    elif horas_trabajadas>40:
      total = int(40*20)
      mas = int ((horas_trabajadas-40)*25)
      print(f"tu salario era de {total+mas}")


"""Quinto Punto"""

"""Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero
que el teatro deja de percibir por cada una de las categorías. Tomar en cuenta que los
niños menores de 5 años no pueden entrar al teatro y que existe un precio único en los
asientos. Los descuentos se hacen tomando en cuenta el siguiente cuadro:"""

