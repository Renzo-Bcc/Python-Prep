import unittest
from utilidades import utilidades

class TestUtilidades(unittest.TestCase):
    
    def test_creacion_objeto_incorrecta(self):
        # Prueba la creación incorrecta del objeto (lista con un tipo de dato no válido).
        with self.assertRaises(ValueError) as context:
            utilidades([1, 2, "tres", 4])  # Lista contiene un string
        
        self.assertEqual(str(context.exception), "Todos los elementos de la lista deben ser números enteros.")
    
    def test_creacion_objeto_correcta(self):
        # Prueba la creación correcta del objeto.
        try:
            util = utilidades([1, 2, 3, 4])
            self.assertIsInstance(util, utilidades)  # Verificar que el objeto se crea correctamente
        except ValueError:
            self.fail("No debería lanzarse una excepción para una lista válida.")
    
    def test_valor_modal(self):
        # Prueba el método valor_modal() sobre una lista.
        util = utilidades([1, 2, 2, 3, 4, 4, 4, 5])
        modal, repeticiones = util.valor_modal()
        self.assertEqual(modal, 4)
        self.assertEqual(repeticiones, 3)

    def test_valor_modal_lista_vacia(self):
        # Prueba el método valor_modal() con una lista vacía.
        util = utilidades([])
        with self.assertRaises(ValueError) as context:
            util.valor_modal()
        
        self.assertEqual(str(context.exception), "La lista no puede estar vacía.")

    def test_verifica_primos(self):
        # Prueba el método verifica_primos() sobre una lista.
        util = utilidades([2, 3, 4, 5, 6])
        resultado = util.obtener_primos()
        self.assertEqual(resultado, [True, True, False, True, False])

    def test_convertir_temperatura_correcta(self):
        # Prueba convertir_temperatura() con valores válidos.
        util = utilidades([1, 2, 3])
        resultado = util.convertir_temperatura(100, 'C', 'F')
        self.assertEqual(resultado, 212.0)
    
    def test_convertir_temperatura_incorrecta(self):
        # Prueba convertir_temperatura() con unidades incorrectas.
        util = utilidades([1, 2, 3])
        with self.assertRaises(ValueError) as context:
            util.convertir_temperatura(100, 'C', 'X')
        self.assertEqual(str(context.exception), "Unidad de destino 'X' no válida. Las unidades válidas son: 'C', 'F', 'K'.")

    def test_factorial_correcto(self):
        # Prueba el método factorial() con un valor correcto.
        util = utilidades([1, 2, 3])
        resultado = util.factorial(5)
        self.assertEqual(resultado, 120)

    def test_factorial_numero_negativo(self):
        # Prueba el método factorial() con un número negativo.
        util = utilidades([1, 2, 3])
        with self.assertRaises(ValueError) as context:
            util.factorial(-5)
        self.assertEqual(str(context.exception), "El número no puede ser negativo.")

    def test_factorial_no_entero(self):
        # Prueba el método factorial() con un valor no entero.
        util = utilidades([1, 2, 3])
        with self.assertRaises(ValueError) as context:
            util.factorial(4.5)
        self.assertEqual(str(context.exception), "El número debe ser un entero.")

# Ejecutar los casos de prueba
if __name__ == '__main__':
    unittest.main()