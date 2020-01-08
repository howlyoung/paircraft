from unit import Unit
from bullet import Bullet


class Arms(Unit):
    def __init__(self):
        super().__init__()
        # 子弹数量
        self.count = 0
        # 剩余子弹数量
        self.surplus_count = 0
        # 武器标识
        self.flag = ''
        # 当前持有武器的对象
        self.owner = None

    # 发射
    def attack(self):
        if self.surplus_count > 0:
            self.surplus_count = self.surplus_count - 1
            return [Bullet(self.get_config())]
        else:
            return []

    # 填充
    def fill(self):
        pass

    # 获取子弹显示配置
    def get_config(self):
        return {'flag': '', 'speed': self.owner.speed,
                'x': self.owner.x, 'y': self.owner.y, 'image': ''}
