import time
import random

# Definición de acciones
def tomar(nombre):
    print(f"{nombre} está tomando cerveza...")
    time.sleep(0.7)

def usar_baño(nombre):
    print(f"{nombre} está en el baño...")
    time.sleep(1.2)
    print(f"{nombre} salió del baño.")

def llamada_ex(nombre):
    print(f"{nombre} está hablando con su ex... (¡Qué incómodo!)")
    time.sleep(1.8)
    print(f"{nombre} colgó llorando")

def cantando(nombre):
    print(f"{nombre} está cantando rancheras desafinadas")
    time.sleep(1)

# Lista de borrachitos
borrachitos = ["Borrachito 0", "Borrachito 1", "Borrachito 2", "Borrachito 3", "Borrachito 4"]
acciones_disponibles = ["tomar", "cantar", "baño", "llamar ex"]

# Función para generar secuencia aleatoria válida
def generar_secuencia_valida():
    while True:
        # Mezclar acciones
        secuencia = random.sample(acciones_disponibles, 4)
        
        # Verificar que baño y llamada ex no sean consecutivas
        for i in range(3):
            if (secuencia[i] in ["baño", "llamar ex"] and 
                secuencia[i+1] in ["baño", "llamar ex"]):
                break
        else:
            return secuencia

# Función para ejecutar acciones
def ejecutar_accion(accion, nombre):
    if accion == "tomar":
        tomar(nombre)
    elif accion == "baño":
        usar_baño(nombre)
    elif accion == "llamar ex":
        llamada_ex(nombre)
    elif accion == "cantar":
        cantando(nombre)

# Simulación principal
for ciclo in range(5):
    print(f"\n=== CICLO {ciclo + 1} ===")
    
    # Generar secuencia aleatoria única para este ciclo
    secuencia = generar_secuencia_valida()
    print(f"Secuencia: {' → '.join(secuencia)}")
    
    # Mezclar borrachitos para asignación aleatoria pero ordenada en ejecución
    borrachitos_mezclados = random.sample(borrachitos, len(borrachitos))
    
    # Asignar acciones exclusivas primero
    asignaciones = {}
    for accion in secuencia:
        if accion in ["baño", "llamar ex"]:
            # Encontrar próximo borrachito disponible
            for b in borrachitos_mezclados:
                if b not in asignaciones.values():
                    asignaciones[accion] = b
                    break
    
    # Asignar acciones no exclusivas
    for accion in secuencia:
        if accion not in asignaciones:
            for b in borrachitos_mezclados:
                if b not in asignaciones.values():
                    asignaciones[accion] = b
                    break
    
    # Ejecutar en orden de secuencia con borrachitos aleatorios
    for accion in secuencia:
        ejecutar_accion(accion, asignaciones[accion])
    
    # Participación completa - verificar que todos hicieron algo
    participantes = set(asignaciones.values())
    if len(participantes) < 5:
        # Asignar acciones adicionales a los que no participaron
        no_participantes = [b for b in borrachitos if b not in participantes]
        extra_acciones = ["tomar", "cantar"]
        for b in no_participantes:
            accion = random.choice(extra_acciones)
            print(f"{b} hace acción extra: {accion}")
            ejecutar_accion(accion, b)
    
    time.sleep(1.5)

print("\n¡Simulación completada con éxito!")
print("Todos los borrachitos participaron activamente en cada ciclo.")
print("Secuencias de acciones diferentes en cada ejecución.")