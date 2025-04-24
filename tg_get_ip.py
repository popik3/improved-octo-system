# Этот скрипт предназначен для определения IP-адреса собеседника в мессенджере Telegram.
# Для его использования необходимо установить tshark.
# Протестировано на macOS 13.4.1 и Ubuntu Linux 20.
# Возможно, будет работать на телефоне Android с root-правами и Termux.
# Автор: n0a, 2020-2023
# https://n0a.pw

import ipaddress
import netifaces
import requests
import argparse
import platform
import pyshark
import sys
import http.client
import http.client
import os
import platform

def get_wireshark_install_path_from_registry():
    try:
        import winreg
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Wireshark")
        value, _ = winreg.QueryValueEx(registry_key, "InstallLocation")
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def check_tshark_availability():
    """Проверка наличия tshark."""
    wireshark_path = None
    if platform.system() == "Windows":
        wireshark_path = get_wireshark_install_path_from_registry()
    elif platform.system() == "Darwin":
        wireshark_path = "/Applications/Wireshark.app/Contents/MacOS"
    elif platform.system() == "Linux":
        wireshark_path = os.popen('which wireshark').read().strip()
        tshark_path = os.popen('which tshark').read().strip()
        if os.path.isfile(wireshark_path):
            wireshark_path = os.path.dirname(wireshark_path)
        elif os.path.isfile(tshark_path):
            wireshark_path = os.path.dirname(tshark_path)

    if not wireshark_path:
        os_type = platform.system()
        if os_type == "Linux":
            print("Установите tshark: sudo apt update && apt install tshark")
        elif os_type == "Darwin":  # macOS
            print("Установите Wireshark: https://www.wireshark.org/download.html")
        else:
            print("Установите tshark. Попробуйте загрузить его отсюда: https://www.wireshark.org/download.html")
        sys.exit(1)
    else:
        print("[+] tshark доступен.")

# Список исключенных диапазонов IP-адресов Telegram
EXCLUDED_NETWORKS = ['91.108.13.0/24', '149.154.160.0/21', '149.154.160.0/22',
                     '149.154.160.0/23', '149.154.162.0/23', '149.154.164.0/22',
                     '149.154.164.0/23', '149.154.166.0/23', '149.154.168.0/22',
                     '149.154.172.0/22', '185.76.151.0/24', '91.105.192.0/23',
                     '91.108.12.0/22', '91.108.16.0/22', '91.108.20.0/22',
                     '91.108.4.0/22', '91.108.56.0/22', '91.108.56.0/23',
                     '91.108.58.0/23', '91.108.8.0/22', '95.161.64.0/20']


def get_hostname(ip):
    """Получение имени хоста для указанного IP."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

def get_my_ip():
    """Получение внешнего IP-адреса."""
    try:
        return requests.get('https://icanhazip.com').text.strip()
    except Exception as e:
        print(f"[!] Ошибка при получении внешнего IP: {e}")
        return None

def get_whois_info(ip):
    """Получение данных whois для указанного IP."""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        # Получение имени хоста с помощью библиотеки socket
        hostname = get_hostname(ip)
        if hostname:
            print(f"[+] Имя хоста: {hostname}")

        return data
    except Exception as e:
        print(f"[!] Ошибка при получении данных whois: {e}")
        return None


def display_whois_info(data):
    """Отображение полученных данных whois."""
    if not data:
        return

    print(f"[!] Страна: {data.get('country', 'N/A')}")
    print(f"[!] Код страны: {data.get('countryCode', 'N/A')}")
    print(f"[!] Регион: {data.get('region', 'N/A')}")
    print(f"[!] Название региона: {data.get('regionName', 'N/A')}")
    print(f"[!] Город: {data.get('city', 'N/A')}")
    print(f"[!] Почтовый индекс: {data.get('zip', 'N/A')}")
    print(f"[!] Широта: {data.get('lat', 'N/A')}")
    print(f"[!] Долгота: {data.get('lon', 'N/A')}")
    print(f"[!] Часовой пояс: {data.get('timezone', 'N/A')}")
    print(f"[!] ISP: {data.get('isp', 'N/A')}")
    print(f"[!] Организация: {data.get('org', 'N/A')}")
    print(f"[!] AS: {data.get('as', 'N/A')}")


def is_excluded_ip(ip):
    """Проверка, входит ли IP в список исключенных."""
    for network in EXCLUDED_NETWORKS:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(network):
            return True
    return False


def choose_interface():
    """Предложить пользователю выбрать сетевой интерфейс."""
    interfaces = netifaces.interfaces()
    import socket, requests; print("\nВаш локальный IP:", socket.gethostbyname(socket.gethostname()), "Ваш внешний IP:", requests.get('https://api.ipify.org').text, "\n\n")
    print("[+] Доступные интерфейсы:")
    for idx, iface in enumerate(interfaces, 1):
        print(f"{idx}. {iface}")
        try:
            ip_address = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
            print(f"[+] Выбранный интерфейс: {iface}, IP-адрес: {ip_address}")
        except KeyError:
            print("[!] Не удалось получить IP-адрес для выбранного интерфейса.")

    choice = int(input("[+] Введите номер интерфейса, который хотите использовать: "))
    return interfaces[choice - 1]


def extract_stun_xor_mapped_address(interface):
    """Перехват пакетов и извлечение IP-адреса из протокола STUN."""
    print("[+] Перехват трафика, пожалуйста, подождите...")
    if platform.system() == "Windows":
        interface = "\\Device\\NPF_"+interface
    cap = pyshark.LiveCapture(interface=interface, display_filter="stun")
    my_ip = get_my_ip()
    resolved = {}
    whois = {}

    for packet in cap.sniff_continuously(packet_count=999999):
        if hasattr(packet, 'ip'):
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst

            if is_excluded_ip(src_ip) or is_excluded_ip(dst_ip):
                continue

            if src_ip not in resolved:
                resolved[src_ip] = f"{src_ip}({get_hostname(src_ip)})"
            if dst_ip not in resolved:
                resolved[dst_ip] = f"{dst_ip}({get_hostname(dst_ip)})"
            if src_ip not in whois:
                whois[src_ip] = get_whois_info(src_ip)
            if dst_ip not in whois:
                whois[dst_ip] = get_whois_info(dst_ip)
            if packet.stun:
                xor_mapped_address = packet.stun.get_field_value('stun.att.ipv4')
                print(f"[+] Найден STUN-пакет: {resolved[src_ip]} ({whois[src_ip].get('org', 'N/A')}) -> ({resolved[dst_ip]} {whois[dst_ip].get('org', 'N/A')}). XOR-адрес: {xor_mapped_address}")
                if xor_mapped_address:
                    if xor_mapped_address != my_ip:
                        return xor_mapped_address
    return None


def parse_arguments():
    """Разбор аргументов командной строки."""
    parser = argparse.ArgumentParser(
        description='Определение IP-адреса собеседника в мессенджере Telegram.')
    parser.add_argument('-i', '--interface', help='Сетевой интерфейс для использования', default=None)
    return parser.parse_args()


def main():
    try:
        check_tshark_availability()
        args = parse_arguments()

        if args.interface:
            interface_name = args.interface
        else:
            interface_name = choose_interface()

        address = extract_stun_xor_mapped_address(interface_name)
        if address:
            print(f"[+] УСПЕХ! IP-адрес: {address}")
            whois_data = get_whois_info(address)
            display_whois_info(whois_data)
        else:
            print("[!] Не удалось определить IP-адрес собеседника.")
    except (KeyboardInterrupt, EOFError):
        print("\n[+] Завершение работы...")
        pass


if __name__ == "__main__":
    main()
