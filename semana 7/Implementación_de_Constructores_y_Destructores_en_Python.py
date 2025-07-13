# Tarea: Implementación de Constructores y Destructores en Python
# Autor: [Tu Nombre]
# Fecha: [Fecha]

class Recurso:
    """
    Clase que demuestra el uso de constructor y destructor
    Simula la gestión de un recurso del sistema (archivo, conexión, etc.)
    """

    def __init__(self, nombre_recurso):
        """
        Constructor: Se ejecuta automáticamente al crear una instancia
        Inicializa los atributos del objeto y simula apertura del recurso
        """
        self.nombre = nombre_recurso
        self.estado = "Abierto"
        print(f"[CONSTRUCTOR] Recurso '{self.nombre}' creado y {self.estado}")

    def operacion(self):
        """Método que simula una operación con el recurso"""
        print(f"Realizando operación con '{self.nombre}'...")

    def __del__(self):
        """
        Destructor: Se ejecuta automáticamente cuando el objeto es eliminado
        Realiza tareas de limpieza y liberación de recursos
        """
        self.estado = "Cerrado"
        print(f"[DESTRUCTOR] Recurso '{self.nombre}' liberado. Estado: {self.estado}")


class Sistema:
    """Clase adicional que demuestra uso de constructor con más parámetros"""

    def __init__(self, id_sistema, capacidad):
        """
        Constructor con parámetros adicionales
        Inicializa múltiples atributos del objeto
        """
        self.id = id_sistema
        self.capacidad = capacidad
        self.recursos = []
        print(f"[CONSTRUCTOR] Sistema {self.id} creado (Capacidad: {self.capacidad})")

    def agregar_recurso(self, recurso):
        """Agrega un recurso al sistema"""
        self.recursos.append(recurso)
        print(f"Recurso '{recurso.nombre}' añadido al sistema {self.id}")

    def __del__(self):
        """Destructor para limpieza del sistema"""
        print(f"[DESTRUCTOR] Sistema {self.id} siendo eliminado...")


# Demostración de funcionamiento
if __name__ == "__main__":
    print("\n--- Creando recursos ---")
    # Creación de instancias (llama automáticamente a __init__)
    recurso1 = Recurso("Archivo_Principal")
    recurso2 = Recurso("Base_Datos")

    print("\n--- Realizando operaciones ---")
    recurso1.operacion()
    recurso2.operacion()

    print("\n--- Creando sistema y agregando recursos ---")
    sistema = Sistema("Sistema_01", "128MB")
    sistema.agregar_recurso(recurso1)
    sistema.agregar_recurso(recurso2)

    print("\n--- Finalizando programa ---")
    # Los destructores se llamarán automáticamente al finalizar
    # También se pueden llamar explícitamente con: del objeto