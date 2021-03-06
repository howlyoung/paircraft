import pygame


class Event():

    def __init__(self):
        # 注册的事件的字典
        self.event_list = {}

    def keyboard_event(self):
        for event in pygame.event.get():
            if event.key in self.event_list:
                handle_list = self.event_list[event.key]
                for handle in handle_list:
                    handle.event_handle(event)

    '''
    注册事件
    如果是对象必须有event_handle方法
    参数是event
    也可以是方法
    '''

    def register_event(self, event_key, event_handle):
        val = self.event_list.get(event_key)
        if val is None:
            key_list = [event_handle]
            self.event_list[event_key] = key_list
        else:
            self.event_list[event_key] = event_handle
