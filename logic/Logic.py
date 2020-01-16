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

    def loop(self):
        # 处理这一帧的逻辑
        # 单元移动  碰撞处理

        for sprie in self.enemy_bullet_list:
            # 渲染
            pass

        for sprie in self.plane_bullet_list:
            # 渲染
            pass

        for sprie in self.enemy_list:
            # 渲染
            pass
