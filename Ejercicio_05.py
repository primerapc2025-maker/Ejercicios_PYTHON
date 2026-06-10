contactos = []

# ========================================

def nuevo():
    print("========================")
    print("    NUEVO CONTACTO")
    print("========================")

    nombre = set(input("Ingrese el nombre: "))
    numero = int(input("Ingrese el numero: "))

    contac = (nombre, numero)
    contactos.append(contac)

    print("...contacto registrado..")

# ========================================
def buscar():
    print("========================")
    print("    BUSCAR CONTACTO")
    print("========================")
    
