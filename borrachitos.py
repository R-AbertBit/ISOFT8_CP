import time

nombres = ["Angel", "Brayan", "Ramiro", "Jaracuaro", "Zuñiga"]

# Acciones por ciclo, cada lista es un ciclo
# Cada acción puede ser: 
# - "A drinking"
# - "Cantando la troka"
# - "llama_ex"
# - "baño"
acciones_ciclos = [
    ["A drinking"] * 5,
    ["llama_ex", "A drinking", "baño", "Cantando la troka", "Cantando la troka"],
    ["Cantando la troka", "llama_ex", "A drinking", "baño", "Cantando la troka"],
    ["Cantando la troka", "Cantando la troka", "llama_ex", "A drinking", "baño"],
    ["baño", "Cantando la troka", "Cantando la troka", "llama_ex", "A drinking"],
    ["A drinking", "baño", "Cantando la troka", "Cantando la troka", "llama_ex"],
]

# Estados por persona
estado_usuarios = {
    nombre: {
        "accion": None,
        "espera_llorar": False,
        "espera_salir_baño": False,
        "quien_llora": None
    }
    for nombre in nombres
}

# Cola de llorones para que el que sale del baño sepa a quién decirle que pistie
cola_llorones = []

def ejecutar_ciclo(num_ciclo, acciones):
    print(f"\nCiclo {num_ciclo}")
    ocupados = {
        "llama_ex": False,
        "llora": False,
        "baño": False,
        "sale_baño": False
    }

    # Primera pasada: acciones principales
    for i, accion in enumerate(acciones):
        nombre = nombres[i]
        estado = estado_usuarios[nombre]

        if accion == "llama_ex" and not ocupados["llama_ex"]:
            print(f'{nombre} "Llama a la ex para suplicarle que regresen"')
            time.sleep(0.8)
            estado["espera_llorar"] = True
            ocupados["llama_ex"] = True

        elif accion == "baño" and not ocupados["baño"]:
            print(f'{nombre} "Entra al baño"')
            time.sleep(0.8)
            estado["espera_salir_baño"] = True
            ocupados["baño"] = True

        elif accion == "A drinking" or accion == "Cantando la troka":
            print(f'{nombre} "{accion}"')
            time.sleep(1.3)

    # Segunda pasada: llorar
    for nombre in nombres:
        estado = estado_usuarios[nombre]
        if estado["espera_llorar"] and not ocupados["llora"]:
            print(f'{nombre} "Llora porque le colgó la ex"')
            time.sleep(0.8)
            estado["espera_llorar"] = False
            cola_llorones.append(nombre)
            ocupados["llora"] = True

    # Tercera pasada: salir del baño
    for nombre in nombres:
        estado = estado_usuarios[nombre]
        if estado["espera_salir_baño"] and not ocupados["sale_baño"]:
            if cola_llorones:
                quien_chilla = cola_llorones.pop(0)
            else:
                quien_chilla = "el compa"
            print(f'{nombre} "Sale del baño y le dice a {quien_chilla} que ya no chille y que ¡Pistie!"')
            time.sleep(0.8)
            estado["espera_salir_baño"] = False
            ocupados["sale_baño"] = True

# Ejecutar todos los ciclos
for i, acciones in enumerate(acciones_ciclos):
    ejecutar_ciclo(i + 1, acciones)