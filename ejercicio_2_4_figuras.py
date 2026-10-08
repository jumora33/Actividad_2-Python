import math
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class TrianguloRectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def tipo_triangulo(self):
        lado1 = self.base
        lado2 = self.altura
        lado3 = self.calcular_hipotenusa()

        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"

def main():
    circulo = Circulo(5)
    rectangulo = Rectangulo(4, 6)
    cuadrado = Cuadrado(5)
    triangulo = TrianguloRectangulo(3, 4)

    print("--- Círculo ---")
    print(f"Área: {circulo.calcular_area():.2f} cm²")
    print(f"Perímetro: {circulo.calcular_perimetro():.2f} cm")

    print("--- Rectángulo ---")
    print(f"Área: {rectangulo.calcular_area():.2f} cm²")
    print(f"Perímetro: {rectangulo.calcular_perimetro():.2f} cm")

    print("--- Cuadrado ---")
    print(f"Área: {cuadrado.calcular_area():.2f} cm²")
    print(f"Perímetro: {cuadrado.calcular_perimetro():.2f} cm")

    print("--- Triángulo rectángulo ---")
    print(f"Hipotenusa: {triangulo.calcular_hipotenusa():.2f} cm")
    print(f"Área: {triangulo.calcular_area():.2f} cm²")
    print(f"Perímetro: {triangulo.calcular_perimetro():.2f} cm")
    print("Tipo de triángulo:", triangulo.tipo_triangulo())

if __name__ == "__main__":
    main()
