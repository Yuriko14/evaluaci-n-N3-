# ============================================================
# Ejercicio 1 - Sistema de Registro de Médicos
# Hospital Central Metropolitano
# FPY1101 - Evaluación Parcial 3
# ============================================================

# --- Inicialización de contadores (IE 2.1.1) ---
especialistas_senior = 0
residentes_junior = 0

# --- Solicitar cantidad de médicos con validación (IE 2.5.1, IE 2.4.1) ---
while True:
    try:
        cantidad_medicos = int(input("¿Cuántos médicos desea registrar? "))
        if cantidad_medicos <= 0:
            raise ValueError
        break
    except ValueError:
        print("¡Registro médico inválido! Ingresa un entero positivo para continuar.")

# --- Registro de cada médico (IE 2.4.2) ---
for i in range(1, cantidad_medicos + 1):
    print(f"\n--- Registro del médico N°{i} ---")

    # Validación del nombre profesional (IE 2.2.2, IE 2.3.1)
    while True:
        nombre = input("Ingresa el nombre profesional del médico: ")
        if len(nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")

    # Validación de experiencia clínica (IE 2.5.1, IE 2.4.1)
    while True:
        try:
            experiencia = int(input("Ingresa los años de experiencia clínica: "))
            if experiencia <= 0:
                raise ValueError
            break
        except ValueError:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")

    # Clasificación del médico (IE 2.3.2)
    if experiencia > 5:
        tipo = "Especialista Senior"
        especialistas_senior += 1   # IE 2.1.2
    else:
        tipo = "Residente Junior"
        residentes_junior += 1      # IE 2.1.2

    print(f"Médico '{nombre}' clasificado como: {tipo}")

# --- Salida final (IE 2.1.3) ---
print(f"\n¡El hospital cuenta con {especialistas_senior} Especialistas Senior y "
      f"{residentes_junior} Residentes Junior! ¡Sistema listo para operar!")
