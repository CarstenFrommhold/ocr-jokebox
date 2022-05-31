from PIL import Image
import os


def rotate(image_path: str):
    image = Image.open(image_path)
    rotated_image = image.rotate(180)
    rotated_image.save(image_path)


def rotate_all(path: str):
    for image in os.listdir(path):
        rotate(path + "/" + image)


if __name__ == "__main__":
    # rotate("../pictures/2022_5_31_16_39_6.jpg")
    rotate_all("../pictures")
