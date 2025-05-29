import time
import random

nombres = ["Angel", "Brayan", "Ramiro", "Jaracuaro", "Zuñiga"]
acciones_libres = ["A drinking", "Cantando la troka"]
acciones_exclusivas = [
    "Llama a la ex para suplicarle que regresen",
    "Llora porque le colgó la ex",
    "Entra al baño",
    "Sale del baño y le dice a {name} que ya no chille y que ¡Pistie!"
]

# Cada borracho tendrá una cola de acciones
colas_acciones = {
    1: [
        ["A drinking"] * 5,
        [
            "Llama a la ex para suplicarle que regresen",
            "A drinking",
            "Entra al baño",
            "Cantando la troka",
            "Cantando la troka",
            "Llora porque le colgó la ex",
            "Sale del baño y le dice a Angel que ya no chille y que ¡Pistie!"
        ],
        [
            "Cantando la troka",
            "Llama a la ex para suplicarle que regresen",
            "A drinking",
            "Entra al baño",
            "Cantando la troka",
            "Llora porque le colgó la ex",
            "Sale del baño y le dice a Brayan que ya no chille y que ¡Pistie!"
        ],
        [
            "Cantando la troka",
            "Cantando la troka",
            "Llama a la ex para suplicarle que regresen",
            "A drinking",
            "Entra al baño",
            "Llora porque le colgó la ex",
            "Sale del baño y le dice a Ramiro que ya no chille y que ¡Pistie!"
        ],
        [
            "Entra al baño",
            "Cantando la troka",
            "Cantando la troka",
            "Llama a la ex para suplicarle que regresen",
            "A drinking",
            "Llora porque le colgó la ex",
            "Sale del baño y le dice a Jaracuaro que ya no chille y que ¡Pistie!"
        ],
        [
            "A drinking",
            "Entra al baño",
            "Cantando la troka",
            "Cantando la troka",
            "Llama a la ex para suplicarle que regresen",
            "Llora porque le colgó la ex",
            "Sale del baño y le dice a Zuñiga que ya no chille y que ¡Pistie!"
        ]
    ]
}

# Reorganizamos las acciones para acceder por ciclo
ciclos = [
    ["A drinking"] * 5,
    [
        "Llama a la ex para suplicarle que regresen",
        "A drinking",
        "Entra al baño",
        "Cantando la troka",
        "Cantando la troka",
        "Llora porque le colgó la ex",
        "Sale del baño y le dice a Angel que ya no chille y que ¡Pistie!"
    ],
    [
        "Cantando la troka",
        "Llama a la ex para suplicarle que regresen",
        "A drinking",
        "Entra al baño",
        "Cantando la troka",
        "Llora porque le colgó la ex",
        "Sale del baño y le dice a Brayan que ya no chille y que ¡Pistie!"
    ],
    [
        "Cantando la troka",
        "Cantando la troka",
        "Llama a la ex para suplicarle que regresen",
        "A drinking",
        "Entra al baño",
        "Llora porque le colgó la ex",
        "Sale del baño y le dice a Ramiro que ya no chille y que ¡Pistie!"
    ],
    [
        "Entra al baño",
        "Cantando la troka",
        "Cantando la troka",
        "Llama a la ex para suplicarle que regresen",
        "A drinking",
        "Llora porque le colgó la ex",
        "Sale del baño y le dice a Jaracuaro que ya no chille y que ¡Pistie!"
    ],
    [
        "A drinking",
        "Entra al baño",
        "Cantando la troka",
        "Cantando la troka",
        "Llama a la ex para suplicarle que regresen",
        "Llora porque le colgó la ex",
        "Sale del baño y le dice a Zuñiga que ya no chille y que ¡Pistie!"
    ]
]

# Función que reparte acciones por ciclo
def ejecutar_ciclo(num_ciclo, acciones):
    print(f"\nCiclo {num_ciclo}")
    exclusivas_ocupadas = False
    exclusivas_en_uso = set()

    index = 0
    cola_pendiente = []

    while index < len(acciones):
        accion = acciones[index]
        nombre_index = index if index < 5 else index - (len(acciones) - 5)
        nombre = nombres[nombre_index % len(nombres)]

        # Si la acción es exclusiva, verificamos si hay otra ejecutándose
        if any(ex in accion for ex in acciones_exclusivas):
            if not exclusivas_ocupadas:
                print(f'{nombre} "{accion}"')
                exclusivas_ocupadas = True
                exclusivas_en_uso.add(accion)
                time.sleep(1)
                exclusivas_ocupadas = False
            else:
                # Se espera a que termine otra exclusiva
                cola_pendiente.append((index, accion, nombre))
        else:
            print(f'{nombre} "{accion}"')
            time.sleep(0.5)
        index += 1

    # Procesamos las pendientes exclusivas
    for item in cola_pendiente:
        _, accion, nombre = item
        print(f'{nombre} "{accion}"')
        time.sleep(1)

# Ejecutamos los ciclos
for i, ciclo in enumerate(ciclos):
    ejecutar_ciclo(i + 1, ciclo)