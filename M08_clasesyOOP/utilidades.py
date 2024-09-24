# Archivo: utilidades.py

class utilidades:
    
    def __init__(self, lista_numeros):
        # Inicializa la clase con una lista de números.
        if not isinstance(lista_numeros, list):
            raise ValueError("Debes proporcionar una lista de números.")
        self.lista = lista_numeros

    def es_primo(self, numero):
        # Verifica si un número es primo.
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def obtener_primos(self):
        # Devuelve una lista de los números primos en la lista.
        return [numero for numero in self.lista if self.es_primo(numero)]

    def valor_modal(self):
        # Devuelve el valor modal de la lista (el número que más se repite).
        if not self.lista:
            raise ValueError("La lista no puede estar vacía.")
        frecuencias = {}
        for numero in self.lista:
            frecuencias[numero] = frecuencias.get(numero, 0) + 1
        max_repeticiones = max(frecuencias.values())
        for numero, repeticiones in frecuencias.items():
            if repeticiones == max_repeticiones:
                return numero, repeticiones

    def convertir_temperatura(self, valor, origen, destino):
        # Convierte una temperatura de una unidad a otra (Celsius, Fahrenheit, Kelvin).
        if origen == 'C':
            celsius = valor
        elif origen == 'F':
            celsius = (valor - 32) * 5/9
        elif origen == 'K':
            celsius = valor - 273.15
        else:
            raise ValueError("Unidad de origen no válida. Usa 'C', 'F' o 'K'.")
        
        if destino == 'C':
            return celsius
        elif destino == 'F':
            return (celsius * 9/5) + 32
        elif destino == 'K':
            return celsius + 273.15
        else:
            raise ValueError("Unidad de destino no válida. Usa 'C', 'F' o 'K'.")

    def factorial(self, n):
        # Calcula el factorial de un número.
        if not isinstance(n, int):
            raise ValueError("El número debe ser un entero.")
        if n < 0:
            raise ValueError("El número no puede ser negativo.")
        
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado