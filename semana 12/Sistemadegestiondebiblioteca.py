class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tuplas para almacenar autor y título (inmutables)
        self.datos = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.datos[1]}' por {self.datos[0]} - {self.categoria} ({self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para libros prestados al usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        # Diccionario para libros disponibles (ISBN como clave)
        self.libros_disponibles = {}
        # Conjunto para IDs de usuarios únicos
        self.usuarios_registrados = set()
        # Diccionario para objetos de usuario (ID como clave)
        self.usuarios = {}
        # Diccionario para registrar préstamos (ISBN: ID usuario)
        self.prestamos_activos = {}

    def añadir_libro(self, libro):
        """Añade un libro a la colección disponible"""
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        """Elimina un libro de la colección disponible"""
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro removido: {libro}")
        else:
            print("ISBN no encontrado en la colección")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en el sistema"""
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Error: ID de usuario ya existe")

    def dar_baja_usuario(self, id_usuario):
        """Elimina un usuario del sistema"""
        if id_usuario in self.usuarios_registrados:
            # Verificar que no tenga libros prestados
            if not self.usuarios[id_usuario].libros_prestados:
                self.usuarios_registrados.remove(id_usuario)
                del self.usuarios[id_usuario]
                print(f"Usuario {id_usuario} eliminado")
            else:
                print("Error: Usuario tiene libros prestados")
        else:
            print("Error: Usuario no registrado")

    def prestar_libro(self, isbn, id_usuario):
        """Gestiona el préstamo de un libro a un usuario"""
        if isbn not in self.libros_disponibles:
            print("Error: Libro no disponible")
            return

        if id_usuario not in self.usuarios_registrados:
            print("Error: Usuario no registrado")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios[id_usuario]

        # Registrar préstamo
        usuario.libros_prestados.append(libro)
        self.prestamos_activos[isbn] = id_usuario
        del self.libros_disponibles[isbn]

        print(f"Libro prestado: {libro} a {usuario}")

    def devolver_libro(self, isbn):
        """Gestiona la devolución de un libro"""
        if isbn not in self.prestamos_activos:
            print("Error: Este libro no está prestado")
            return

        id_usuario = self.prestamos_activos[isbn]
        usuario = self.usuarios[id_usuario]
        libro = next(lib for lib in usuario.libros_prestados if lib.isbn == isbn)

        # Remover de préstamos activos
        usuario.libros_prestados.remove(libro)
        self.libros_disponibles[isbn] = libro
        del self.prestamos_activos[isbn]

        print(f"Libro devuelto: {libro} por {usuario}")

    def buscar_libros(self, criterio, valor):
        """Busca libros por título, autor o categoría"""
        resultados = []
        # Buscar en libros disponibles
        for libro in self.libros_disponibles.values():
            if (criterio == 'titulo' and valor.lower() in libro.datos[1].lower() or
                    criterio == 'autor' and valor.lower() in libro.datos[0].lower() or
                    criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)

        # Buscar en libros prestados
        for isbn, id_usuario in self.prestamos_activos.items():
            libro = self.usuarios[id_usuario].libros_prestados[
                next(i for i, lib in enumerate(self.usuarios[id_usuario].libros_prestados)
                     if lib.isbn == isbn)
            ]
            if (criterio == 'titulo' and valor.lower() in libro.datos[1].lower() or
                    criterio == 'autor' and valor.lower() in libro.datos[0].lower() or
                    criterio == 'categoria' and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)

        return resultados

    def listar_libros_prestados(self, id_usuario):
        """Lista todos los libros prestados a un usuario específico"""
        if id_usuario not in self.usuarios:
            print("Error: Usuario no registrado")
            return []
        return self.usuarios[id_usuario].libros_prestados


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Crear biblioteca
    bib = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "1234567890")
    libro2 = Libro("1984", "George Orwell", "Ciencia ficción", "0987654321")
    bib.añadir_libro(libro1)
    bib.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Juan Pérez", "001")
    usuario2 = Usuario("María García", "002")
    bib.registrar_usuario(usuario1)
    bib.registrar_usuario(usuario2)

    # Prestar libros
    bib.prestar_libro("1234567890", "001")
    bib.prestar_libro("0987654321", "002")

    # Buscar libros
    resultados = bib.buscar_libros("autor", "orwell")
    for libro in resultados:
        print(f"Resultado búsqueda: {libro}")

    # Listar libros prestados
    prestados = bib.listar_libros_prestados("001")
    for libro in prestados:
        print(f"Libro prestado a usuario 001: {libro}")

    # Devolver libro
    bib.devolver_libro("1234567890")

    # Dar de baja usuario
    bib.dar_baja_usuario("001")