

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
        # 攻击力
        self.attack = 0
        # 存活标志
        self.life = 1
        # 防御值
        self.defense = 0

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

    # 被击中
    def be_hit(self, unit):
        hurt = unit.get_attack() - self.get_def()
        if hurt > 0:
            if hurt >= self.get_hp():
                # 被击落
                self.life = 0
            else:
                self.hp = self.hp - hurt

    # 获取攻击力
    def get_attack(self):
        return self.attack

    # 获取防御力
    def get_def(self):
        return self.defense

    # 获得血量
    def get_hp(self):
        return self.hp
