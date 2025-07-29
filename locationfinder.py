from pyfiglet import figlet_format
from termcolor import colored
import requests
import os
import socket
import time

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Main Banner
banner = figlet_format("NPTracerX", font="slant")
print(colored(banner, color="red"))

# Subtitle
print(colored("Night Panthers IPTracerX Tool", "magenta", attrs=["bold"]))
print(colored("Version: v2.0", "yellow"))
print(colored("Created by: npxarmy", "green"))
print(colored("Contact: jassonmiler363@gmail.com", "blue"))
print(colored("Author: Abuzar","yellow"))
print(colored("="*50, "white"))

# Main Menu
while True:
    print(colored("\nSelect an Option:", "cyan", attrs=["bold"]))
    print(colored("[1] IP Address Tracker", "green"))
    print(colored("[2] Show Local IP Address", "green"))
    print(colored("[3] About Tool", "green"))
    print(colored("[4] Exit", "red"))

    choice = input(colored("\nEnter your choice: ", "yellow"))

    if choice == "1":
        ip = input(colored("Enter the IP Address: ", "blue"))
        try:
            res = requests.get(f"http://ip-api.com/json/{ip}").json()

            if res["status"] == "fail":
                print(colored("❌ Invalid IP address or API error!", "red"))
            else:
                print(colored(f"\n📡 IP Address Info: {ip}", "yellow"))
                print(colored(f"🌍 Country       : {res['country']}"))
                print(colored(f"🏙️ City          : {res['city']}", "green"))
                print(colored(f"📡 ISP           : {res['isp']}", "blue"))
                print(colored(f"🧭 Latitude      : {res['lat']}", "yellow"))
                print(colored(f"🧭 Longitude     : {res['lon']}", "green"))
        except:
            print(colored("⚠️ Network error or connection issue.", "red"))

    elif choice == "2":
        try:
            local_ip = socket.gethostbyname(socket.gethostname())
            print(colored(f"\n🌐 Your Local IP Address is: {local_ip}", "cyan"))
        except:
            print(colored("⚠️ Unable to fetch local IP address.", "red"))

    elif choice == "3":
        print(colored("\n💡 About NPMT Tool", "magenta", attrs=["bold"]))
        print(colored("This tool is developed for ethical purposes only.", "white"))
        print(colored("You can use it to fetch geolocation of IPs, get your local IP, and more.", "white"))
        print(colored("Stay tuned for more tools in future updates!", "green"))

    elif choice == "4":
        print(colored("\nExiting... Goodbye 🐾", "red"))
        time.sleep(1)
        break

    else:
        print(colored("❗ Invalid option, try again.", "red"))

