from unit import Unit


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
