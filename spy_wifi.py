import os
import subprocess
import platform
import sys
import time

# Color Palette (Premium Standard)
R = '\033[31m'  # Red
G = '\033[32m'  # Green
Y = '\033[33m'  # Yellow
C = '\033[36m'  # Cyan
W = '\033[0m'   # White
B = '\033[1m'   # Bold

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    # ASCII Art: Hacker Face + WiFi Symbol
    print(f"""{C}
      .---.        {W}__________________________________{C}
     /     \      {W}|                                  |{C}
    | () () |     {W}|      {B}SPY-E & 123TOOL{W}             |{C}
     \  ^  /      {W}|   {G}WIFI HACKER - PREMIUM TOOL{W}     |{C}
      |||||       {W}|__________________________________|{C}
      |||||             {Y}V.1.0 - PROJECT NAGA{C}

             .-------.
           .'  ___    '.
          /  .'   '.    \\
         |  /  {W}.-.{C}  \    |      {G} ((( WIFI ))){C}
         |  | {W}(   ){C} |    |     {G}      |{C}
         |  \  {W}'-'{C}  /    |     {G}    _|_|_ {C}
          \  '.___.'    /
           '._______.'
{W}  ---------------------------------------------------------
  {G}[+] Developer : Rolandino
  [+] Brand     : SPY-E / 123Tool
  [+] Platform  : {platform.system()} {platform.release()}
  ---------------------------------------------------------
    """)

def check_root():
    if os.name != 'nt' and os.geteuid() != 0:
        print(f"{R}[!] ERROR: Akses Ditolak! Gunakan 'sudo python3 spy_wifi.py'{W}")
        sys.exit()

def run_cmd(cmd):
    try:
        return subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"{R}[!] Terjadi kesalahan: {e}{W}")

def install_driver():
    print(f"{Y}[*] Mempersiapkan lingkungan sistem...{W}")
    if os.name == 'nt':
        print(f"{R}[!] Fitur instalasi otomatis RTL8188FU hanya untuk Linux/Kali.{W}")
    else:
        print(f"{C}[*] Mengunduh dependensi driver...{W}")
        run_cmd("sudo apt-get update")
        run_cmd("sudo apt-get install build-essential git dkms linux-headers-$(uname -r) -y")
        
        if not os.path.exists("rtl8188fu"):
            run_cmd("git clone https://github.com/kelebek333/rtl8188fu")
        
        os.chdir("rtl8188fu")
        print(f"{C}[*] Memasang Driver ke Sistem (DKMS)...{W}")
        run_cmd("sudo dkms install .")
        run_cmd("sudo cp ./firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/")
        print(f"{G}[+] BERHASIL! Driver RTL8188FU telah terpasang.{W}")
        print(f"{Y}[!] Disarankan REBOOT perangkat Anda sekarang.{W}")

def monitor_mode():
    print(f"{C}--- AKTIVASI MONITOR MODE ---{W}")
    run_cmd("nmcli radio wifi off") # Mematikan konflik WiFi
    run_cmd("sudo rfkill unblock wifi")
    iface = input(f"{C}[?] Masukkan Interface (contoh: wlan1): {W}")
    print(f"{Y}[*] Mematikan proses pengganggu (Airmon-ng check kill)...{W}")
    run_cmd("sudo airmon-ng check kill")
    print(f"{Y}[*] Mengubah {iface} ke Monitor Mode...{W}")
    run_cmd(f"sudo airmon-ng start {iface}")
    print(f"{G}[+] SELESAI! Interface Anda kini dalam mode monitor.{W}")

def scan_target():
    print(f"{C}--- SCANNING JARINGAN (2.4GHz) ---{W}")
    iface = input(f"{C}[?] Masukkan Monitor Interface (contoh: wlan1mon): {W}")
    print(f"{G}[*] Memulai pemindaian... Tekan CTRL+C untuk berhenti.{W}")
    time.sleep(2)
    try:
        run_cmd(f"sudo airodump-ng {iface}")
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Pemindaian dihentikan.{W}")

def capture_handshake():
    print(f"{C}--- HANDSHAKE CAPTURE ASSISTANT ---{W}")
    iface = input(f"{C}[?] Monitor Interface: {W}")
    bssid = input(f"{C}[?] Target BSSID (MAC Address): {W}")
    chan  = input(f"{C}[?] Target Channel: {W}")
    file  = input(f"{C}[?] Nama File Output: {W}")
    
    print(f"{G}[*] Memulai Penangkapan... Biarkan sampai 'WPA Handshake' muncul di pojok kanan atas.{W}")
    run_cmd(f"sudo airodump-ng -c {chan} --bssid {bssid} -w {file} {iface}")

def main():
    while True:
        clear_screen()
        banner()
        print(f"[{G}01{W}] {B}Install Driver RTL8188FU{W} (ANT AE200M/Murah)")
        print(f"[{G}02{W}] {B}Aktifkan Monitor Mode{W}")
        print(f"[{G}03{W}] {B}Pindai Target WiFi{W} (Airodump-ng Scan)")
        print(f"[{G}04{W}] {B}Capture Handshake{W} (Target Spesifik)")
        print(f"[{G}05{W}] {B}Buka Dokumentasi 123Tool{W}")
        print(f"[{R}00{W}] Keluar")
        
        choice = input(f"\n{C}SPY-E-SHELL > {W}")
        
        if choice == '1' or choice == '01':
            install_driver()
            input(f"\n{Y}Tekan Enter untuk kembali ke Menu...{W}")
        elif choice == '2' or choice == '02':
            monitor_mode()
            input(f"\n{Y}Tekan Enter untuk kembali ke Menu...{W}")
        elif choice == '3' or choice == '03':
            scan_target()
            input(f"\n{Y}Tekan Enter untuk kembali ke Menu...{W}")
        elif choice == '4' or choice == '04':
            capture_handshake()
            input(f"\n{Y}Tekan Enter untuk kembali ke Menu...{W}")
        elif choice == '5' or choice == '05':
            print(f"{G}[*] Mengalihkan ke database 123Tool...{W}")
            time.sleep(1)
            print(f"{C}[i] Kunjungi GitHub: github.com/rolandino-spy-e{W}")
            input(f"\nTekan Enter...")
        elif choice == '0' or choice == '00':
            print(f"{Y}Sistem Dimatikan. Sampai Jumpa, Peretas!{W}")
            break
        else:
            print(f"{R}[!] Pilihan Tidak Valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    check_root()
    main()
