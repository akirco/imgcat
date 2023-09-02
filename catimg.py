from imgcat import imgcat
from PIL import Image
from io import BytesIO
import re
import urllib3
import numpy as np
import os
import sys


def is_file_path(path):
    return os.path.isfile(path)


def is_url(img: str):
    pattern = re.compile(r'^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    return bool(pattern.match(img))


def cat_url(img: str):
    image = np.asarray(Image.open(
        BytesIO(urllib3.request("GET", img).data)))
    imgcat(image)


def cat_local(img: str):
    image = Image.open(img)
    imgcat(image)


def icat(img):
    if img == "":
        print("image is missing.")
    elif is_url(img):
        cat_url(img)
    elif is_file_path(img):
        cat_local(img)
    else:
        print("this file is not support")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.isabs(path) or is_url(path):
            abs_path = path
        else:
            abs_path = os.path.abspath(path)
        icat(abs_path)
    else:
        print("image is missing")
