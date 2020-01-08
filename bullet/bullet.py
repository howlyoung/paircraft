from unit import Unit


class Bullet(Unit):
    def __init__(self, config):
        super().__init__()
        self.arm_flag = config.flag
        self.image = config.image
        self.speed = config.speed
        self.x = config.x
        self.y = config.y
        self.dir = 0
