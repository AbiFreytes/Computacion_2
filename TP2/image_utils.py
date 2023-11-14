from PIL import Image
import os
from multiprocessing import Event

def convert_to_grayscale(input_path, output_path, e):
    hijo = os.getpid()
    print(f"Soy el proceso hijo - PID: {hijo}")
    with Image.open(input_path):
        image_gray = Image.open(input_path).convert("L")
        image_gray.save(output_path)
        e.set()


