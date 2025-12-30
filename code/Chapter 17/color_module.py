# Listing 17.1 File color_module.py

class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return f"Color: R={self._red:d}, G={self._green:d}, B={self._blue:d}"
