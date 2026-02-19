import os
import socket

# স্ক্রিন পরিষ্কার করার জন্য ফাংশন
def clear_screen():
    os.system('clear')

# তোমার সুন্দর ব্যানার
def show_banner():
    clear_screen()
    print("\033[1;31m" + "="*50) # লাল রঙ (ANSI code)
    print("""
    ██████╗ ███████╗██████╗     ██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██╔════╝██╔══██╗    ██║  ██║██╔══██╗╚══██╔══╝
    ██████╔╝█████╗  ██║  ██║    ███████║███████║   ██║   
    ██╔══██╗██╔══╝  ██║  ██║    ██╔══██║██╔══██║   ██║   
    ██║  ██║███████╗██████╔╝    ██║  ██║██║  ██║   ██║   
    ╚═╝  ╚═╝╚══════╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    """)
    print("           CREATED BY: [Md Sazid]")
    print("           VERSION: 1.0 (RED HAT EDITION)")
    print("="*50 + "\033[0m")

# মেনু অপশন
def show_menu():
    print("\n[1] Start Network Scanner")
    print("[2] Developer Info")
    print("[3] Exit")
    print("-" * 50)

# স্ক্যানার ফাংশন
def start_scanner():
    target = input("\nEnter Target IP (e.g., 192.168.0.1): ")
    print(f"\nScanning {target}... Please wait.")
    try:
        for port in range(1, 101):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"-> Port {port}: OPEN")
            s.close()
    except:
        print("\nAn error occurred!")
    input("\nPress Enter to return to menu...")

# মেইন লজিক
while True:
    show_banner()
    show_menu()
    choice = input("Select an option: ")

    if choice == '1':
        start_scanner()
    elif choice == '2':
        print("\n--- DEVELOPER INFO ---")
        print("Name: [Md Sazid]")
        print("Role: Red Hat Hacker")
        print("Goal: Cybersecurity Learning")
        input("\nPress Enter to return to menu...")
    elif choice == '3':
        print("\nGoodbye! Happy Hacking.")
        break
    else:
        print("\nInvalid choice! Try again.")
