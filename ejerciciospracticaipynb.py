#Presebtado por Omar Fernando GRanados Vergara
#Cód 150346
# ------------------------------------------------------------------------------
# PUNTO No1
print("Punto No1 ingrese los siguientes datos solitados para cisualizarlos en pantalla")
nom = input("Ingrese nombre: ")
ed = int(input("Ingrese edad: "))
est = float(input("Ingrese estatura en metros: "))
estu = input("¿Estudia actualmente? (si/no): ").strip().lower() == "si"
print(f"\nNom: {nom} | Tipo: {type(nom)}")
print(f"Ed: {ed} | Tipo: {type(ed)}")
print(f"Est: {est} | Tipo: {type(est)}")
print(f"Estu: {estu} | Tipo: {type(estu)}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO No2
print("Punto No2 ingrese Dos números (cualesquiera), para validar las operaciones básicas:")
n1 = float(input("Ingrese el Número 1: "))
n2 = float(input("Ingrese el Número 2: "))
print(f"\n La Suma es : {n1 + n2}")
print(f"La Resta es: {n1 - n2}")
print(f"La Multiplicación es: {n1 * n2}")
if n2 != 0:
    d = n1 / n2
    print(f"La División es : {d}\n")
else:
    print("Div: Error (división por cero)\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO No3
print("Punto No3 ingrese Los datos para cálcular el área de un triángulo y posterior los lados para el perimetro:")
b = float(input("Por favor ingrese la Base: "))
h = float(input("Por Favor ingrese la Altura: "))
a = (b * h) / 2
print(f"EL Área del triángulo es: {a}")

l1 = float(input("Ingrese el Lado 1: "))
l2 = float(input("Ingrese el Lado  2: "))
l3 = float(input("Ingrese el Lado 3: "))
per = l1 + l2 + l3
print(f"El Perímetro del triángulo es: {per}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO No4
print("Venta de productos de una tienda, por lo que ingrese la siguiente información:")
p_u = float(input("Precio unitario: "))
cant = int(input("Cantidad: "))
p_desc = float(input("Porcentaje descuento (%): "))
print(f"Subtotal: {p_u * cant}")
print(f"Desc ({p_desc}%): {(p_u * cant)* (p_desc / 100)}")
print(f"Subtotal c/desc: {((p_u * cant)-((p_u * cant)* (p_desc / 100)))}")
print(f"IVA (19%): {((p_u * cant)*0.19)}")
print(f"Total: {(p_u * cant)-((p_u * cant)* (p_desc / 100))+((p_u * cant)*0.19)}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO No5
seg_t = int(input("Por Favor ingresar la cantidad total de Segundos que quiere conocer en horas y minutos: "))
hrs = seg_t // 3600
res_s = seg_t % 3600
mins = res_s // 60
segs = res_s % 60
print(f"Son {hrs} hora(s), {mins} minuto(s) y {segs} segundo(s)\n")
# ------------------------------------------------------------------------------
# PUNTO 6
num = int(input("Ingrese un número entero para saber si es positivo ó negativo y par o impar: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Es Cero")

if num != 0:
    if num % 2 == 0:
        print("Par\n")
    else:
        print("Impar\n")
# ------------------------------------------------------------------------------
# PUNTO No7
ed = int(input("Ingrese la edad que desea determinar si es un niño, adolescente, adulto o adulto mayor: "))
if ed < 0:
    print("Edad inválida")
elif ed <= 11:
    print("Clasificado como Niño\n")
elif ed <= 17:
    print("Clasificado como Adolescente\n")
elif ed <= 59:
    print("Clasificado como Adulto\n")
else:
    print("Clasificado como Adulto Mayor\n")

print("Menores o iguales de 11 años son niños")
print("Entre 11 y 17 años son Adolescentes")
print("Entre 18 y 59 años son Adultos")
print("Mayores de 60 años son Adultos Mayores\n")
# ------------------------------------------------------------------------------
# PUNTO No8
print("Por favor ingrese tres(3) números  para determinar cual es el mayor o su defecto iguales")
n1 = float(input("Ingrese el primer Número N1: "))
n2 = float(input("Ingrese el segundo Número N2: "))
n3 = float(input("Ingrese el Tercer Número N3: "))
may = max(n1, n2, n3)
men = min(n1, n2, n3)
print(f"Mayor: {may} | Menor: {men}")
if n1 == n2 == n3:
    print("Los Tres (3) valores son iguales\n")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Existen Dos (2) valores repetidos\n")
else:
    print("Todos los valores son distintos\n")
# ------------------------------------------------------------------------------
# PUNTO No9
print("Ingreso de nota, para la clasificación del estudiante")
nt = float(input("Ingrese la nota entre el rango de (0.0 a 5.0): "))

if nt < 0.0 or nt > 5.0:
    print("Error: Nota fuera del rango\n")
else:
    if nt < 3.0:
        print("Reprobado\n")
    elif nt < 3.5:
        print("Aprobado\n")
    elif nt < 4.5:
        print("Sobresaliente\n")
    else:
        print("Excelente\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO No10
u_val, p_val = "admin", "1234"
c_min, c_max = 1000, 9999
print("Bienvenido al sistema de Validación de Usuario y Contraseña")
u = input("Usuario: ")
p = input("Contraseña: ")
c_v = int(input("Código verificación (1000-9999): "))

if u != u_val:
    print("Acceso denegado: Usuario incorrecto\n")
elif p != p_val:
    print("Acceso denegado: Contraseña incorrecta\n")
elif c_v < c_min or c_v > c_max:
    print("Acceso denegado: Código de verificación fuera de rango\n")
else:
    print("¡Ingreso exitoso!\n")
print ("")
# ------------------------------------------------------------------------------
# PUNTO No11
print ("Muestreo de los números del 1 al 100 y posterior multiplos de 5 que hay en este rango")
print("Del 1 al 100:")
for i in range(1, 101):
    print(i, end=" ")

print("\n Múltiplos de 5:")
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=" ")
print("")
# ------------------------------------------------------------------------------
# PUNTO 12
print("Validación Tabla de multiplicar con números positivos")
n = int(input("Ingrese un número entero positivo: "))

if n > 0:
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")
    print()
else:
    print("El número debe ser positivo\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 13
print(" ingreso de 10 números. Donde, muestra la suma, el promedio, el número mayor, el número menor  y la cantidad de pares ")
s = 0
c_par = 0
may = None
men = None

for i in range(10):
    val = float(input(f"Num {i+1}/10: "))
    s += val
    if may is None or val > may:
        may = val
    if men is None or val < men:
        men = val
    if val % 2 == 0:
        c_par += 1

prom = s / 10
print(f"Suma #: {s} | Prom #: {prom} | # Mayor: {may} | # Menor: {men} | Cant # Pares: {c_par}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 14
print("Validación de contraseña con intentos")
p_cor = "pcontraseña"
int_r = 3

while int_r > 0:
    p_ing = input("Contraseña: ")
    if p_ing == p_cor:
        print("Acceso concedido\n")
        break
    else:
        int_r -= 1
        print(f"Contraseña incorrecta. Intentos restantes: {int_r}")

if int_r == 0:
    print("Cuenta bloqueada\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 15
print("Ingreso de números enteros hasta que ingrese 0 para salir")
c_t = 0
c_p = 0
c_n = 0
s_n = 0

while True:
    v = int(input("Ingrese los números enteros que quiera: "))
    if v == 0:
        break
    c_t += 1
    s_n += v
    if v > 0:
        c_p += 1
    else:
        c_n += 1

print(f"Total ingresados: {c_t}")
print(f"Positivos: {c_p} | Negativos: {c_n}")
if c_t > 0:
    print(f"El Promedio es: {s_n / c_t:.2f}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 16
print("Validación de números pares")
def f_par(n):
    return n % 2 == 0

for i in range(5):
    val = int(input(f"Evaluando número {i+1}: "))
    print(f"¿Es par?: {f_par(val)}")
print()
# ------------------------------------------------------------------------------
# PUNTO 17
print("Datos para el cálculo de Área y perímetro de un rectángulo")
def f_a(b, h):
    return b * h

def f_p(b, h):
    return 2 * (b + h)

b_in = float(input("Base rectángulo: "))
h_in = float(input("Altura rectángulo: "))

print(f"Área: {f_a(b_in, h_in)} | Perímetro: {f_p(b_in, h_in)}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 18
print("Ingreso de datos de estudiante para el Cálculo de promedio y su estado")
def f_prom(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def f_est(prom):
    return "Aprobado" if prom >= 3.0 else "Reprobado"

n1 = float(input("Ingrese Nota 1: "))
n2 = float(input("Ingrese Nota 2: "))
n3 = float(input("Ingrese Nota 3: "))

p = f_prom(n1, n2, n3)
e = f_est(p)
print(f"Promedio: {p:.2f} | Estado: {e}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 19
print("Ingreso de datos para el Cálculo de Precio Final de los productos")
def f_pfinal(p, d):
    return p * (1 - d / 100)

precio = float(input("Precio: "))
desc = float(input(" Descuento (%): "))

if precio >= 0 and 0 <= desc <= 100:
    res = f_pfinal(precio, desc)
    print(f"Precio Final: {res:.2f}\n")
else:
    print("Datos de entrada inválidos\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 20
print("Calculadora de Suma, Resta, Multiplicación y División")
def f_sum(a, b): return a + b
def f_res(a, b): return a - b
def f_mul(a, b): return a * b
def f_div(a, b): return a / b if b != 0 else "Error: div por 0"

while True:
    print("MENÚ ")
    print("1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir | 5. Salir")
    op = input("Opción: ")
    if op == "5":
        print("Saliendo de la calculadora...\n")
        break
    if op in ["1", "2", "3", "4"]:
        a = float(input("P20 - Num 1: "))
        b = float(input("P20 - Num 2: "))
        if op == "1": print("Resultado:", f_sum(a, b))
        elif op == "2": print("Resultado:", f_res(a, b))
        elif op == "3": print("Resultado:", f_mul(a, b))
        elif op == "4": print("Resultado:", f_div(a, b))
        print()
    else:
        print("Opción inválida\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 21
print("Conteo regresivo de 10 a 1:")
def f_reg(n):
    # CASO BASE: Si n es menor a 1, detiene la recursión
    if n < 1:
        return
    print(n, end=" ")
    f_reg(n - 1)

print("Conteo regresivo de 10 a 1:")
f_reg(10)
print("\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 22
print("Suma acumulada de 1 hasta n:")
def f_srec(n):
    if n == 1: # Caso base
        return 1
    return n + f_srec(n - 1)

n_val = int(input("Ingrese n >= 1: "))
if n_val >= 1:
    print(f"Suma acumulada: {f_srec(n_val)}\n")
else:
    print("Error: n debe ser mayor o igual a 1\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 23
print("Factorial de un número:")
def f_fact(n):
    if n == 0 or n == 1: # Caso base
        return 1
    return n * f_fact(n - 1)

print("Pruebas de Factorial:")
for v in [0, 1, 5, 7]:
    print(f"{v}! = {f_fact(v)}")
print()
print("")

# ------------------------------------------------------------------------------
# PUNTO 24
print("Inverso de una cadena de texto:")
def f_inv(cad):
    if len(cad) <= 1: # Caso base
        return cad
    return f_inv(cad[1:]) + cad[0]

txt = "programar"
print(f"Texto original: {txt} | Invertido: {f_inv(txt)}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 25
print("Suma de dígitos de un número:")
def f_sdig(n):
    if n < 10: # Caso base
        return n
    return (n % 10) + f_sdig(n // 10)

num_in = int(input("Ingrese un número entero positivo: "))
if num_in >= 0:
    print(f"Suma de sus dígitos: {f_sdig(num_in)}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 26
print("Muestreo de información de Tupla Ciudades:")
t_ciu = ("Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Manizales")

print("Análisis de Tupla Ciudades:")
print(f"Primera: {t_ciu[0]}")
print(f"Última: {t_ciu[-1]}")
print(f"Total elementos: {len(t_ciu)}")
print("Posiciones pares:", t_ciu[0::2], "\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 27
print("Análisis de Notas de Estudiantes:")
t_nts = (3.5, 4.2, 2.8, 5.0, 3.0, 1.5, 4.8, 3.9, 2.0, 4.5)

may = max(t_nts)
men = min(t_nts)
prom = sum(t_nts) / len(t_nts)
c_ap = sum(1 for x in t_nts if x >= 3.0)

print(f"Mayor: {may} | Menor: {men} | Prom: {prom:.2f} | Aprobadas (>=3.0): {c_ap}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 28
print("Análisis de Productos:")
t_prod = (101, "Teclado Mecanico", 45000.0, 15)

cod, nom, pr, cant = t_prod
val_t = pr * cant

print(f"Cód: {cod} | Nombre: {nom} | Inventario Total: ${val_t}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 29
print("Clasificación de Estudiantes:")
t_est = (
    ("Ana", 4.5),
    ("Luis", 3.8),
    ("Pedro", 4.0),
    ("María", 2.9),
    ("Sofia", 4.9)
)

print("Estudiantes sobresalientes (Promedio >= 4.0):")
for nom, prom in t_est:
    if prom >= 4.0:
        print(f"- {nom}: {prom}")
print()
print("")

# ------------------------------------------------------------------------------
# PUNTO 30
print("Busqeuda de Números en la tupla:")
t_num = (5, 2, 8, 5, 3, 5, 9, 1)
val_b = int(input(" Ingrese un número a buscar en la tupla (de 1 a 9): "))

# Solución A: Métodos integrados
print("\n Método Nativo (.count() / .index()) ")
cnt = t_num.count(val_b)
print(f"Aparece {cnt} veces")
if cnt > 0:
    print(f"Primera aparición en la posición: {t_num.index(val_b)}")

# Solución B: Algoritmo manual
print("\nMétodo Algorítmico (paso a paso)")
c_man = 0
p_man = -1

for idx in range(len(t_num)):
    if t_num[idx] == val_b:
        c_man += 1
        if p_man == -1:
            p_man = idx

print(f"Aparece {c_man} veces")
if p_man != -1:
    print(f"Primera aparición en la posición: {p_man}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 31
print("Ingreso de Nombres por medio de .append():")
l_nom = []
for i in range(5):
    l_nom.append(input(f"Nombre {i+1}: "))

print(f"Lista de nombres: {l_nom} | Cantidad: {len(l_nom)}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 32
print("Ingreso de Números por medio de .append():")
l_n = [12, 7, 22, 5, 18, 9, 30, 4, 11, 15]

s = sum(l_n)
prom = s / len(l_n)
may = max(l_n)
men = min(l_n)
l_par = [x for x in l_n if x % 2 == 0]

print(f"P32 - Suma: {s} | Promedio: {prom} | Mayor: {may} | Menor: {men}")
print(f"Números Pares: {l_par}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 33
print("Ingreso de Productos modificando los actuales:")
l_p = [input(f"Producto inicial {i+1}: ") for i in range(5)]
print(f"Lista actual: {l_p}")

p_bus = input("Nombre de producto a buscar: ")
if p_bus in l_p:
    print(f"Encontrado en índice: {l_p.index(p_bus)}")
else:
    print("Producto no registrado")

p_mod = input("Nombre de producto a modificar: ")
if p_mod in l_p:
    idx = l_p.index(p_mod)
    l_p[idx] = input("Nuevo nombre para el producto: ")
    print(f"Lista tras modificación: {l_p}")

p_eli = input("Nombre de producto a eliminar: ")
if p_eli in l_p:
    l_p.remove(p_eli)
    print(f"Lista tras eliminación: {l_p}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 34
print("Ingreso de Notas de Estudiantes:")
l_nts = []
while True:
    n = float(input("Ingrese nota (-1 para finalizar): "))
    if n == -1:
        break
    if 0.0 <= n <= 5.0:
        l_nts.append(n)
if l_nts:
    l_nts.sort()
    prom = sum(l_nts) / len(l_nts)
    med = l_nts[len(l_nts) // 2]
    c_ap = sum(1 for x in l_nts if x >= 3.0)

    print(f"Notas Ordenadas: {l_nts}")
    print(f"Promedio: {prom:.2f} | Mediana Aprox: {med} | Aprobados: {c_ap}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 35
print("Ingreso de Inventario de Productos (lista de Listas):")
l_inv = []
for i in range(5):
    nom = input(f"Prod {i+1} nombre: ")
    pr = float(input("Precio: "))
    cant = int(input("Cantidad: "))
    l_inv.append([nom, pr, cant])
tot_gen = 0
m_inv = ["", 0] # Nombre, Valor Total
for p in l_inv:
    v_tot = p[1] * p[2]
    tot_gen += v_tot
    print(f"Producto: {p[0]} | Valor Inventario: ${v_tot:.2f}")
    if v_tot > m_inv[1]:
        m_inv = [p[0], v_tot]
print(f"\nValor Total Almacenado: ${tot_gen:.2f}")
print(f"Mayor Inversión en: {m_inv[0]} (${m_inv[1]:.2f})\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 36
print("Eliminación de duplicados de una lista Uso de SETS:")
l_col = ["Rojo", "Azul", "Rojo", "Verde", "Azul", "Amarillo"]
s_col = set(l_col)

print(f"Lista original con duplicados: {l_col}")
print(f"Set resultante sin repetidos: {s_col}")
# Explicación: Los conjuntos en Python son estructuras de datos no ordenadas que
# por definición lógica no admiten elementos repetidos, descartándolos automáticamente.
print()
print("")
# ------------------------------------------------------------------------------
# PUNTO 37
print(" lista a sets:")
l_in = [int(input(f"Entero {i+1}/10: ")) for i in range(10)]
s_u = set(l_in)

print(f"Cantidad de valores únicos ingresados: {len(s_u)}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 38

c1 = {"Ana", "Juan", "Pedro", "Maria"}
c2 = {"Pedro", "Maria", "Luis", "Sofia"}
print("Análisis de Cursos por medio de conjuntos:")
print("Inscritos en ambos cursos:", c1 & c2)
print("Solamente en el primer curso:", c1 - c2)
print("Solamente en el segundo curso:", c2 - c1)
print("Todos los estudiantes inscritos:", c1 | c2, "\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 39
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print("Operaciones Conjuntistas:")
print("Unión (todos los elementos sin duplicar):", s1 | s2)
print("Intersección (elementos presentes en ambos):", s1 & s2)
print("Diferencia s1 - s2 (elementos de s1 que no están en s2):", s1 - s2)
print("Diferencia Simétrica (elementos no compartidos):", s1 ^ s2, "\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 40
d1 = {101, 102, 103, 104, 105}
d2 = {103, 105, 106, 107}
rec = d1 & d2
nuev_d2 = d2 - d1
unic_un_dia = d1 ^ d2
print(f" Usuarios recurrentes (Día 1 y Día 2): {rec}")
print(f" Usuarios nuevos registrados el Día 2: {nuev_d2}")
print(f" Usuarios que ingresaron exactamente solo un día: {unic_un_dia}\n")
print("")
# ------------------------------------------------------------------------------
# PUNTO 41
def f_prom(nts): return sum(nts) / len(nts)
def f_est(prom): return "Aprobado" if prom >= 3.0 else "Reprobado"
l_reg = []
n_est = int(input("Número de estudiantes a registrar: "))
for _ in range(n_est):
    nom = input("Nombre estudiante: ")
    nts = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    p = f_prom(nts)
    e = f_est(p)
    l_reg.append({"nom": nom, "prom": p, "est": e})
p_gen = sum(x["prom"] for x in l_reg) / len(l_reg)
m_est = max(l_reg, key=lambda x: x["prom"])
print(f"\nPromedio General Grupo: {p_gen:.2f}")
print(f"Mejor Desempeño: {m_est['nom']} con Promedio {m_est['prom']:.2f}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 42
def f_add(inv):
    c = int(input("Código: "))
    p = input("Producto: ")
    pr = float(input("Precio: "))
    cnt = int(input("Cantidad: "))
    inv.append((c, p, pr, cnt))
def f_show(inv):
    for item in inv:
        print(f"Cód: {item[0]} | Prod: {item[1]} | Precio: ${item[2]} | Cant: {item[3]}")
def f_tot(inv):
    return sum(item[2] * item[3] for item in inv)
inv = []
f_add(inv)
f_show(inv)
print(f"Valor Total Inventario: ${f_tot(inv):.2f}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 43
l_res = ["Python", "Java", "Python", "C++", "Python", "Java", "JavaScript"]
s_leng = set(l_res)
print("Lenguajes Unicos Registrados:", s_leng)
for leng in s_leng:
    print(f"- {leng}: Votado {l_res.count(leng)} vez/veces")
print()
print("")

# ------------------------------------------------------------------------------
# PUNTO 44
def f_proc(l_num):
    par = [x for x in l_num if x % 2 == 0]
    imp = [x for x in l_num if x % 2 != 0]
    pos = [x for x in l_num if x > 0]
    neg = [x for x in l_num if x < 0]
    prom = sum(l_num) / len(l_num) if l_num else 0
    u_vals = set(l_num)
    res_t = (len(par), len(imp), len(pos), len(neg), prom)
    return u_vals, res_t
nums = [12, -5, 0, 7, -2, 12, 8]
unicos, resumen = f_proc(nums)
print(f"Valores Únicos (Set): {unicos}")
print(f"Resumen (Cant_Pares, Cant_Impares, Pos, Neg, Promedio): {resumen}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 45
def f_srec(lst):
    if not lst: # Caso base: lista vacía
        return 0
    return lst[0] + f_srec(lst[1:])
l_vals = [10, 20, 30, 40, 50]
res_rec = f_srec(l_vals)
res_ciclo = 0
for x in l_vals:
    res_ciclo += x
print(f"Lista: {l_vals}")
print(f"Resultado Recursivo: {res_rec} | Resultado Iterativo: {res_ciclo}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 46
def f_busrec(tup, val, idx=0):
    if idx >= len(tup): # Caso base: no encontrado
        return -1
    if tup[idx] == val: # Caso base: encontrado
        return idx
    return f_busrec(tup, val, idx + 1)
t_datos = (10, 25, 40, 55, 70)
v = int(input("Valor a buscar en la tupla: "))
pos = f_busrec(t_datos, v)
if pos != -1:
    print(f"Valor encontrado en el índice: {pos}\n")
else:
    print("Valor no encontrado en la tupla (-1)\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 47
def f_desc(monto):
    return 0.10 if monto > 100000 else 0.05
def f_iva(sub):
    return sub * 0.19
l_ventas = []
while True:
    m = float(input("Monto de venta (0 para terminar): "))
    if m == 0:
        break
    d = m * f_desc(m)
    sub = m - d
    i = f_iva(sub)
    tot = sub + i
    l_ventas.append(tot)
if l_ventas:
    tot_v = sum(l_ventas)
    prom_v = tot_v / len(l_ventas)
    print(f"\nTotal General Vendido: ${tot_v:.2f}")
    print(f"Promedio por Compra: ${prom_v:.2f}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 48
def f_analizar(l1, l2):
    s1, s2 = set(l1), set(l2)
    rep = s1 & s2
    u_j1 = s1 - s2
    u_j2 = s2 - s1
    t_dif = s1 | s2
    return rep, u_j1, u_j2, t_dif
j1 = ["Juan", "Ana", "Pedro", "Maria"]
j2 = ["Pedro", "Luis", "Maria", "Sofia"]
rep, u1, u2, tot = f_analizar(j1, j2)
print("Análisis de Asistencia:")
print(f"Asistentes a ambas jornadas: {rep}")
print(f"Exclusivos de la Jornada 1: {u1}")
print(f"Exclusivos de la Jornada 2: {u2}")
print(f"Total personas distintas: {len(tot)}\n")
print("")

# ------------------------------------------------------------------------------
# PUNTO 49
def f_list(bib):
    for b in bib:
        st = "Prestado" if b[3] else "Disponible"
        print(f"Código: {b[0]} | Título: {b[1]} | Autor: {b[2]} | Estado: {st}")
def f_pres(bib, cod):
    for i, b in enumerate(bib):
        if b[0] == cod:
            if b[3]:
                print("Operación rechazada: El libro ya se encuentra prestado")
            else:
                bib[i] = (b[0], b[1], b[2], True)
                print("Préstamo registrado exitosamente")
            return
    print("Error: Código no existe")
bib = [
    (1, "100 Años de Soledad", "G. García Márquez", False),
    (2, "El Principito", "A. Saint-Exupéry", False)
]
print(" Catálogo Inicial:")
f_list(bib)
print("\nRealizando préstamo de libro cód 1:")
f_pres(bib, 1)
print("\nIntentando prestar de nuevo cód 1:")
f_pres(bib, 1)
print()
print("")

# ------------------------------------------------------------------------------
# PUNTO 50
def f_srec(nts, idx=0):
    if idx == len(nts):
        return 0
    return nts[idx] + f_srec(nts, idx + 1)
ests = [
    {"nom": "Ana", "nts": (4.5, 3.8, 5.0)},
    {"nom": "Carlos", "nts": (2.5, 3.0, 2.8)},
    {"nom": "Beatriz", "nts": (4.0, 4.2, 4.5)}
]
all_nts = set()
print(" Reporte Académico Final ---")
for e in ests:
    s_nt = f_srec(e["nts"])
    p = s_nt / len(e["nts"])
    clas = "Excelente" if p >= 4.5 else ("Aprobado" if p >= 3.0 else "Reprobado")
    all_nts.update(e["nts"])
    print(f"Estudiante: {e['nom']} | Suma Notas: {s_nt:.2f} | Promedio: {p:.2f} | Estado: {clas}")
print("\n--- Estadísticas Globales ---")
print(f"Set de notas únicas registradas en el sistema: {all_nts}")
print("")
