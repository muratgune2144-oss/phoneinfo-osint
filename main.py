from phonebul import get_city_from_number
from phone_osint import run_osint
import sys

def print_banner():
    print(r"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║     ███████╗ ██████╗ ███╗   ██╗███╗   ██╗██╗███████╗           ║
║     ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██║██╔════╝           ║
║     ███████╗██║   ██║██╔██╗ ██║██╔██╗ ██║██║███████╗           ║
║     ╚════██║██║   ██║██║╚██╗██║██║╚██╗██║██║╚════██║           ║
║     ███████║╚██████╔╝██║ ╚████║██║ ╚████║██║███████║           ║
║     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝           ║
║                                                                ║
║         🔎 TELEFON NUMARASI OSINT ARAŞTIRMA ARACI 🔍          ║
╚════════════════════════════════════════════════════════════════╝
""")

def show_menu():
    print("\n📲 Seçenekler:")
    print("1 - Numaranın şehir bilgilerini tahmin et")
    print("2 - Web üzerinde isim/e-posta bilgisi ara")
    print("3 - Her ikisini yap")
    print("0 - Çıkış\n")

def main():
    print_banner()

    while True:
        show_menu()
        secim = input("➡️ Seçiminiz: ").strip()

        if secim == "1":
            num = input("📞 Numara (+90 ile): ").strip()
            print(get_city_from_number(num))

        elif secim == "2":
            num = input("📞 Numara (+90 ile): ").strip()
            run_osint(num)

        elif secim == "3":
            num = input("📞 Numara (+90 ile): ").strip()
            print(get_city_from_number(num))
            print()
            run_osint(num)

        elif secim == "0":
            print("👋 Çıkılıyor...")
            sys.exit()

        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    main()
