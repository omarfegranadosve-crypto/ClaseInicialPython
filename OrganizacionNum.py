#organización de Números
val=[1,7,8,9,3]
aux=0
for i in range (0,len(val)):
   for j  in range (len(val)-1):
       if val[j]> val[j+1]:
            aux=val[j]
            val[j]=val[j+1]
            val[j+1]=aux
            print (val[j],val[j+1],aux)
    
print (val)
