##Punto No 1
#Cree una tupla llamada lenguajes con cinco lenguajes de programación. Muestre la tupla completa,
#el primer elemento, el último elemento y la cantidad total de elementos usando len(). Nivel sugerido:
#Básico.
Lenguajes=("C#","Python","Julia","Java","C++")
print(Lenguajes)
print(Lenguajes[1])
print(Lenguajes[-1])
print("Punto No1")
print("La cantidad de elementos de la tupla es: ",len(Lenguajes))
print("")
#---------------------------------------------------------------
##Punto No 2
#Defina una tupla con las edades de 10 personas. Recorra la tupla e imprima únicamente las edades
#mayores o iguales a 18 años. Al final, muestre cuántas personas son mayores de edad. Nivel sugerido:
#Básico.
edades=(18,22,19,25,21,10,2,5,3,7)
mayor=0
print("Punto No2")
print ("Edades Mayores o iguales a 18: ")
for may in edades:
    if may>=18:
        mayor=mayor+1
        print(may)
print("la cantidad de personas Mayores o iguales a 18 son: ",mayor)
print("")
#-----------------------------------------------------------------
#Punto No3
#Cree una tupla con ocho números enteros. Calcule y muestre la suma, el valor mayor, el valor menor
#y el promedio de los datos. Puede usar sum(), max() y min(). Nivel sugerido: Básico.
num=(1,2,9,5,3,5,8,12)
may=0
men=1000
suma=0
for i in num:
    if i>may:
        may=i
for i in num:
    if i<men:
        men=i
for i in num:
    suma=i+suma
print("Punto No3")
print("Por medio de For")
print("El promedio de los números es", sum(num)/len(num))
print("La suma de los números de la tupla es: ", suma)
print("El número más grande de la tupla es: ",may)
print("El número más pequeño de la tupla es: ",men)
print("Usando comando Sum(), Max, Min")
print("El promedio de los números es", sum(num)/len(num))
print("La suma de los números de la tupla es: ", sum(num))
print("El número más grande de la tupla es: ",max(num))
print("El número más pequeño de la tupla es: ",min(num))
print("")

#-----------------------------------------------------------------
#Punto No4
#Solicite al usuario una palabra y cree una tupla con cada uno de sus caracteres. Muestre la tupla y
#determine cuántas veces aparece la letra a. Tenga en cuenta mayúsculas y minúsculas. Nivel sugerido:
#Básico.

pal=input("Por favor ingrese la palabra, para identificar cuantas a hay ")
pal=list(pal)
pal=pal
print(pal)
cant=0
for p in pal:
    if p=="a" or p=="A":
        cant=cant+1
print("Punto No4")
print("La cantidad de letras a (A) en la palabra ingresada es: ",cant)
print("Usando Función count", pal.count("a")+pal.count("A"))
print("")

#-----------------------------------------------------------------
#Punto No5
#Cree una tupla con los días de la semana. Solicite al usuario un número entre 1 y 7 y muestre el
#día correspondiente. Valide que el número ingresado se encuentre dentro del rango permitido. Nivel
#sugerido: Intermedio.

dias=("Lunes","Martes","Miércoles","Jueves","Viernes","Sábado", "Domingo")
while True:
  num=int(input("Por favor ingrese el número de 1 a 7 para saber a cual día de la semana corresponde: "))
  if num>0 and num<8:
    print(f"El día de la semana a que corresponde el día {num} es al: ",dias[num-1])
    break
  else:
    print ("Ingrese un número entre el rango valido")
print("")

#------------------------------------------------------------------
#Punto No6
#Cree una tupla que represente los datos de un estudiante: nombre, edad, programa, semestre y
#promedio. Use desempaquetado para guardar cada dato en una variable diferente y muestre una
#ficha del estudiante en pantalla. Nivel sugerido: Intermedio.

datos=("Juan Perez","19","Estadistica","6","4.6")
nom,ed,pro,sem,prom=datos

print("Punto No6")
print("El Nombre del estudiante es: ",nom)
print("La Edad del estudiante es: ",ed)
print("El Programa que cursa es: ",pro)
print("El Semestre actual: ",sem)
print("El Promedio acumulado hasta el momento es: ",prom)
print("")

#-----------------------------------------------------------------------
#Punto No7
#Cree una tupla con las calificaciones de un estudiante. Solicite una nota al usuario y determine
#mediante count() cuántas veces aparece. Si aparece al menos una vez, indique además la primera
#posición en la que se encuentra usando index(). Nivel sugerido: Intermedio.

notas=(3,2,5,4,3,3.2,4.1,4.9,1.5,2.8,3.2,2,3,4,4,5)
notval=int(input("Por favor ingrese la nota a validar en el regsitro durante el semestre: "))

print("Esa nota ingresada aparece: {",notas.count(notval),"} veces")

if notas.count(notval) !=0:
  print("La posición de la nota en el registro es la número: ", notas.index(notval)+1, " (Contando desde 1)")
else:
  print("La nota ingresada no se encuentra en el registro")
print("")

#-------------------------------------------------------------------------
#Punto No8
#Diseñe un programa con una tupla de productos. Cada producto debe estar representado por una tupla 
#interna con la estructura (nombre, precio, cantidad). Recorra todos los productos, calcule el valor
# del inventario de cada uno y determine el valor total del inventario. Nivel sugerido: Intermedio.

product= (
    ("Impresora_Epson", 350000, 5),
    ("Celular_HuaweiMAX",1250000, 10),
    ("Nevera", 2750000, 6),
    ("Teclado_Lenovo", 125000, 15),
    ("Horno_Electrico_5L", 375000, 8))
valProd=0

print("Punto No 8 (Detalles de los productos)")

for nom, pre, cant in product:
    valItem = pre * cant
    valProd = valProd+valItem
    print(f"Producto: {nom} | Precio: ${pre} | Cantidad: {cant} | Total: ${valItem}")

print("")
print(f"El Total de los productos (Inventario Registrado) es: ${valProd}")
