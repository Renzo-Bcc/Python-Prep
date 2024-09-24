# Archivo: utilidades.py

class utilidades:
    
    def __init__(self, lista_numeros):
        # Inicializa la clase con una lista de números enteros.
        if not isinstance(lista_numeros, list):
            raise ValueError("Debes proporcionar una lista.")
        
        # Verificar que todos los elementos de la lista sean enteros
        for num in lista_numeros:
            if not isinstance(num, int):
                raise ValueError("Todos los elementos de la lista deben ser números enteros.")
        
        self.lista = lista_numeros

    def es_primo(self, numero):
        # Verifica si un número es primo.
        if not isinstance(numero, int):
            raise ValueError("El número debe ser un entero.")
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
        unidades_validas = ['C', 'F', 'K']
        
        # Verificar que las unidades de origen y destino sean válidas
        if origen not in unidades_validas:
            raise ValueError(f"Unidad de origen '{origen}' no válida. Las unidades válidas son: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin).")
        
        if destino not in unidades_validas:
            raise ValueError(f"Unidad de destino '{destino}' no válida. Las unidades válidas son: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin).")
        
        # Verificar que el valor sea un número (int o float)
        if not isinstance(valor, (int, float)):
            raise ValueError(f"El valor de la temperatura debe ser un número. Se recibió: {type(valor).__name__}")
        
        # Convertir el valor a Celsius primero
        if origen == 'C':
            celsius = valor
        elif origen == 'F':
            celsius = (valor - 32) * 5/9
        elif origen == 'K':
            celsius = valor - 273.15
        
        # Convertir de Celsius a la unidad de destino
        if destino == 'C':
            return celsius
        elif destino == 'F':
            return (celsius * 9/5) + 32
        elif destino == 'K':
            return celsius + 273.15

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
