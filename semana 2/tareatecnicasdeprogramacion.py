# ABSTRACCIÓN: Clase base abstracta
class Personaje:
    def __init__(self, nombre, salud):
        self._nombre = nombre  # Encapsulación
        self._salud = salud

    # POLIMORFISMO: Método que será implementado de diferente forma
    def atacar(self):
        pass

    # Encapsulación con getter
    @property
    def salud(self):
        return self._salud

    # Encapsulación con setter
    @salud.setter
    def salud(self, valor):
        if valor >= 0:
            self._salud = valor
        else:
            self._salud = 0


# HERENCIA: Clases hijas
class Guerrero(Personaje):
    def atacar(self):  # Implementación específica
        return 20


class Mago(Personaje):
    def atacar(self):  # Implementación diferente
        return 15


# POLIMORFISMO: Función que usa diferentes personajes
def combate(jugador1, jugador2):
    # Turno 1
    danio = jugador1.atacar()
    jugador2.salud -= danio
    print(f"{jugador1._nombre} ataca! {jugador2._nombre} pierde {danio} HP")

    # Turno 2
    if jugador2.salud > 0:
        danio = jugador2.atacar()
        jugador1.salud -= danio
        print(f"{jugador2._nombre} contraataca! {jugador1._nombre} pierde {danio} HP")


# DEMOSTRACIÓN
if __name__ == "__main__":
    # Crear personajes
    conan = Guerrero("Conan", 100)
    gandalf = Mago("Gandalf", 80)

    # Iniciar combate
    print("=== COMBATE ÉPICO ===")
    print(f"INICIO: {conan._nombre} ({conan.salud} HP) vs {gandalf._nombre} ({gandalf.salud} HP)\n")

    # Ejecutar combate (polimorfismo)
    combate(conan, gandalf)

    # Resultado final
    print("\nRESULTADO FINAL:")
    print(f"{conan._nombre}: {conan.salud} HP")
    print(f"{gandalf._nombre}: {gandalf.salud} HP")
    print("\n¡Combate terminado!")