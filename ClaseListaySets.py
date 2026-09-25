#Como crear una lista
frutas=["manzana","pera","uva"]
numeros=[10,20,30,40]
mixta=["Ana",18,4.5,True]

print(frutas)
print(numeros)
print(mixta)

#Indices de Listas
print("")
estudiantes=["Laura","Carlos","Diana","Mateo"]
print(estudiantes[0]) #Laura
print(estudiantes[1]) #Carlos
print(estudiantes[-1])#Mateo
print("")
#Uso de append, remove
notas=[3,4.2,2.8]
notas.append(5.0) #agrega un elmento a la lista
notas[0]=3.5      #reescribe la posición
notas.remove(2.8) #Elimina el valor 2.8
print("Retorno de La lista con el uso de append, reescribir y eliminar")
print(notas)
print("")
#--------------------------------------------
notas =[4.0,3.5,2.9,5.0]
for nota in notas:
    print("Nota:",nota)
#--------------------------------------------
notas =[4.0,3.5,2.9,5.0]
suma=0
print("")
for nota in notas:
    suma=suma+nota
promedio=suma/len(notas)
print("Promedio:",promedio)
#--------------------------------------------
#En el set se elimina elmentos repetidos, como en el ejemplo
numeros={1,2,3,3,4,4,5}
print(numeros)
nombres={"Ana","Luis","Ana","Marta"}
print(nombres)
#---------------------------------------------
#discard permite para eliminar elemento de la lista
#En set es mejor discard que remove
usuarios={"ana","luis","marta"}
usuarios.add("carlos")
usuarios.discard("luis")
print(usuarios)
#-------------------------------------------------------
ciudades=["Bogotá","Calí","Bogotá","Medellín"]
ciudades_unicas = set(ciudades)
print("")
print(ciudades)
print(ciudades_unicas)
print("")
#---------------------------------------------------------
#descripción de Conjunto, Intersección y Diferencia / Solo en los sets
grupo_a={"Ana","Luis","Marta"}
grupo_b={"Luis","Carlos","Diana"}
print("Descripción de los elementos de conjuntos")
print(grupo_a | grupo_b) #Unión
print(grupo_a & grupo_b) #Intersección
print(grupo_a - grupo_b) #Diferencia
print("")
#-----------------------------------------------------------
#Aplicación de uso de set con diferencia
inscritos ={"Ana","Luis","Marta","Carlos"}
asistieron ={"Ana","Carlos"}

faltaron= inscritos - asistieron
print("Faltaron: ",faltaron)

#------------------------------------------------------------
#Ejercicio Guiado No1
print("Ejercicio Guiado No1")
print("Ingrese cinco (5) notas")

notas=[]

for i in range(5):
    nota=float(input("Digite una nota: "))
    notas.append(nota)
    
promedio=sum(notas)/len(notas)
print("Promedio: ",promedio)
print("Mayor: ",max(notas))
print("Menor: ",min(notas))
#-------------------------------------------------------------
#Ejercicio Guiado No2
print("Ejercicio Guiado No2")

codigos=[]

for i in range(6):
    codigo=float(input("Digite el código: "))
    codigos.append(codigo)
    
codigos_unicos=set(codigos)
print("Todos: ",codigos)
print("Unicos (códigos no repetidos): ",codigos_unicos)
