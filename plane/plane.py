from unit import Unit
import pygame


class Plane(Unit):
    def __init__(self):
        super().__init__()
        # 能量
        self.mp = 0

    # 使用武器
    def attack(self):
        return self.arm.attack()

    # 切换武器
    def switch_arm(self):
        pass

    # 装备武器
    def armed(self, arm):
        pass

    def event_handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.move(4)
            elif event.key == pygame.K_LEFT:
                self.move(3)
            elif event.key == pygame.K_SPACE:
                self.attack()
            elif event.key == pygame.K_R:
                self.switch_arm()
