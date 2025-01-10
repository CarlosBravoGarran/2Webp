# 2Webp - Image to WebP Converter

This Python script allows web developers to easily convert images from several common formats to WebP. You can specify a complete directory or an individual file for conversion and optionally delete the original files after conversion.

## Features

- Converts images to WebP format.
- Supports multiple image formats such as PNG, JPG, JPEG, BMP, and TIFF.
- Ability to convert multiple files/directories at once.
- Option to delete the original files after conversion with the `-r` flag.

## Clone the Repository

To get started, clone this repository to your device:

   ```bash
   git clone git@github.com:CarlosBravoGarran/2Webp.git      # SSH
   cd 2webp
   ```
   ```bash
   git clone https://github.com/CarlosBravoGarran/2Webp.git  # HTTPS
   cd 2webp
   ```

## Requirements

To run this script, you need Python and Pillow. The script has been tested with Python 3.8 or higher. Make sure they are installed on your system.

### Installing Pillow in Your Virtual Environment

Before running the script, you need to install the necessary requirements in  your virtual enviroment:

- Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To use the script, navigate to the directory where the script is located and run it by passing the path of the directory or file you want to convert:

```bash
python 2webp.py paths/to/images
```

### Delete Original Files

If you want to delete the original files after converting them to WebP format, you can add the `-r` flag:

```bash
python 2webp.py -r paths/to/images
```

### Usage Examples

Convert all images in a directory and another image while keeping the original files:

```bash
python 2webp.py /path/to/directory /path/to/file
```

Convert a specific image and delete the original file:

```bash
python 2webp.py -r /path/to/image.png
```
