import os
from tools.planes import track_planes
from effects.visual import visual_noise
from effects.audio import play_sound

def main():
    os.system("clear")
    print("🧠 وحدة مراقبة استخباراتية - CLI")
    print("----------------------------------")
    print("1. تتبع طائرات")
    print("2. تشغيل تشويش بصري")
    print("3. تشغيل صوت إنذار")
    print("4. فتح واجهة QR من الهاتف")
    print("0. خروج")

    while True:
        choice = input("\nاختر الخيار: ")
        if choice == "1":
            country = input("أدخل اسم الدولة: ")
            track_planes(country)
        elif choice == "2":
            visual_noise()
        elif choice == "3":
            play_sound()
        elif choice == "4":
            os.system("python3 web/app.py")
        elif choice == "0":
            print("🛑 إنهاء البرنامج.")
            break
        else:
            print("❌ خيار غير معروف.")

if __name__ == "__main__":
    main()
