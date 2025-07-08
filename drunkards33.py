import time
import random

# Define the 4 system resources
def order_beer(name):
    print(f"{name} is ordering beer...")
    time.sleep(random.uniform(0.2, 0.6))
    print(f"{name} finished ordering beer.")

def jukebox(name):
    print(f"{name} is using the jukebox...")
    time.sleep(random.uniform(0.2, 0.6))
    print(f"{name} is done with the jukebox.")

def sing(name):
    print(f"{name} is singing 🎤.")
    time.sleep(random.uniform(0.2, 0.5))

def dance(name):
    print(f"{name} is dancing 💃🕺.")
    time.sleep(random.uniform(0.2, 0.5))

# Each cycle, only 1 person from the corresponding core can use order_beer and jukebox
# Core1 (drunk guys) uses those resources in odd cycles, Core2 (drunk girls) in even cycles

# Simulate 6 processes for each core
drunk_guys = [f"DrunkGuy{i+1}" for i in range(6)]
drunk_girls = [f"DrunkGirl{i+1}" for i in range(6)]

# Simulate 5 cycles
for cycle in range(1, 6):
    print(f"\n--- Cycle {cycle} ---")

    if cycle % 2 == 1:
        # Odd cycles: Core1 has exclusive access to resources
        current_core = drunk_guys
        other_core = drunk_girls
    else:
        # Even cycles: Core2 has exclusive access to resources
        current_core = drunk_girls
        other_core = drunk_guys

    # Randomly choose 1 process from the current core to use order_beer and jukebox
    selected = random.choice(current_core)

    # Exclusive access to order_beer and jukebox for one process from the corresponding core
    order_beer(selected)
    jukebox(selected)

    # All drunk guys and girls can sing and dance simultaneously
    for person in drunk_guys + drunk_girls:
        sing(person)
    for person in drunk_guys + drunk_girls:
        dance(person)

    time.sleep(1)  # Short pause between cycles
