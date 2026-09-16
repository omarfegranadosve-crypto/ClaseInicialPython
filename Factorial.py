def factorial (n):
    print("Entrando con n= ",n)
    if n==1:
        return 1
    return n*factorial(n-1)

    
n=int(input("Ingrese el numero a usar el factorial "))
factorial(n)