# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
class DiaClima:
    """Representa la información climática de un día específico"""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.temperatura = None

    def establecer_temperatura(self, valor: float):
        """Establece la temperatura del día (encapsulamiento)"""
        self.temperatura = valor


class SemanaClima:
    """Gestiona y calcula el promedio de temperaturas para una semana completa"""

    def __init__(self):
        self.dias = [
            DiaClima("lunes"),
            DiaClima("martes"),
            DiaClima("miércoles"),
            DiaClima("jueves"),
            DiaClima("viernes"),
            DiaClima("sábado"),
            DiaClima("domingo")
        ]

    def ingresar_temperaturas(self):
        """Solicita y almacena las temperaturas para cada día"""
        for dia in self.dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia.nombre}: "))
                    dia.establecer_temperatura(temp)
                    break
                except ValueError:
                    print("¡Error! Debe ingresar un valor numérico.")

    def calcular_promedio(self):
        """Calcula el promedio semanal con 2 decimales"""
        total = sum(dia.temperatura for dia in self.dias if dia.temperatura is not None)
        return round(total / len(self.dias), 2)

    def mostrar_resultado(self):
        """Muestra el resultado formateado"""
        promedio = self.calcular_promedio()
        print("\n" + "-" * 50)
        print(f"RESULTADO: El promedio semanal es {promedio}°C")
        print("-" * 50 + "\n")


def main():
    print("\n" + "=" * 50)
    print("PROGRAMA ORIENTADO A OBJETOS: PROMEDIO SEMANAL DE TEMPERATURAS")
    print("=" * 50)

    semana = SemanaClima()
    semana.ingresar_temperaturas()
    semana.mostrar_resultado()


if __name__ == "__main__":
    main()