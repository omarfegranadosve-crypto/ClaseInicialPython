#Operaciones de Suma, Resta, Multiplicación y División
def suma(a,b):
    return a+b;

def mult(a,b):
    return a*b;

def rest(a,b):
    return a-b;

def div(a,b):
    return a/b

num_1=int(input("Leer el número 1 :"))
num_2=int(input("Leer el número 2 y este número diferente de 0 :"))

print ("El Resultado de la suma es: ",suma(num_1,num_2))
print ("El Resultado de la resta en forma a-b: ",rest(num_1,num_2))
print ("El Resultado de la multiplicación: ",mult(num_1,num_2))
print ("El Resultado de la División considerando num1/num2: ",div(num_1,num_2)) 
