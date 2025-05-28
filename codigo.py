import time

def tomar(nombre):
    print(f"{nombre} toma cerveza...")
    time.sleep(1)

def usar_baño(nombre):
    print(f"{nombre} orinando...")
    time.sleep(1)  
    print(f"{nombre} salio del baño...")

def llamada_ex(nombre):
    print(f"{nombre} llama a su ex y empieza a llorar...")
    time.sleep(2)
    print(f"{nombre} cuelga la llamada sintiéndose peor...")

def cantando(nombre):
    print(f"{nombre} empieza a cantar desafinadamente...")
    time.sleep(1.5)
    print(f"{nombre} termina su 'performance'...")

def borrachito(nombre, paso):
    if nombre == "Borrachito 0":
        if paso == 0:
            tomar(nombre)
        elif paso == 1:
            usar_baño(nombre)
        elif paso == 2:
            llamada_ex(nombre)
        else:
            cantando(nombre)
    elif nombre == "Borrachito 1":
        if paso == 0:
            usar_baño(nombre)
        elif paso == 1:
            tomar(nombre)
        elif paso == 2:
            cantando(nombre)
        else:
            tomar(nombre)
    elif nombre == "Borrachito 2":
        if paso == 0:
            cantando(nombre)
        elif paso == 1:
            llamada_ex(nombre)
        elif paso == 2:
            tomar(nombre)
        else:
            usar_baño(nombre)
    elif nombre == "Borrachito 3":
        if paso == 0:
            llamada_ex(nombre)
        elif paso == 1:
            cantando(nombre)
        elif paso == 2:
            usar_baño(nombre)
        else:
            tomar(nombre)

# Simulación secuencial con 4 ciclos
ciclos = 4
for ciclo in range(ciclos):
    print(f"\n--- Ciclo {ciclo + 1} ---")
    borrachito("Borrachito 0", ciclo % 4)
    borrachito("Borrachito 1", ciclo % 4)
    borrachito("Borrachito 2", ciclo % 4)
    borrachito("Borrachito 3", ciclo % 4)

print("\nSimulación completada!")
