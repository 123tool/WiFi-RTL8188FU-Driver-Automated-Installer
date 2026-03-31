# 🛰️ SPY-WiFi Tracker & Driver Installer
### [ Powered by SPY-E & 123Tool ]

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![OS](https://img.shields.io/badge/OS-Linux%20|%20Termux%20|%20Windows-orange.svg)

**SPY-WiFi** adalah tool otomatisasi untuk menginstal driver Chipset **RTL8188FU** (Ant Esports AE200M & Cheap WiFi Dongles) serta asisten penetrasi jaringan WiFi menggunakan suite Aircrack-ng.

---

## 🚀 Fitur Utama
* **Auto-Installer**: Menginstal driver RTL8188FU tanpa ribet (Fix "Interface not found").
* **Monitor Mode Enabler**: Mengubah mode Managed ke Monitor hanya dengan satu klik.
* **WiFi Scanner**: Memindai jaringan 2.4GHz di sekitar secara real-time.
* **Handshake Capture**: Membantu proses de-authentication dan penangkapan file WPA handshake.
* **Multi-Platform**: Support Kali Linux, Parrot OS, Ubuntu, dan Termux (Rooted).

---

## 🛠️ Persyaratan Sistem
Sebelum menjalankan script, pastikan Anda memiliki:
1. WiFi Adapter dengan Chipset **RTL8188FU**.
2. Akses **Root** atau **Sudo**.
3. Python 3.x terinstal.

---

## 📥 Instalasi & Penggunaan

### 🐧 Linux (Kali/Ubuntu/Parrot)
```bash
# Clone Repositori
git clone [https://github.com/123tool/WiFi-RTL8188FU-Driver-Automated-Installer.git](https://github.com/123tool/WiFi-RTL8188FU-Driver-Automated-Installer.git)
cd WiFi-RTL8188FU-Driver-Automated-Installer

# Jalankan Script
sudo python3 spy_wifi.py
