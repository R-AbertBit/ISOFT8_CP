import time
#Aqui esta mi participación -commit-
nombres = ["Angel", "Brayan", "Ramiro", "Jaracuaro", "Zuñiga"]
bartender = "Bartender"

# Acciones por ciclo, cada lista es un ciclo
# Cada acción puede ser: 
# - "Sirviendo Cerveza" (antes "A drinking")
# - "Cantando la troka"
# - "llama_ex"
# - "baño"
acciones_ciclos = [
    ["Sirviendo Cerveza"] * 5,
    ["llama_ex", "Sirviendo Cerveza", "baño", "Cantando la troka", "Cantando la troka"],
    ["Cantando la troka", "llama_ex", "Sirviendo Cerveza", "baño", "Cantando la troka"],
    ["Cantando la troka", "Cantando la troka", "llama_ex", "Sirviendo Cerveza", "baño"],
    ["baño", "Cantando la troka", "Cantando la troka", "llama_ex", "Sirviendo Cerveza"],
    ["Sirviendo Cerveza", "baño", "Cantando la troka", "Cantando la troka", "llama_ex"],
]

# Estados por persona
estado_usuarios = {
    nombre: {
        "accion": None,
        "espera_llorar": False,
        "espera_salir_baño": False,
        "quien_llora": None,
        "cervezas_tomadas": 0,
        "puede_usar_baño": False
    }
    for nombre in nombres
}

# Estado del bartender
estado_bartender = {
    "cervezas_servidas": {nombre: 0 for nombre in nombres},
    "baño_libre": True
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

        elif accion == "baño" and not ocupados["baño"] and estado["puede_usar_baño"]:
            if estado_bartender["baño_libre"]:
                print(f'{nombre} "Entra al baño"')
                time.sleep(0.8)
                estado["espera_salir_baño"] = True
                ocupados["baño"] = True
                estado_bartender["baño_libre"] = False
            else:
                print(f'{nombre} "Intenta entrar al baño pero está ocupado"')
                time.sleep(0.8)

        elif accion == "Sirviendo Cerveza":
            print(f'{bartender} "Sirve cerveza a {nombre}"')
            estado_bartender["cervezas_servidas"][nombre] += 1
            estado["cervezas_tomadas"] += 1
            estado["puede_usar_baño"] = estado["cervezas_tomadas"] >= 1
            time.sleep(0.8)

        elif accion == "Cantando la troka":
            print(f'{nombre} "Cantando la troka"')
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
            print(f'{bartender} "Baño Libre"')
            time.sleep(0.8)
            estado["espera_salir_baño"] = False
            estado_bartender["baño_libre"] = True
            ocupados["sale_baño"] = True

    # Mostrar contador de cervezas (opcional)
    print("\nResumen de cervezas servidas:")
    for nombre, count in estado_bartender["cervezas_servidas"].items():
        print(f"{nombre}: {count} cervezas")

# Ejecutar todos los ciclos
for i, acciones in enumerate(acciones_ciclos):
    ejecutar_ciclo(i + 1, acciones)