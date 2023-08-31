'''класс, который разбирает hex rgb в десятичные значения'''
class Color:
    def __init__(self,hex):
        self.hexcode = hex
    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value
        self.r = int(value[0:2], 16)
        self.g = int(value[2:4], 16)
        self.b = int(value[4:], 16)
