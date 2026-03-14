from datetime import datetime

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial
        self.__historial = []
        if saldo_inicial > 0:
            self._registrar_transaccion(\"Depósito inicial\", saldo_inicial)

    def __validar_monto(self, monto):
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise ValueError(\"El monto debe ser un número positivo.\")

    def _registrar_transaccion(self, tipo, monto):
        self.__historial.append({
            \"fecha\": datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\"),
            \"tipo\": tipo,
            \"monto\": monto,
            \"saldo_resultante\": self.__saldo
        })

    def depositar(self, monto):
        self.__validar_monto(monto)
        self.__saldo += monto
        self._registrar_transaccion(\"Depósito\", monto)

    def retirar(self, monto):
        self.__validar_monto(monto)
        if monto > self.__saldo:
            raise ValueError(\"Fondos insuficientes.\")
        self.__saldo -= monto
        self._registrar_transaccion(\"Retiro\", monto)

    def consultar_saldo(self):
        return self.__saldo

    def mostrar_info(self):
        return f\"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: ${self.__saldo:.2f}\"

    def obtener_historial(self):
        return self.__historial
