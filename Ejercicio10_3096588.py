print("\n**************************************************")
print("Ejercicio 10: Reto final, ¿soy viral?")
print("CALCULADORA DE ENGAGEMENT - Tienda de snacks")

# input() guarda el nombre de usuario como texto
usuario = input("\nTu usuario de Instagram: @")

# int() convierte el texto a un número entero
seguidores = int(input("¿Cuántos seguidores tienes? "))

likes = int(input("¿Cuántos likes tuvo tu última publicación? "))

comentarios = int(input("¿Cuántos comentarios tuvo? "))

# Sumamos todas las interacciones
interacciones = likes + comentarios

# Calculamos el porcentaje de engagement
engagement = (interacciones / seguidores) * 100

# Mostramos los resultados
print(f"\n******** RESULTADOS DE @{usuario} ********")

print(f"Interacciones totales: {interacciones}")

print(f"Engagement: {engagement:.2f}%")

print("\nDato: un engagement superior al 3% puede ser una buena señal, dependiendo de la cuenta y su audiencia.")

print("\n**************************************************")