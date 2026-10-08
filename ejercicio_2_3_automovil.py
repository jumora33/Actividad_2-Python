from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas natural"

class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    def __init__(self, marca, modelo, motor, combustible, tipo,
                 num_puertas, num_asientos, velocidad_maxima, color,
                 velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_motor(self):
        return self.motor

    def get_combustible(self):
        return self.combustible

    def get_tipo(self):
        return self.tipo

    def get_num_puertas(self):
        return self.num_puertas

    def get_num_asientos(self):
        return self.num_asientos

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def get_color(self):
        return self.color

    def get_velocidad_actual(self):
        return self.velocidad_actual

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_motor(self, motor):
        self.motor = motor

    def set_combustible(self, combustible):
        self.combustible = combustible

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_num_puertas(self, num_puertas):
        self.num_puertas = num_puertas

    def set_num_asientos(self, num_asientos):
        self.num_asientos = num_asientos

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color):
        self.color = color

    def set_velocidad_actual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento):
        nueva = self.velocidad_actual + incremento
        if nueva > self.velocidad_maxima:
            print("No se puede acelerar más allá de la velocidad máxima "
                  f"({self.velocidad_maxima} km/h).")
        else:
            self.velocidad_actual = nueva

    def desacelerar(self, decremento):
        nueva = self.velocidad_actual - decremento
        if nueva < 0:
            print("No se puede desacelerar a una velocidad negativa.")
        else:
            self.velocidad_actual = nueva

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):

        if self.velocidad_actual == 0:
            print("El automóvil está detenido, no se puede calcular el tiempo.")
            return None
        return distancia / self.velocidad_actual

    def mostrar_datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Motor:", self.motor, "L")
        print("Combustible:", self.combustible.value)
        print("Tipo de automóvil:", self.tipo.value)
        print("Número de puertas:", self.num_puertas)
        print("Número de asientos:", self.num_asientos)
        print("Velocidad máxima:", self.velocidad_maxima, "km/h")
        print("Color:", self.color.value)
        print("Velocidad actual:", self.velocidad_actual, "km/h")
        print("-" * 40)

def main():
    auto = Automovil("Toyota", 2022, 1.8, TipoCombustible.GASOLINA,
                     TipoAutomovil.COMPACTO, 4, 5, 200, Color.ROJO)

    auto.mostrar_datos()

    auto.set_velocidad_actual(100)
    print("Velocidad actual:", auto.get_velocidad_actual(), "km/h")

    auto.acelerar(20)
    print("Después de acelerar 20 km/h:", auto.get_velocidad_actual(), "km/h")

    auto.desacelerar(50)
    print("Después de desacelerar 50 km/h:", auto.get_velocidad_actual(), "km/h")

    tiempo = auto.calcular_tiempo_llegada(140)
    print(f"Tiempo estimado para 140 km: {tiempo:.2f} horas")

    auto.frenar()
    print("Después de frenar:", auto.get_velocidad_actual(), "km/h")

if __name__ == "__main__":
    main()
