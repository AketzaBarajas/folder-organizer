import os

# Averigüar quíen soy para el sistema
ruta_base = os.path.expanduser('~')
print(f"1. La ruta base de mi usuario es: {ruta_base}")

# Ver las carpetas reales que hay
print("2. Carpetas disponibles en mi usuario:")
try:
    contenido = os.listdir(ruta_base)
    for archivo in contenido:
        # Solo imprimimos si parece una carpeta de descargas
        if 'ownload' in archivo or 'escarga' in archivo:
            print(f"  --> ¡ENCONTRADO!:  {archivo}")
except Exception as e:
    print(f"Error al leer el directorio: {e}")

# La ruta que falló
ruta_fallo = os.path.join(ruta_base, 'Descargas')
print(f"3. Intentamos entrar a: {ruta_fallo}")