class Persona:
    def __init__(self, nombre, apellido, documento, anio_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.anio_nacimiento = anio_nacimiento

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Documento:", self.documento)
        print("Año de nacimiento:", self.anio_nacimiento)
        print("-" * 30)

def main():
    persona1 = Persona("Carlos", "Gómez", "1037654321", 1995)
    persona2 = Persona("María", "Restrepo", "43215678", 2001)
    persona1.mostrar_datos()
    persona2.mostrar_datos()

if __name__ == "__main__":
    main()
