from dataclasses import dataclass

from pygame import Surface, Color
import pygame

from rendering import Line

@dataclass
class Circle:
    center: tuple
    radius: int

    thickness: int = 1

    @property
    def innerRadius(self):
        if self.thickness == 1:
            return self.radius

        return self.radius - self.thickness / 2

    @property
    def outerRadius(self):
        if self.thickness == 1:
            return self.radius

        return self.innerRadius + self.thickness

    def render(self, surface: Surface, color: Color):
        positionY = 0

        innerX = self.innerRadius
        outerX = self.outerRadius
        
        innerError = 1 - self.innerRadius
        outerError = 1 - self.outerRadius

        r = 0
        g = 0
        b = 255

        while (outerX >= positionY):
            color = Color(r, g, b)

            Line.horizontal(surface, color, (self.center[0] + innerX, self.center[1] + positionY), self.center[0] + outerX)
            Line.horizontal(surface, color, (self.center[0] - outerX, self.center[1] + positionY), self.center[0] - innerX)
            Line.horizontal(surface, color, (self.center[0] + innerX, self.center[1] - positionY), self.center[0] + outerX)
            Line.horizontal(surface, color, (self.center[0] - outerX, self.center[1] - positionY), self.center[0] - innerX)

            Line.vertical(surface, color, (self.center[0] + positionY, self.center[1] + innerX), self.center[1] + outerX)
            Line.vertical(surface, color, (self.center[0] - positionY, self.center[1] + innerX), self.center[1] + outerX)
            Line.vertical(surface, color, (self.center[0] - positionY, self.center[1] - outerX), self.center[1] - innerX)
            Line.vertical(surface, color, (self.center[0] + positionY, self.center[1] - outerX), self.center[1] - innerX)

            g += 1

            positionY += 1

            if (outerError < 0):
                outerError += 2 * positionY + 1
            
            else:
                outerX -= 1
                outerError += 2 * (positionY - outerX) + 1

            if (positionY > self.innerRadius):
                innerX = positionY
                return

            if (innerError < 0):
                innerError += 2 * positionY + 1

            else:
                innerX -= 1
                innerError += 2 * (positionY - innerX) + 1
