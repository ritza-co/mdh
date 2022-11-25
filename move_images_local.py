import requests
import sys
import os
import imghdr

from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer

md = MarkdownIt("gfm-like").enable('table')

def move_images_local(text, path):
    env = {}
    tokens = md.parse(text, env)
    image_number = 1
    for i, token in enumerate(tokens):
        if token.type == "inline":
            for child in token.children:
                if child.type == "image":
                    img_src = child.attrs['src']
                    if img_src.startswith("http"):
                        print("handling", img_src)
                        print(image_number)
                        img_subdir_path = os.path.join(path, "img")
                        if not os.path.isdir(img_subdir_path):
                            os.mkdir(img_subdir_path)
                        r = requests.get(img_src).content
                        image_type = imghdr.what(None, h=r)
                        print(image_type)
                        image_number_string = str(image_number).zfill(3)
                        imagename = f"image{image_number_string}.png"
                        dest_file = os.path.join(path, "img", imagename)
                        print("saving to", dest_file)
                        with open(dest_file, "wb") as f:
                            f.write(r)
                        image_number += 1 
def run(fle):
    with open(fle) as f:
        text = f.read()
    path = os.path.dirname(fle)
    print(path)
    move_images_local(text, path)

