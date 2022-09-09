"""
draw_rect_alpha.py
Lenny Vigeon (lenny.vigeon@gmail.com)
To draw rect with transparency
Copyright (c) 2022
"""

import pygame

def draw_rect_alpha(surface, color, rect, alpha):
    rect_surface = pygame.Surface(pygame.Rect(rect).size)
    rect_surface.set_alpha(alpha)
    pygame.draw.rect(rect_surface, color, rect_surface.get_rect())
    surface.blit(rect_surface, rect)