import os
from PIL import Image
from cv2 import imread

processesd_dir="data_processesd"
data_dir="data"


def get_files(path):
    files = []
    for folder in os.listdir(path):
        files.extend([(file, folder, f"{path}/{folder}/{file}") for file in os.listdir(f"{path}/{folder}")])
    return files


def resize_images(files):
    for name, value, path in files:
        image = Image.open(path)
        image.thumbnail((224, 224))
        image.save(f"./{processesd_dir}/{value}_{name}")
        print(f"saved image {name}")


def read_and_normalize_images():
    images = []
    for file in os.listdir(f"./{processesd_dir}"):
        value, _ = file.split(sep="_")
        img = imread(f"./{processesd_dir}/{file}")
        images.append((img/256, int(value)))
    return images


def main():
    # prep the files
    if not processesd_dir in os.listdir("./"):
        os.makedirs(f"./{processesd_dir}")
    resize_images(get_files(f"./{data_dir}"))
    return read_and_normalize_images()

