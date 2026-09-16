def potencia(base,exponente):
    if exponente ==0:
        return 1;
    else:
        return base*potencia(base,exponente-1)
    
nb=int(input("Ingrese el Número base"))
nexp=int(input("Ingrese el Número al que quiere"))

potencia(nb,nexp)
