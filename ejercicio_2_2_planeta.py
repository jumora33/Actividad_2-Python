from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    UA = 149.59787

    def __init__(self, nombre=None, satelites=0, masa=0.0, volumen=0.0,
                 diametro=0, distancia_sol=0, tipo=None, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa                    # en kg
        self.volumen = volumen              # en km³
        self.diametro = diametro            # en km
        self.distancia_sol = distancia_sol  # en millones de km
        self.tipo = tipo
        self.observable = observable

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Satélites:", self.satelites)
        print("Masa:", self.masa, "kg")
        print("Volumen:", self.volumen, "km³")
        print("Diámetro:", self.diametro, "km")
        print("Distancia media al Sol:", self.distancia_sol, "millones de km")
        print("Tipo:", self.tipo.value if self.tipo else None)
        print("Observable a simple vista:", self.observable)
        print("-" * 40)

    def calcular_densidad(self):
        if self.volumen == 0:
            return 0
        return self.masa / self.volumen

    def es_exterior(self):
        distancia_en_ua = self.distancia_sol / Planeta.UA
        return distancia_en_ua > 3.4

def main():
    tierra = Planeta("Tierra", 1, 5.97e24, 1.08321e12, 12742, 149,
                     TipoPlaneta.TERRESTRE, True)
    jupiter = Planeta("Júpiter", 95, 1.898e27, 1.4313e15, 139820, 778,
                      TipoPlaneta.GASEOSO, True)

    for planeta in (tierra, jupiter):
        planeta.mostrar_datos()
        print(f"Densidad de {planeta.nombre}: {planeta.calcular_densidad():.2e} kg/km³")
        if planeta.es_exterior():
            print(f"{planeta.nombre} es un planeta exterior.")
        else:
            print(f"{planeta.nombre} NO es un planeta exterior.")
        print()

if __name__ == "__main__":
    main()
