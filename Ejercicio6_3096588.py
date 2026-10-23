print("\n======================================================")
print("Ejercicio 6: Vidas y daño")
print("======================= BATALLA ======================")

# Damos de alta la variable personaje y vida
personaje = "Sylvia"
vida = 100

print(f"\nMi personaje se llama {personaje} y empieza con {100} de vida")

# Como vida vale 100, esta fórmula dice: vida = 100 - 25
vida = vida - 25
print(f"Me dio un golpe de un goblin, ahora tengo vida: {75}")

# Ahora vida vale 75, esta fórmula dice: vida = 75 - 40
vida = vida - 40
print(f"Ah, ahora me toco el golpe de un ogro, tengo de vida: {35}")

# Ahora vida vale 35, esta fórmula dice: vida = 35 - 15
vida = vida - 15
print(f"Me toco una flecha enemiga!, tengo de vida: {20}")

# Ahora vida vale 20, esta fórmula dice: vida = 20 + 30
vida = vida + 30
print(f"Tomó una poción... mi vida: {50}")

print(f"\n{personaje} terminó la batalla con {50} HP\n")
print("======================================================")