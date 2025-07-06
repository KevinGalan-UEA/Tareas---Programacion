"""
Tarea: Aplicación de Conceptos de POO en Python
Autor: Kevin Galan
Fecha: 06/07/2025
Descripción: Programa que demuestra herencia, encapsulación y polimorfismo
"""


class Vehiculo:
    """Clase base que representa un vehículo genérico"""

    def __init__(self, marca: str, modelo: str):
        # Encapsulación: atributos protegidos (convención con _)
        self._marca = marca
        self._modelo = modelo
        self._estado = 'apagado'  # Estado interno encapsulado

    def arrancar(self):
        """Método para cambiar el estado del vehículo"""
        if self._estado == 'apagado':
            self._estado = 'encendido'
            return f"{self._marca} {self._modelo}: Motor encendido"
        return f"{self._marca} {self._modelo}: Ya estaba encendido"

    # Getter para estado (encapsulación)
    @property
    def estado(self):
        return self._estado

    # Método que será sobrescrito (polimorfismo)
    def tipo_vehiculo(self):
        return "Vehículo genérico"


class Coche(Vehiculo):
    """Clase derivada que hereda de Vehiculo (Herencia)"""

    def __init__(self, marca: str, modelo: str, num_puertas: int):
        super().__init__(marca, modelo)
        # Encapsulación: atributo privado (doble __)
        self.__num_puertas = num_puertas

    # Método específico de la clase derivada
    def abrir_puertas(self):
        return f"Abriendo {self.__num_puertas} puertas"

    # Polimorfismo: sobrescritura de método
    def tipo_vehiculo(self):
        return "Coche"


class Motocicleta(Vehiculo):
    """Otra clase derivada de Vehiculo"""

    def __init__(self, marca: str, modelo: str, tipo_manubrio: str):
        super().__init__(marca, modelo)
        self.__tipo_manubrio = tipo_manubrio  # Atributo privado

    # Polimorfismo: método específico
    def hacer_caballito(self):
        return "¡Haciendo caballito!"

    # Polimorfismo: sobrescritura de método
    def tipo_vehiculo(self):
        return "Motocicleta"


# Función que demuestra polimorfismo
def mostrar_tipo(vehiculos: list):
    """Recibe diferentes tipos de vehículos (polimorfismo)"""
    for v in vehiculos:
        print(v.tipo_vehiculo())


if __name__ == "__main__":
    # Creación de objetos (instancias)
    mi_coche = Coche("Toyota", "Corolla", 4)
    mi_moto = Motocicleta("Honda", "CBR600", "deportivo")

    # Demostración de funcionalidad
    print("\n--- Encapsulación ---")
    print(mi_coche.arrancar())
    print(mi_coche.arrancar())  # Estado interno protegido
    print("Estado:", mi_coche.estado)  # Acceso mediante propiedad

    print("\n--- Herencia y métodos específicos ---")
    print(mi_moto.arrancar())
    print(mi_coche.abrir_puertas())
    print(mi_moto.hacer_caballito())

    print("\n--- Polimorfismo ---")
    vehiculos = [mi_coche, mi_moto, Vehiculo("MarcaGen", "ModeloGen")]
    mostrar_tipo(vehiculos)  # Mismo método, comportamientos diferentes

    # Acceso a atributo encapsulado (genera error)
    # print(mi_coche.__num_puertas)  # AttributeError