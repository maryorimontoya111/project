import unittest
from main import crear_producto, leer_producto, actualizar_producto, eliminar_producto

class TestCRUD(unittest.TestCase):

    def test_crear_producto(self):
        producto = {"nombre": "Manzana", "descripción": "Fruta roja", "precio": 1.5, "cantidad": 10}
        resultado = crear_producto(producto)
        self.assertEqual(resultado["nombre"], "Manzana")
        self.assertEqual(resultado["precio"], 1.5)
        self.assertEqual(resultado["cantidad"], 10)

    def test_leer_producto(self):
        producto = {"nombre": "Manzana", "descripción": "Fruta roja", "precio": 1.5, "cantidad": 10}
        creado = crear_producto(producto)
        leido = leer_producto(creado["id"])
        self.assertEqual(leido["nombre"], "Manzana")
        self.assertEqual(leido["precio"], 1.5)

    def test_actualizar_producto(self):
        producto = {"nombre": "Manzana", "descripción": "Fruta roja", "precio": 1.5, "cantidad": 10}
        creado = crear_producto(producto)
        nuevos_datos = {"precio": 2.0}
        resultado = actualizar_producto(creado["id"], nuevos_datos)
        self.assertEqual(resultado["precio"], 2.0)

    def test_eliminar_producto(self):
        producto = {"nombre": "Manzana", "descripción": "Fruta roja", "precio": 1.5, "cantidad": 10}
        creado = crear_producto(producto)
        eliminado = eliminar_producto(creado["id"])
        self.assertEqual(eliminado["nombre"], "Manzana")
        leido = leer_producto(creado["id"])
        self.assertIsNone(leido)

if __name__ == "__main__":
    unittest.main()
