# =========================================
#     Simulación de Cajero Automático 
# =========================================

saldo = 1000000

# =========================================
#            COSULTAR SALDO
# =========================================
def consultar_saldo():
    print("\n===CONSULTAR SALDO===")
    print(f"Su saldo es de: {saldo}")
    print("=======================")

# =========================================
#           REALISAR RETIRO 
# =========================================
def retiro():

    global saldo

    print("====RETIRO====")
    cuanto_RE = float(input("Cuanto desea retirar: "))

    print("===FATURA===")
    print(f"retira: {cuanto_RE}")
    saldo = saldo - cuanto_RE
    print(f"Nuebo saldo: {saldo}")
    print(f"============")

# =========================================
#               CONSIGNAR
# =========================================
def consignar():
    global saldo
    
    print("====COSIGNAR====")
    cuanto_CO = float(input("Cuan desea consignar: "))

    print("===FATURA===")
    print(f"consigna: {cuanto_CO}")
    saldo = saldo + cuanto_CO
    print(f"Nuedo saldo: {saldo}")
    print(f"==============")


# =========================================
#                INTERFAS
# =========================================
escoje = 0

while escoje != 4:
    print("=================")
    print("      BANCO")
    print("=================")
    print("1. Consultar saldo")
    print("2. retirar ")
    print("3. consignar")
    print("4. salir")
    print("=================")

    escoje = int(input("seleccione>> "))
    
    if escoje == 1:
        consultar_saldo()
    
    elif escoje == 2:
        retiro()
    
    elif escoje == 3:
        consignar()

    else:
        print()

print("SALIENDO...")

