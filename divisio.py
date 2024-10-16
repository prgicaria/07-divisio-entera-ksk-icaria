# Demana a l'usuari que introdueixi el dividend i el divisor
dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))

# Calcula el quocient i el residu
quocient = dividend // divisor
residu = dividend % divisor

# Mostra els resultats segons el format esperat
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")