# =========================================
#     Simulación de Cajero Automático 
# =========================================

saldo = 1000000

# =========================================
#            COSULTAR SALDO
# =========================================
def consultar_saldo():
    print("\n===CONSULTAR SALDO===")
    print(f"Su saldo esde: {saldo}")
    print("=======================")

# =========================================
#           REALISAR DEPOSITOS
# =========================================
def retiro():

    global saldo

    print("====RETIRO====")
    cuanto = float(input("Cuanto desea retirar: "))

    print("===FATURA===")
    print(f"retira: {cuanto}")
    print(f"Teniendo un sado de: {saldo}")
    saldo = saldo - cuanto
    print(f"Nuebo saldo: {saldo}")


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
    print("3. Salir")

    escoje = int(input("seleccione>> "))
    
    if escoje == 1:
        consultar_saldo()
    
    elif escoje == 2:
        retiro()
    
    else:
        print()


