import unittest
from main import crear_producto, leer_producto, actualizar_producto, eliminar_producto

class TestCRUD(unittest.TestCase):

    def test_crear_producto(self):
        producto = {"nombre": "Manzana", "descripción": "Fruta roja", "precio": 1.5, "cantidad": 10}
        resultado = crear_producto(producto)
        self.assertEqual(resultado["nombre"], "Manzana")

    def test_leer_producto(self):
        self.assertIsNotNone(leer_producto())

    def test_actualizar_producto(self):
        nuevos_datos = {"precio": 2.0}
        resultado = actualizar_producto(1, nuevos_datos)
        self.assertIsNotNone(resultado)

    def test_eliminar_producto(self):
        resultado = eliminar_producto(1)
        self.assertIsNotNone(resultado)

if __name__ == "__main__":
    unittest.main()
