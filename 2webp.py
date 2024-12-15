import os
import argparse
from PIL import Image

def convert_to_webp(file_path, remove_original, converted_files, removed_files, already_webp_files):
    name, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".webp":
        already_webp_files.append(file_path)
        return

    supported_formats = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    if ext in supported_formats:
        try:
            with Image.open(file_path) as img:
                webp_path = f"{name}.webp"
                img.save(webp_path, "webp")
                converted_files.append(webp_path)
                if remove_original:
                    os.remove(file_path)
                    removed_files.append(file_path)
        except Exception as e:
            print(f"Error converting {file_path}: {e}\n")
    else:
        print(f"{file_path} is not a supported format.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to WebP format.")
    parser.add_argument('-r', '--remove', action='store_true',
                        help="Remove the original files after conversion.")
    parser.add_argument('paths', nargs='+', help="Paths of the files or directories with images to convert.")
    args = parser.parse_args()

    converted_files = []
    removed_files = []
    already_webp_files = []

    for path in args.paths:
        if os.path.isdir(path):
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if os.path.isfile(file_path):
                    convert_to_webp(file_path, args.remove, converted_files, removed_files, already_webp_files)
        elif os.path.isfile(path):
            convert_to_webp(path, args.remove, converted_files, removed_files, already_webp_files)
        else:
            print(f"Error: '{path}' is not a valid file or directory.\n")

    if already_webp_files:
        print("Files already in WebP format:")
        for file in already_webp_files:
            print(' ', file)
        print()

    if converted_files:
        print("Converted files:")
        for file in converted_files:
            print(' ', file)
        print() 

    if args.remove and removed_files:
        print("Original files removed:")
        for file in removed_files:
            print(' ', file)
