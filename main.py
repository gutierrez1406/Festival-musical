
# main.py
# Programa: Festival 

# Clase base
class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, interpreto {self.genero} y mi popularidad es de {self.popularidad}/100.")

    def actuar(self):
        print("El artista está realizando su presentación...")

    def despedirse(self):
        print(f"{self.nombre}: ¡Gracias a todos! ¡Fue un placer presentarme aquí!")


# Subclase Cantante
class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")


# Subclase DJ
class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


# Subclase Banda
class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


# Función principal del festival
def iniciar_festival(lista_artistas):
    print("\n¡Comienza el Festival Musical!\n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación\n")


# Programa principal
if __name__ == "__main__":
    lista_artistas = []

    n = int(input("¿Cuántos artistas se presentarán en el festival? "))

    for i in range(n):
        print(f"\n--- Artista #{i+1} ---")
        tipo = input("Tipo de artista (Cantante / DJ / Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1-100): "))

        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)

        elif tipo == "dj":
            estilo = input("Estilo de mezcla: ")
            artista = DJ(nombre, genero, popularidad, estilo)

        elif tipo == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)

        else:
            print("Tipo no reconocido. Se omitirá este artista.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)
