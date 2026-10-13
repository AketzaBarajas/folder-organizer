# Importación de librerías
import os
import shutil

# Estructura diccionario con las extensiones
extensiones = {
    'Imagenes' : ['.jpg','.jpeg','.png','.gif','webp'],
    'Documentos' : ['.doc','.docx','.xls','.xlsx','.ppt','.pptx','.txt'],
    'PDFs' : ['.pdf'],
    'Videos' : ['.mp4','.mkv','.avi','.mov','.webm'],
    'Comprimidos' : ['.zip','.rar'],
    'Instaladores' : ['.exe','.msi','.bat']
}

# Definir ruta de forma dinámica
ruta_base = os.path.expanduser("~")
ruta_descargas = os.path.join(ruta_base, "Downloads")

# Verificación de seguridad
if os.path.exists(ruta_descargas):
    print(f"--> Analizando carpeta: {ruta_descargas}")

    archivos = os.listdir(ruta_descargas) # Todos los archivos de la carpeta 'Downloads'

    # Bucle de análisis
    for archivo in archivos:
        # Ignorar archivos ocultos o propios del script
        if archivo.startswith(".") or archivo == "organizar_descargas.py":
            continue

        # Separamos el nombre y la extensión
        nombre, extension = os.path.splitext(archivo)

        # Poner extensiones en minúsculas
        extension = extension.lower()

        # Destino determinado
        carpeta_destino = 'Otros'
    
        # Buscar en el diccionario
        for categoria, lista_extensiones in extensiones.items():
            if extension in lista_extensiones:
                carpeta_destino = categoria
                break # Cuando encuentre la extensión para el bucle

        # Construir rutas completas
        ruta_origen = os.path.join(ruta_descargas, archivo)
        ruta_carpeta_destino = os.path.join(ruta_descargas, carpeta_destino)

        try:
            # Crear carpeta en caso de que no exista
            os.makedirs(ruta_carpeta_destino, exist_ok = True)

            # Mover el archivo
            shutil.move(ruta_origen, ruta_carpeta_destino)

            # Imprimir
            print(f"Movido: {archivo:50} >>> {carpeta_destino}")
        
        except Exception as e:
            print(f"Error moviendo {archivo} : {e}")

    print("¡ORGANIZACIÓN COMPLETADA!")

else:
    print("Error crítico: Ruta no encontrada")