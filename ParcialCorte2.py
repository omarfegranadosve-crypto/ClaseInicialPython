# Catálogo inicial de productos (codigo, nombre, precio, stock, categoria)
cat = [
    ("P01", "Mouse", 45000, 10, "Perifericos"),
    ("P02", "Teclado", 80000, 8, "Perifericos"),
    ("P03", "Memoria USB", 35000, 15, "Almacenamiento"),
    ("P04", "Audifonos", 65000, 6, "Audio"),
    ("P05", "Webcam", 120000, 5, "Video")
]
vent = []
prod_ven = set()
cl_at = set()
def calc_desc(subt):
    if subt < 100000:
        return 0.0
    elif subt < 250000:
        return 0.05
    else:
        return 0.10
def busc_prod(cat, cod):
    for i in range(len(cat)):
        if cat[i][0] == cod:
            return i
    return -1
def sum_vent(vent, pos):
    if pos == len(vent):
        return 0
    return vent[pos][6] + sum_vent(vent, pos + 1)
while True:
    try:
        num_vent = int(input("¿Cuántas ventas desea registrar del día?: "))
        if num_vent > 0:
            break
        print("Debe ingresar un número mayor a cero.")
    except ValueError:
        print("Debe ingresar un número (valor) válido.")
for i in range(num_vent):
    print("")
    print(f"Registro de la Venta No {i + 1}")
    print("")
    nom_cl = input("Nombre del cliente: ")
    while not nom_cl:
        nom_cl = input("El nombre debe tener al menos un carácter. Ingrese la información nuevamente: ")
    while True:
        cod_prod = input("Ingrese el código del producto (RECUERDE QUE DEBE SER EN MAYÚSCULAS): ")
        pos_prod = busc_prod(cat, cod_prod)
        if pos_prod != -1:
            break
        print("El código ingresado NO existe en el catálogo. Intente nuevamente.")

    prod_id, prod_nom, prod_pre, prod_stock, prod_cat = cat[pos_prod]
    while True:
        cant = int(input(f"Cantidad a comprar, En Stock disponible es: {prod_stock}): "))
        if cant <= 0:
            print("La cantidad de productos debe ser un entero mayor que cero.")
        elif cant > prod_stock:
            print("No hay suficiente stock. Solo quedan {",prod_stock,"} unidades.")
        else:
            break

    subtot = prod_pre * cant
    porc_desc = calc_desc(subtot)
    desc_pes = subtot * porc_desc
    subtot_desc = subtot - desc_pes
    iva = subtot_desc * 0.19
    totFin = subtot_desc + iva
    nv_stock = prod_stock - cant
    cat[pos_prod] = (prod_id, prod_nom, prod_pre, nv_stock, prod_cat)
    vent_act = (nom_cl, cod_prod, cant, subtot, desc_pes, iva, totFin)
    vent.append(vent_act)
    cl_at.add(nom_cl)
    prod_ven.add(cod_prod)
    
    print("La venta fue registrada con éxito")
    print("El Total a pagar es: ${",totFin,"}")
print("")
print("VENTAS DEL DÍA")
print("")
print("El número de ventas registradas es:", len(vent))
totDia = sum_vent(vent, 0)
print("El Total vendido en el día (jornada): $",totDia,"")
prom_vent = totDia / len(vent) if len(vent) > 0 else 0
print("Promedio ventas: $",prom_vent)
print("La cantidad de clientes diferentes atendidos es:", len(cl_at))
print("Los códigos de los productos vendidos es:", prod_ven)
tod_cod = set([prod[0] for prod in cat])
prodNoVen = tod_cod.difference(prod_ven)
print("Códigos de productos NO vendidos:", prodNoVen)
ventMayor = vent[0]
for v in vent:
    if v[6] > ventMayor[6]:  
        ventMayor = v
print("Venta de mayor valor: ${",ventMayor[6],"} (Cliente: {",ventMayor[0],"})")
print("")
print("Catálogo Actualizado:")
print("")
for prod in cat:
    print(f" Código: {prod[0]} | Producto: {prod[1]} | Precio: ${prod[2]} | Stock Restante: {prod[3]} | Categoría: {prod[4]}")