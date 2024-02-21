from pygame import Surface, Color
import pygame

class Line:
    @staticmethod
    def horizontal(surface: Surface, color: Color, start: tuple, end: int):
        start = (int(start[0]), int(start[1]))
        
        while (start[0] <= end):
            surface.set_at(start, color)
            start = (int(start[0] + 1), int(start[1]))

    @staticmethod
    def vertical(surface: Surface, color: Color, start: tuple, end: int):
        start = (int(start[0]), int(start[1]))

        while (start[1] <= end):
            surface.set_at(start, color)
            start = (int(start[0]), int(start[1] + 1))