from apscheduler.schedulers.background import BackgroundScheduler
import funpay as FunPayAPI
import telegram_bot as TelegramBot
import json
import time
import os
print("Текущая рабочая директория:", os.getcwd())
print("Содержимое папки:", os.listdir())

from config import CONFIG

class FunPayBot:
    def __init__(self):
        self.config = CONFIG  # Используем импортированную переменную
        self.tg_bot = TelegramBot(self.config['telegram_token'])
        self.accounts = [FunPayAPI(acc) for acc in self.config['funpay_accounts']]
        self.scheduler = BackgroundScheduler()
        
    def auto_raise_job(self):
        print("\n--- Автоподнятие лотов ---")
        for account in self.accounts:
            if account.raise_lots():
                print(f"Лоты подняты для {account.account['username']}")
                self.tg_bot.send_notification(
                    self.config['telegram_admin_id'],
                    f"✅ Лоты подняты для {account.account['username']}"
                )
    
    def check_messages_job(self):
        print("\n--- Проверка сообщений ---")
        for account in self.accounts:
            messages = account.get_unread_messages()
            for msg in messages:
                print(f"Новое сообщение от {msg['user']}: {msg['text']}")
                # Здесь будет отправка ответа

    def start(self):
        try:
            # Запускаем Telegram бота
            self.tg_bot.start_polling()
            
            # Настраиваем задачи
            self.scheduler.add_job(self.auto_raise_job, 'interval', minutes=35)
            self.scheduler.add_job(self.check_messages_job, 'interval', minutes=3)
            self.scheduler.start()
            
            print("Бот успешно запущен!")
            self.tg_bot.send_notification(
                self.config['telegram_admin_id'],
                "🚀 Бот FunPay успешно запущен!"
            )
            
            # Бесконечный цикл
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("Остановка бота...")
            self.scheduler.shutdown()
            self.tg_bot.updater.stop()
    
if __name__ == "__main__":
    print("Проверка конфига:")
    try:
        bot = FunPayBot()
        print("Конфиг успешно загружен!")
        print("Аккаунты:", bot.config['funpay_accounts'])
        bot.start()
    except Exception as e:
        print("Ошибка:", e)
        input("Нажмите Enter для выхода...")