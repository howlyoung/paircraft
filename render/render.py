import pygame
from pygame.sprite import Sprite

class Render():
    def __init__(self, config):
        # 单元列表,存放要渲染的单元
        self.unit_list = []
        # 初始化屏幕对象
        self.screen = pygame.display.set_mode(config.screen_width, config.screen_height)
        self.screen.fill(config.background)

    # 渲染整个场景
    def render(self):
        for unit in self.unit_list:
            image = pygame.image.load(unit.get_image())
            rect = image.get_rect()
            poisition = unit.get_poisiion()
            rect.x = poisition[0]
            rect.y = poisition[1]
            self.screen.blit(image, rect)
        pygame.display.filp()

    # 将单元加入列表
    def add_unit(self, unit):
        self.unit_list.append(unit)

    # 将单元移出列表
    def del_unit(self, unit):
        self.unit_list.remove(unit)    
