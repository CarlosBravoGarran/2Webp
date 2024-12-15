import os
import argparse
from PIL import Image

def to_webp(directory):
    if not os.path.isdir(directory):
        print(f"Error: La carpeta '{directory}' no existe.")
        return

    # Extensiones de imágenes soportadas
    supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if not os.path.isfile(filepath):
            continue
        
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # Si ya es WebP, lo ignoramos
        if ext == ".webp":
            print(f"{filename} ya está en formato WebP. Se omite.")
            continue
        
        if ext in supported_formats:
            try:
                with Image.open(filepath) as img:
                    webp_path = os.path.join(directory, f"{name}.webp")
                    img.save(webp_path, "webp")
                    print(f"{filename} convertido a {name}.webp")
                    # Opcional: Eliminar el archivo original
                    # os.remove(filepath)
            except Exception as e:
                print(f"Error al convertir {filename}: {e}")
        else:
            print(f"{filename} no es un formato soportado. Se omite.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte imágenes a formato WebP.")
    parser.add_argument("directory", type=str, help="Ruta de la carpeta con imágenes a convertir.")
    args = parser.parse_args()

    to_webp(args.directory)

