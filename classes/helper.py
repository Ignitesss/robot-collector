import math
import pygame as pg


def to_velosity(speed: float, direction: float):
    return pg.Vector2(speed*math.cos(direction),speed*math.sine(direction))