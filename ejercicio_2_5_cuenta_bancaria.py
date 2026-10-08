from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "Ahorros"
    CORRIENTE = "Corriente"

class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta):
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0  # toda cuenta nueva empieza en cero

    def mostrar_datos(self):
        print("Titular:", self.nombres, self.apellidos)
        print("Número de cuenta:", self.numero_cuenta)
        print("Tipo de cuenta:", self.tipo_cuenta.value)
        print("Saldo:", self.saldo)
        print("-" * 30)

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, valor):
        if valor <= 0:
            print("El valor a consignar debe ser mayor que cero.")
        else:
            self.saldo += valor
            print(f"Se consignaron ${valor}. Nuevo saldo: ${self.saldo}")

    def retirar(self, valor):
        if valor <= 0:
            print("El valor a retirar debe ser mayor que cero.")
        elif valor > self.saldo:
            print(f"Fondos insuficientes. Saldo actual: ${self.saldo}")
        else:
            self.saldo -= valor
            print(f"Se retiraron ${valor}. Nuevo saldo: ${self.saldo}")

def main():
    cuenta = CuentaBancaria("Carlos Andrés", "Gómez Restrepo",
                            "123456789", TipoCuenta.AHORROS)

    cuenta.mostrar_datos()

    cuenta.consignar(500000)
    print("Saldo actual:", cuenta.consultar_saldo())

    cuenta.retirar(200000)
    print("Saldo actual:", cuenta.consultar_saldo())

    # Intento de retiro mayor al saldo
    cuenta.retirar(1000000)
    print("Saldo final:", cuenta.consultar_saldo())

if __name__ == "__main__":
    main()
