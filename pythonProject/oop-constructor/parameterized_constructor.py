class Shape:
    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

    def setColor(self, c):
        self.color = c

    def getColor(self):
        return self.color

    def setBorderWidth(self, borderWidth):
        self.borderWidth = borderWidth

    def getBorderWidth(self):
        return self.borderWidth


s = Shape("Red", 5)
print("Color", s.getColor())
print("BorderWidth", s.getBorderWidth())
