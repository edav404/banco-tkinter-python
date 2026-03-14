from cuenta_bancaria import CuentaBancaria

class Banco:
    def __init__(self, nombre="Banco Nacional"):
        self.nombre = nombre
        self.__cuentas = {}

    def crear_cuenta(self, numero, titular, saldo_inicial=0):
        if numero in self.__cuentas:
            raise ValueError(f"Ya existe una cuenta con el numero {numero}.")
        if not titular or not titular.strip():
            raise ValueError("El titular no puede estar vacio.")
        nueva = CuentaBancaria(numero, titular, saldo_inicial)
        self.__cuentas[numero] = nueva
        return nueva

    def buscar_cuenta(self, numero):
        if numero not in self.__cuentas:
            raise KeyError(f"No se encontro ninguna cuenta con el numero {numero}.")
        return self.__cuentas[numero]

    def listar_cuentas(self):
        return [c for c in self.__cuentas.values()]

    def total_cuentas(self):
        return len(self.__cuentas)

    def saldo_global(self):
        return sum(c.consultar_saldo() for c in self.__cuentas.values())
