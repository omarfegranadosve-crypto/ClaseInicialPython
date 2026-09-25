#Desarrollar en Thonny un programa que permita registrar nombres de estudiantes
#Sus notas  y luego mostrar el resumen.
#guardar nombre de lista
#Guardar notas en otra lista
#Mostrar el promedio general
#Convertir los nombres a set para validar estudiantes únicos
#Mostrar los estudiantes registrados sin repetir
seg="s"
nomb=[]
nota=[]
sum=0
while (seg=="s"):
  nomb.append(input("Por favor ingrese el nombre del estudiante a agregar: "))
  nota.append(float(input("por favor ingrese la nota del estudiante: ")))
  seg=input("¿Desea agregar otro estudiante? (s/n): ")

for n in nota:
  sum=sum+n
prom=sum/len(nota)

print("Los estudiantes ingresados en la lsita son: ",nomb)
print("El promedio de las notas de los estudiantes anteriormente mostrados es de: ", prom)
print("Convirtiendo la lista en un set (eliminación de nombres repetidos: )", set(nomb))

#Ejecuta bajo las condiciones descritas
