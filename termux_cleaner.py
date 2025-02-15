import os
import shutil
import subprocess

# لیست مسیرهای کش برای پاک‌سازی
cache_dirs = [
    "/data/data/com.termux/cache/",
    "/storage/emulated/0/Android/data/com.android.chrome/cache/",
    "/storage/emulated/0/Android/data/com.instagram.android/cache/",
    "/storage/emulated/0/Android/data/com.whatsapp/cache/",
    "/storage/emulated/0/Android/data/com.facebook.katana/cache/",
    "/storage/emulated/0/Android/data/com.google.android.youtube/cache/",
    "/storage/emulated/0/DCIM/.thumbnails/",
    "/storage/emulated/0/Download/.tmp/",
    "/storage/emulated/0/Android/data/com.android.gallery3d/cache/"
]

# بررسی و نصب پیش‌نیازها
def install_requirements():
    print("[⚡] بررسی و نصب پیش‌نیازهای Termux...")

    # بررسی نصب بودن پایتون
    if not shutil.which("python"):
        os.system("pkg install python -y")

    # بررسی نصب بودن termux-api
    if not shutil.which("termux-battery-status"):
        os.system("pkg install termux-api -y")

# تابع حذف دایرکتوری‌ها
def clean_directory(path):
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"[✅] حذف شد: {path}")
        except Exception as e:
            print(f"[❌] خطا در حذف {path}: {e}")

# آزادسازی فضای ذخیره‌سازی
def free_storage():
    print("[⚡] در حال حذف فایل‌های بیهوده سیستم...")
    os.system("rm -rf /storage/emulated/0/Android/data/*/cache/")
    os.system("rm -rf /storage/emulated/0/Android/data/*/files/.thumbnails/")
    os.system("rm -rf /storage/emulated/0/Download/*.log")
    os.system("rm -rf /storage/emulated/0/Pictures/*.tmp")

# پاک‌سازی فایل‌های بی‌استفاده ترمیکس
def clean_termux():
    print("[⚡] پاک‌سازی کش و لاگ‌های Termux...")
    os.system("rm -rf $HOME/.cache/")
    os.system("rm -rf $HOME/.termux/boot/")
    os.system("rm -rf $HOME/.termux/tasker/")
    os.system("rm -rf $HOME/.termux/config")
    
# نمایش وضعیت باتری برای بررسی سلامت دستگاه
def check_battery():
    print("[⚡] در حال بررسی وضعیت باتری...")
    os.system("termux-battery-status")

# اجرای فرآیند پاک‌سازی
def clean_system():
    print("\n🚀 شروع پاک‌سازی کش و فایل‌های اضافی...\n")
    
    for directory in cache_dirs:
        clean_directory(directory)

    free_storage()
    clean_termux()
    check_battery()

    print("\n✅ پاک‌سازی کامل شد! گوشی شما اکنون سریع‌تر است.\n")

# اجرای اسکریپت
if __name__ == "__main__":
    install_requirements()
    clean_system()
