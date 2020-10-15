#!/usr/bin/env python

import requests
from PIL import Image
from io import BytesIO

def get_google_image():
    website = requests.get('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
    png = Image.open(BytesIO(website.content))
    png.show()


def main():
    print(f"Testing here")


if __name__ == "__main__":
    main()
