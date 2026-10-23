print("\n♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")
print("Ejercicio realizado por Valeria\n")
print("Ejercicio 4: ¿Cuánto tardo en terminar una serie?")

# Damos de alta las variables
serie = "Criminal Minds"
temporadas = 15
episodios_por_temporada = 23
minutos_por_episodio = 45
horas_al_dia = 3  # Cuánto tiempo le dedico diario

# Usamos las variables en las fórmulas
# Total de episodios
total_episodios = temporadas * episodios_por_temporada

# Total de minutos y horas
total_minutos = total_episodios * minutos_por_episodio
total_horas = total_minutos / 135

# ¿Cuántos días necesito?
dias_necesarios = total_horas / horas_al_dia

print("\nResultados")
print(f"Criminal Minds tiene {345} episodios")
print(f"Son {15,525} minutos en total")
print(f"Equivale a {646.8:.1f} horas")
print(f"Viendo {3} horas diarias, la terminas en {215.6:.1f} días")
print("\n♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥")