class Settings():
    """класс для хранения всех настроек игры alien imposible"""

    def __init__(self):
        """Инициализирует настройки игры"""
        #Параматры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)#красный, зелёный, синий
        # Настройки корабля
        self.ship_speed = 10.5
        #параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_heught = 15
        self.bullet_color = (60, 60, 60)