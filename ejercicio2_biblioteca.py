# ============================================================
# Ejercicio 2 - Sistema de Préstamos - Biblioteca Central
# FPY1101 - Evaluación Parcial 3
# ============================================================

# --- Inicialización de variables (IE 2.1.1) ---
CAPACIDAD_MAXIMA = 120
stock_disponible = 120
historial_prestamos = 0

# --- Bienvenida (IE 2.1.3) ---
print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central!")

# --- Ciclo principal del menú (IE 2.4.1, IE 2.4.2) ---
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Libros disponibles")
    print("2. Realizar préstamo")
    print("3. Devolver préstamo")
    print("4. Historial de préstamos")
    print("5. Salir")

    # Validación de opción del menú (IE 2.5.1)
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Opción inválida. Ingresa un número entre 1 y 5.")
        continue

    # --- Opción 1: Libros disponibles (IE 2.3.1, IE 2.3.2) ---
    if opcion == 1:
        print(f"Libros disponibles actualmente: {stock_disponible}")

    # --- Opción 2: Realizar préstamo (IE 2.3.2, IE 2.5.1) ---
    elif opcion == 2:
        while True:
            try:
                cantidad = int(input("¿Cuántos libros deseas prestar? "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif cantidad > stock_disponible:
                    print(f"No hay suficientes libros disponibles. Stock actual: {stock_disponible}")
                else:
                    stock_disponible -= cantidad       # IE 2.1.2
                    historial_prestamos += cantidad    # IE 2.1.2
                    print(f"Préstamo realizado: {cantidad} libro(s). Stock restante: {stock_disponible}")
                    break
            except ValueError:
                print("Ingresa un número entero válido.")

    # --- Opción 3: Devolver préstamo (IE 2.3.2, IE 2.5.1) ---
    elif opcion == 3:
        while True:
            try:
                cantidad = int(input("¿Cuántos libros deseas devolver? "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif stock_disponible + cantidad > CAPACIDAD_MAXIMA:
                    print(f"No puedes devolver esa cantidad. Supera la capacidad máxima ({CAPACIDAD_MAXIMA}).")
                else:
                    stock_disponible += cantidad       # IE 2.1.2
                    historial_prestamos -= cantidad    # IE 2.1.2
                    print(f"Devolución registrada: {cantidad} libro(s). Stock actual: {stock_disponible}")
                    break
            except ValueError:
                print("Ingresa un número entero válido.")

    # --- Opción 4: Historial (IE 2.3.1) ---
    elif opcion == 4:
        print(f"Total de préstamos activos durante esta sesión: {historial_prestamos}")

    # --- Opción 5: Salir (IE 2.3.2) ---
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        break

    # --- Opción inválida (IE 2.3.1) ---
    else:
        print("Opción inválida. Selecciona una opción entre 1 y 5.")
