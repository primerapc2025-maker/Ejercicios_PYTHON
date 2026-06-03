
inb = []
tt_inb = 0

# ============================

def registrar():
    print('')
    print('============================')
    print("     REGISTRAR PRODUCTOS")
    print('============================')
    print('')
    
    nom = input("Ingrece el nombre del producto: ")
    prec = float(input("Ingrese el presio del producto: $"))
    can = int(input("Ingrese la cantidad disponible: "))

    pro = (nom, prec, can)

    inb.append(pro)
    
    print('============================')

# ============================

def lista():
    print('')
    print('============================')
    print("     LISTA DE PRODUCTOS")
    print('============================')
    print('')

    if len(inb) == 0:
        print("No se han registrado probuctos")
    
    else:
        for pro in inb:

            print('============================')
            print("Nombre:", pro[0])
            print("Precio: $", pro[1])
            print("Stock:", pro[2])

# ============================

def bus_pro():
    print('')
    print('============================')
    print("      BUSCAR PRODUCTOS")
    print('============================')
    print('')

    buscar = input("Ingrese el nobre del producto: ")
    
    enc = False

    for pro in inb:

        if (buscar.lower() == pro[0].lower):
            print("Nombre:", pro[0])
            print("Precio: $", pro[1])
            print("Stock:", pro[2])

        enc = True

    if enc == False:
        print("Producto no encontrado")

# ============================
def valor_inbentario():
    global tt_inb

    for pro in inb:
        tt_ind = pro[1] * pro[2]
        print(tt_inb)

# ============================
opc = 0

while opc != 5:
    print("============================")
    print("    TIENDA DE TECNOLOGIA")
    print("============================")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. salir")
    print(f"total del inbentari: ${valor_inbentario}")
    print("============================")

    opc = int(input("Seleccione una opcion: "))

    if opc == 1:
        registrar()

    elif opc == 2:
        lista()
    
    elif opc == 3:
        bus_pro()

    elif opc == 4:
        print("Saliendo...")

    else:
        print("!Opcion invalida¡")
