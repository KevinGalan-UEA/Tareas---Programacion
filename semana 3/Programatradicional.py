# PROGRAMA TRADICIONAL (FUNCIONES)
def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas de 7 días (lunes a domingo)
    Retorna una lista con las temperaturas ingresadas
    """
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    temperaturas = []

    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("¡Error! Debe ingresar un valor numérico.")

    return temperaturas


def calcular_promedio(temps):
    """
    Calcula el promedio de una lista de temperaturas
    Retorna el valor del promedio redondeado a 2 decimales
    """
    return round(sum(temps) / len(temps), 2) if temps else 0


def main():
    """
    Función principal que coordina la entrada de datos y el cálculo
    Muestra los resultados al usuario
    """
    print("\n" + "=" * 50)
    print("PROGRAMA TRADICIONAL: PROMEDIO SEMANAL DE TEMPERATURAS")
    print("=" * 50)

    # Obtener datos
    temperaturas_semana = ingresar_temperaturas()

    # Calcular resultado
    promedio = calcular_promedio(temperaturas_semana)

    # Mostrar resultados
    print("\n" + "-" * 50)
    print(f"RESULTADO: El promedio semanal es {promedio}°C")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()