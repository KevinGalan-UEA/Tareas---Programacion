"""
Programa: Calculadora de Figuras Geométricas y Conversor de Temperatura
Descripción:
  Este programa permite calcular el área de figuras geométricas (círculo, triángulo, cuadrado)
  y convertir temperaturas entre Celsius y Fahrenheit. Incluye menú interactivo y validación básica.
Autor: Kevin Galan
Fecha: 27/06/2025
"""

import math

# Constantes (SCREAMING_SNAKE_CASE)
PI = math.pi
FACTOR_CELSIUS_A_FAHRENHEIT = 9 / 5
AJUSTE_FAHRENHEIT = 32
FACTOR_FAHRENHEIT_A_CELSIUS = 5 / 9


def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio.

    Args:
        radio (float): Radio del círculo

    Returns:
        float: Área calculada
    """
    return PI * radio ** 2


def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo usando base y altura.

    Args:
        base (float): Base del triángulo
        altura (float): Altura del triángulo

    Returns:
        float: Área calculada
    """
    return (base * altura) / 2


def calcular_area_cuadrado(lado: float) -> float:
    """Calcula el área de un cuadrado dado un lado.

    Args:
        lado (float): Longitud del lado

    Returns:
        float: Área calculada
    """
    return lado ** 2


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte temperatura de Celsius a Fahrenheit.

    Args:
        celsius (float): Temperatura en Celsius

    Returns:
        float: Temperatura en Fahrenheit
    """
    return (celsius * FACTOR_CELSIUS_A_FAHRENHEIT) + AJUSTE_FAHRENHEIT


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Convierte temperatura de Fahrenheit a Celsius.

    Args:
        fahrenheit (float): Temperatura en Fahrenheit

    Returns:
        float: Temperatura en Celsius
    """
    return (fahrenheit - AJUSTE_FAHRENHEIT) * FACTOR_FAHRENHEIT_A_CELSIUS


def mostrar_menu_principal() -> str:
    """Muestra el menú principal y obtiene la selección del usuario.

    Returns:
        str: Opción seleccionada
    """
    print("\n" + "=" * 50)
    print("CALCULADORA GEOMÉTRICA Y CONVERSOR DE TEMPERATURA")
    print("=" * 50)
    print("1. Calcular áreas de figuras geométricas")
    print("2. Convertir temperaturas")
    print("3. Salir")

    return input("Seleccione una opción (1-3): ")


def mostrar_menu_figuras() -> str:
    """Muestra el menú de figuras y obtiene la selección del usuario.

    Returns:
        str: Opción seleccionada
    """
    print("\nFIGURAS GEOMÉTRICAS DISPONIBLES:")
    print("a. Círculo")
    print("b. Triángulo")
    print("c. Cuadrado")
    print("d. Volver al menú principal")

    return input("Seleccione una figura (a-d): ").lower()


def mostrar_menu_temperaturas() -> str:
    """Muestra el menú de temperaturas y obtiene la selección del usuario.

    Returns:
        str: Opción seleccionada
    """
    print("\nCONVERSIÓN DE TEMPERATURAS:")
    print("a. Celsius a Fahrenheit")
    print("b. Fahrenheit a Celsius")
    print("c. Volver al menú principal")

    return input("Seleccione una opción (a-c): ").lower()


def main():
    """Función principal que controla el flujo del programa."""
    programa_activo = True  # Tipo booleano para controlar el estado del programa

    while programa_activo:
        opcion = mostrar_menu_principal()

        # Opción 1: Cálculo de áreas
        if opcion == "1":
            while True:
                figura = mostrar_menu_figuras()

                if figura == "a":  # Círculo
                    try:
                        radio = float(input("\nIngrese el radio del círculo: "))
                        if radio <= 0:
                            print("Error: El radio debe ser positivo")
                            continue
                        area = calcular_area_circulo(radio)
                        print(f"Área del círculo: {area:.2f}")
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                elif figura == "b":  # Triángulo
                    try:
                        base = float(input("\nIngrese la base del triángulo: "))
                        altura = float(input("Ingrese la altura del triángulo: "))
                        if base <= 0 or altura <= 0:
                            print("Error: Valores deben ser positivos")
                            continue
                        area = calcular_area_triangulo(base, altura)
                        print(f"Área del triángulo: {area:.2f}")
                    except ValueError:
                        print("Error: Debe ingresar números válidos")

                elif figura == "c":  # Cuadrado
                    try:
                        lado = float(input("\nIngrese el lado del cuadrado: "))
                        if lado <= 0:
                            print("Error: El lado debe ser positivo")
                            continue
                        area = calcular_area_cuadrado(lado)
                        print(f"Área del cuadrado: {area:.2f}")
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                elif figura == "d":  # Volver
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")

        # Opción 2: Conversión de temperaturas
        elif opcion == "2":
            while True:
                conversion = mostrar_menu_temperaturas()

                if conversion == "a":  # Celsius a Fahrenheit
                    try:
                        celsius = float(input("\nIngrese temperatura en Celsius: "))
                        fahrenheit = celsius_a_fahrenheit(celsius)
                        print(f"{celsius}°C = {fahrenheit:.2f}°F")
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                elif conversion == "b":  # Fahrenheit a Celsius
                    try:
                        fahrenheit = float(input("\nIngrese temperatura en Fahrenheit: "))
                        celsius = fahrenheit_a_celsius(fahrenheit)
                        print(f"{fahrenheit}°F = {celsius:.2f}°C")
                    except ValueError:
                        print("Error: Debe ingresar un número válido")

                elif conversion == "c":  # Volver
                    break

                else:
                    print("Opción inválida. Intente nuevamente.")

        # Opción 3: Salir
        elif opcion == "3":
            programa_activo = False
            print("\n¡Gracias por usar el programa! Hasta luego.")

        else:
            print("\nOpción inválida. Por favor seleccione 1, 2 o 3.")


if __name__ == "__main__":
    main()