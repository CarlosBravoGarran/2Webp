import os
import argparse
from PIL import Image

def convert_to_webp(file_path):
    # Función para convertir un archivo individual a WebP
    name, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == ".webp":
        print(f"{file_path} ya está en formato WebP. Se omite.")
        return
    
    supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    if ext in supported_formats:
        try:
            with Image.open(file_path) as img:
                webp_path = f"{name}.webp"
                img.save(webp_path, "webp")
                print(f"{file_path} convertido a {webp_path}")
                # Opcional: Eliminar el archivo original
                # os.remove(file_path)
        except Exception as e:
            print(f"Error al convertir {file_path}: {e}")
    else:
        print(f"{file_path} no es un formato soportado. Se omite.")

def to_webp(path):
    if os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                convert_to_webp(file_path)
    elif os.path.isfile(path):
        convert_to_webp(path)
    else:
        print(f"Error: '{path}' no es un archivo ni un directorio válido.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte imágenes a formato WebP.")
    parser.add_argument("path", type=str, help="Ruta del archivo o directorio con imágenes a convertir.")
    args = parser.parse_args()

    to_webp(args.path)
