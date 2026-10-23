print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Ejercicio 9: Tienda de snacks")
print("Galletas Gourmet")
# input() le pregunta al usuario y guarda lo que escribe en la variable
# input() SIEMPRE guarda TEXTO, aunque escribas un número
galleta = input("\n¿Te gustan las galletas artesanales")
#Si el usuario escribe galleta, ahora snack vale "galleta"

#float() convierte el texto a número con decimales para poder hacer cuentas
precio_galleta = float(input(f"¿Cuánto cuesta el/la {galleta}? 250 $"))
#Si el usuario escribe 200, ahora precio_galleta vale 200
precio_snack = float(input("¿Cuánto cuestan un mes de galletas? 6000 $"))
#Si el usuario escribe 350, ahora precio_croquetas vale 350.0
#int() convierte el texto en un número entero, porque los meses no llevan decimales
meses = int(input("¿Para cuántos meses quieres galletas? 3 meses"))
#Si el usuario escribe 3, ahora meses vale 3

#Calculamos cuánto gasto en galletas, esta formula dice: cost_galletas = 350.0 * 3
costo_galletas = precio_snack * meses
#Ahora costo_croquetas vale 1050.0

#Calculamos el total, esta formula dice: total = 1500.0 + 1050.0
total = precio_snack + costo_galletas
#Ahora total vale 2550.0

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("TICKET DE COMPRA")
#El :.2f muestra 2 decimales, como se ve el dinero
print(f"Snack: {galleta} ${precio_snack:.2f}")
print(f"Galletas por {meses} meses: ${costo_galletas:.2f}")
print(f"\nTOTAL A PAGAR: ${total:.2f}")

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")