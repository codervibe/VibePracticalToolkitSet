from crack_wifi_handshake import crack_wifi_handshake
from wifi_cracker import crack_wifi
from CMSIdentifier import cmsFingerprintRecognition


def print_menu():
    """
    打印选择菜单.
    """
    print("\n请选择一个操作:")
    print("1. 一键破解wifi")
    print("2. 破解wifi握手包")
    print("3. 一键CMS指纹识别")
    print("0. 退出")


def perform_action(choice):
    """
    根据用户选择执行相应的操作.
    """
    try:
        if choice == '1':
            crack_wifi_main()
        elif choice == '2':
            crack_wifihandshake()
        elif choice == '3':
            oneClickFingerprintRecognition()
        elif choice == '0':
            print("退出程序.")
            exit()
        else:
            print("无效选择，请重新选择.")
    except KeyboardInterrupt:
        print("\n程序被用户中断.")
        exit()


def main():
    try:
        while True:
            print_menu()
            choice = input("PS>")
            perform_action(choice)
    except KeyboardInterrupt:
        print("\n程序已退出.")


def oneClickFingerprintRecognition():
    try:
        cmsFingerprintRecognition()
    except KeyboardInterrupt:
        print("\n程序已退出.")


def crack_wifi_main():
    """
    执行一键破解wifi.
    """
    try:
        crack_wifi()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


def crack_wifihandshake():
    try:
        crack_wifi_handshake()
    except KeyboardInterrupt:
        print("\n程序被中断.")
        exit()


if __name__ == "__main__":
    main()
