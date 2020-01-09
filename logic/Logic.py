import pygame


class Logic(object):
    def __init__(self):
        super().__init__()
        # 玩家子弹列表
        self.plane_bullet_list = []
        # 敌人子弹列表
        self.enemy_bullet_list = []
        # 敌人单元列表
        self.enemy_list = []
