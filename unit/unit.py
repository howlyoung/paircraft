

class Unit(object):
    def __init__(self):
        super().__init__()
        # 血量
        self.hp = 0
        # 速度
        self.speed = 0
        # 位置X
        self.x = 0
        # 旧位置X
        self.old_x = 0
        # 旧位置Yy
        self.old_y = 0
        # 位置y
        self.y = 0
        # 图片位置
        self.image = ''

    # 移动
    def move(self, dir):
        # 保存当前位置，方便回退
        self.old_x = self.x
        self.old_y = self.y
        # 向上移动
        if dir == 1:
            self.y = self.y - self.speed
        # 向下移动
        elif dir == 2:
            self.y = self.y + self.speed
        # 向左移动
        elif dir == 3:
            self.x = self.x - self.speed
        # 向右移动
        else:
            self.x = self.x + self.speed

    # 获得单元的图片地址
    def get_image(self):
        return self.image

    # 获取位置
    def get_poisiion(self):
        return [self.x, self.y]
