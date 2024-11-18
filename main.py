import json

DB_FILE = "productos.json"

def cargar_datos():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_datos(productos):
    with open(DB_FILE, "w") as file:
        json.dump(productos, file, indent=4)

def crear_producto(producto):
    productos = cargar_datos()
    producto['id'] = len(productos) + 1  
    productos.append(producto)
    guardar_datos(productos)
    return producto

def leer_producto(product_id=None):
    productos = cargar_datos()
    if product_id:
        for producto in productos:
            if producto["id"] == product_id:
                return producto
        return None
    return productos

def actualizar_producto(product_id, nuevos_datos):
    productos = cargar_datos()
    for producto in productos:
        if producto["id"] == product_id:
            producto.update(nuevos_datos)
            guardar_datos(productos)
            return producto
    return None

def eliminar_producto(product_id):
    productos = cargar_datos()
    for producto in productos:
        if producto["id"] == product_id:
            productos.remove(producto)
            guardar_datos(productos)
            return producto
    return None
