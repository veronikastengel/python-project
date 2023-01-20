#!/usr/bin/env python
# coding: utf-8

from PIL import Image
def show_an_image(path):
    # creating a object
    im = Image.open(path)
    # showing it
    im.show()