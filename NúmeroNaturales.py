def suma_naturales(n):
    if n==1:
        return 1;
    else:
        return n+suma_naturales(n-1);
    
numero=int(input("Digite un número positivo: "))
print("Suma:",suma_naturales(numero))