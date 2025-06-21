# sistema_biblioteca.py
"""
Sistema de Gestión de Biblioteca
Modela libros, usuarios, préstamos y la interacción entre ellos
"""


class Libro:
    """Representa un libro en la biblioteca con atributos y comportamientos asociados"""

    def __init__(self, titulo: str, autor: str, isbn: str):
        # Encapsulación: Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True  # Estado inicial disponible

    def obtener_info(self) -> str:
        """Polimorfismo: Método que devuelve información del libro"""
        return f"'{self.__titulo}' por {self.__autor} (ISBN: {self.__isbn})"

    def esta_disponible(self) -> bool:
        """Getter para verificar disponibilidad"""
        return self.__disponible

    def cambiar_estado(self, nuevo_estado: bool):
        """Setter para modificar disponibilidad (encapsulamiento)"""
        self.__disponible = nuevo_estado


class Usuario:
    """Representa un usuario registrado en la biblioteca"""

    def __init__(self, id_usuario: int, nombre: str, email: str):
        # Composición: El usuario tiene libros prestados
        self.__id = id_usuario
        self.__nombre = nombre
        self.__email = email
        self.__libros_prestados = []  # Lista de libros actualmente prestados

    def tomar_prestado(self, libro: Libro):
        """Agrega un libro a la lista de préstamos si está disponible"""
        if libro.esta_disponible():
            libro.cambiar_estado(False)
            self.__libros_prestados.append(libro)
            return True
        return False

    def devolver(self, libro: Libro):
        """Remueve un libro de la lista de préstamos"""
        if libro in self.__libros_prestados:
            libro.cambiar_estado(True)
            self.__libros_prestados.remove(libro)
            return True
        return False

    def listar_prestados(self) -> list:
        """Muestra los libros actualmente prestados"""
        return [libro.obtener_info() for libro in self.__libros_prestados]


class Biblioteca:
    """Sistema principal que gestiona libros y usuarios"""

    def __init__(self):
        # Agregación: Biblioteca contiene libros y usuarios
        self.__catalogo = []
        self.__usuarios_registrados = {}

    def agregar_libro(self, libro: Libro):
        """Añade un libro al catálogo"""
        self.__catalogo.append(libro)
        print(f"Libro añadido: {libro.obtener_info()}")

    def registrar_usuario(self, usuario: Usuario):
        """Registra un nuevo usuario"""
        self.__usuarios_registrados[usuario._Usuario__id] = usuario
        print(f"Usuario registrado: {usuario._Usuario__nombre}")

    def buscar_libro(self, titulo: str) -> list:
        """Busca libros por título (demuestra polimorfismo)"""
        return [lib for lib in self.__catalogo if titulo.lower() in lib._Libro__titulo.lower()]


# --- Demostración del sistema ---
if __name__ == "__main__":
    # Creación de objetos
    biblioteca = Biblioteca()

    # Agregar libros al catálogo
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156013925")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario(1, "Ana Torres", "ana@example.com")
    biblioteca.registrar_usuario(usuario1)

    # Interacciones
    print("\n--- Préstamo de libros ---")
    if usuario1.tomar_prestado(libro1):
        print(f"{usuario1._Usuario__nombre} tomó prestado: {libro1._Libro__titulo}")

    print("\n--- Libros prestados actualmente ---")
    for libro in usuario1.listar_prestados():
        print(f"- {libro}")

    print("\n--- Devolución de libro ---")
    if usuario1.devolver(libro1):
        print(f"{usuario1._Usuario__nombre} devolvió: {libro1._Libro__titulo}")

    print("\n--- Búsqueda en catálogo ---")
    resultados = biblioteca.buscar_libro("principito")
    for libro in resultados:
        print(f"Resultado de búsqueda: {libro.obtener_info()}")