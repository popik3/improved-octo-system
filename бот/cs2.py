import time
import pyautogui
import keyboard
import random
import cv2
import numpy as np
from typing import Tuple, List, Dict
import win32gui
import win32con
import win32api
import threading

class CS2Instance:
    def __init__(self, hwnd: int, instance_id: int):
        self.hwnd = hwnd
        self.instance_id = instance_id
        self.position: Tuple[float, float] = (0, 0)
        self.health: int = 100
        self.ammo: int = 30
        self.team: str = 'CT' if instance_id % 2 == 0 else 'T'
        
        # Получаем размеры и позицию окна
        rect = win32gui.GetWindowRect(hwnd)
        self.window_x = rect[0]
        self.window_y = rect[1]
        self.window_width = rect[2] - rect[0]
        self.window_height = rect[3] - rect[1]
        
        # Основные точки на карте (относительные координаты)
        self.positions = {
            'CT': [
                (0.4, 0.3),   # A-сайт
                (0.6, 0.4),   # B-сайт
                (0.5, 0.35),  # Мид
            ],
            'T': [
                (0.2, 0.15),   # T-спавн
                (0.3, 0.2),    # Туннели
                (0.4, 0.25),   # Длинная
            ]
        }

    def get_absolute_position(self, relative_pos: Tuple[float, float]) -> Tuple[int, int]:
        """Конвертация относительных координат в абсолютные для конкретного окна"""
        x = self.window_x + int(self.window_width * relative_pos[0])
        y = self.window_y + int(self.window_height * relative_pos[1])
        return (x, y)

    def focus_window(self):
        """Установка фокуса на окно"""
        win32gui.SetForegroundWindow(self.hwnd)
        time.sleep(0.1)

    def move(self, target_pos: Tuple[float, float]) -> None:
        """Перемещение к указанной позиции"""
        try:
            self.focus_window()
            abs_pos = self.get_absolute_position(target_pos)
            print(f"Инстанс {self.instance_id}: Перемещение к {abs_pos}")
            
            keyboard.press('w')
            pyautogui.moveTo(abs_pos[0], abs_pos[1])
            time.sleep(random.uniform(1.0, 2.0))
            keyboard.release('w')
        except Exception as e:
            print(f"Ошибка при движении: {e}")

    def aim_and_shoot(self, target_pos: Tuple[float, float]) -> None:
        """Прицеливание и стрельба"""
        try:
            self.focus_window()
            abs_pos = self.get_absolute_position(target_pos)
            
            pyautogui.moveTo(abs_pos[0], abs_pos[1], duration=0.1)
            pyautogui.mouseDown(button='left')
            time.sleep(random.uniform(0.1, 0.3))
            pyautogui.mouseUp(button='left')
        except Exception as e:
            print(f"Ошибка при стрельбе: {e}")

    def check_for_enemies(self) -> bool:
        """Проверка наличия врагов на экране"""
        try:
            self.focus_window()
            # Делаем скриншот только нужного окна
            screenshot = pyautogui.screenshot(region=(
                self.window_x, 
                self.window_y, 
                self.window_width, 
                self.window_height
            ))
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Здесь можно добавить более сложную логику обнаружения врагов
            return False
        except Exception as e:
            print(f"Ошибка при проверке врагов: {e}")
            return False

    def reload_weapon(self) -> None:
        """Перезарядка оружия"""
        try:
            self.focus_window()
            keyboard.press('r')
            time.sleep(0.1)
            keyboard.release('r')
            time.sleep(2.5)
            self.ammo = 30
        except Exception as e:
            print(f"Ошибка при перезарядке: {e}")

    def buy_equipment(self) -> None:
        """Покупка снаряжения в начале раунда"""
        try:
            self.focus_window()
            
            keyboard.press('b')
            time.sleep(0.1)
            keyboard.release('b')
            
            keyboard.press('4')  # AK-47/M4A4
            time.sleep(0.1)
            keyboard.release('4')
            
            keyboard.press('5')  # Броня + шлем
            time.sleep(0.1)
            keyboard.release('5')
            
            keyboard.press('6')  # Флешка
            time.sleep(0.1)
            keyboard.release('6')
        except Exception as e:
            print(f"Ошибка при покупке: {e}")

class CS2Bot:
    def __init__(self):
        self.instances: Dict[int, CS2Instance] = {}
        # Настройки безопасности
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1

    def find_cs2_windows(self) -> List[int]:
        """Поиск всех окон CS2"""
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd):
                window_title = win32gui.GetWindowText(hwnd)
                if "Counter-Strike 2" in window_title:
                    hwnds.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds

    def setup_instances(self):
        """Настройка всех найденных инстансов CS2"""
        cs2_windows = self.find_cs2_windows()
        print(f"Найдено окон CS2: {len(cs2_windows)}")
        
        for i, hwnd in enumerate(cs2_windows):
            self.instances[hwnd] = CS2Instance(hwnd, i)
            # Расположение окон сеткой
            x = (i % 2) * 960
            y = (i // 2) * 540
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, 960, 540, 0)

    def run_instance(self, instance: CS2Instance):
        """Управление отдельным инстансом игры"""
        while True:
            try:
                if instance.health <= 0:
                    time.sleep(5)
                    instance.buy_equipment()
                    continue

                if instance.check_for_enemies():
                    instance.aim_and_shoot(instance.position)

                if instance.ammo <= 5:
                    instance.reload_weapon()

                positions = instance.positions[instance.team]
                target_pos = random.choice(positions)
                instance.move(target_pos)

                time.sleep(random.uniform(0.5, 1.5))

            except Exception as e:
                print(f"Ошибка в инстансе {instance.instance_id}: {str(e)}")
                time.sleep(1)

    def run(self):
        """Основной цикл бота"""
        print("Запуск мульти-инстанс бота CS2")
        print("ВНИМАНИЕ: Убедитесь, что все окна CS2 запущены!")
        print("Нажмите Ctrl+C для остановки")
        time.sleep(5)

        try:
            self.setup_instances()
            
            # Запускаем отдельный поток для каждого инстанса
            threads = []
            for instance in self.instances.values():
                thread = threading.Thread(target=self.run_instance, args=(instance,))
                thread.daemon = True
                threads.append(thread)
                thread.start()

            # Ждем завершения всех потоков
            for thread in threads:
                thread.join()

        except KeyboardInterrupt:
            print("\nБот остановлен пользователем")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    bot = CS2Bot()
    bot.run()