import os
import sys

class Beer:
    def __init__(self, name, price, url, image, brewery=""):
        self.name = name
        self.brewery = brewery
        self.price = price
        self.url = url
        self.image = image