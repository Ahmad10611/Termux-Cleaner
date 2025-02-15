import os
import shutil
import subprocess

# لیست مسیرهای کش برای پاک‌سازی
cache_dirs = [
    "/data/data/com.termux/cache/",
    "/storage/emulated/0/Android/data/*/cache/",
    "/storage/emulated/0/Android/data/*/files/.thumbnails/",
    "/storage/emulated/0/DCIM/.thumbnails/",
    "/storage/emulated/0/Download/.tmp/",
    "/storage/emulated/0/Pictures/.thumbnails/",
    "/storage/emulated/0/Android/data/com.android.gallery3d/cache/",
    "/storage/emulated/0/MIUI/debug_log/",
    "/storage/emulated/0/tencent/MicroMsg/xlog/",
    "/storage/emulated/0/tencent/MicroMsg/cache/",
    "/storage/emulated/0/LOST.DIR/",
    "/storage/emulated/0/.trash/",
]

# لیست فایل‌های بزرگ و لاگ‌های سیستمی که باید حذف شوند
large_files = [
    "/storage/emulated/0/Download/*.log",
    "/storage/emulated/0/*.tmp",
    "/storage/emulated/0/*.bak",
    "/storage/emulated/0/*.old",
    "/storage/emulated/0/*.dmp",
    "/storage/emulated/0/*.apk",
    "/storage/emulated/0/Android/data/*/cache/*.log"
]

# بررسی و نصب پیش‌نیازها
def install_requirements():
    print("[⚡] بررسی و نصب پیش‌نیازهای Termux...")

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

# تابع حذف فایل‌های بزرگ غیرضروری
def clean_large_files():
    print("[⚡] حذف فایل‌های بزرگ و بی‌استفاده...")
    for file_pattern in large_files:
        os.system(f"rm -rf {file_pattern}")

# آزادسازی فضای ذخیره‌سازی
def free_storage():
    print("[⚡] در حال حذف فایل‌های بیهوده سیستم...")
    os.system("rm -rf /storage/emulated/0/Android/data/*/cache/")
    os.system("rm -rf /storage/emulated/0/Android/data/*/files/.thumbnails/")
    os.system("rm -rf /storage/emulated/0/Download/*.log")
    os.system("rm -rf /storage/emulated/0/*.tmp")

# پاک‌سازی فایل‌های بی‌استفاده ترمیکس
def clean_termux():
    print("[⚡] پاک‌سازی کش و لاگ‌های Termux...")
    os.system("rm -rf $HOME/.cache/")
    os.system("rm -rf $HOME/.termux/boot/")
    os.system("rm -rf $HOME/.termux/tasker/")
    os.system("rm -rf $HOME/.termux/config")

# نمایش فضای خالی و وضعیت حافظه داخلی
def check_storage():
    print("\n📊 وضعیت فضای ذخیره‌سازی قبل از پاک‌سازی:")
    os.system("df -h /storage/emulated/0")

# اجرای فرآیند پاک‌سازی
def clean_system():
    print("\n🚀 شروع پاک‌سازی کش و فایل‌های اضافی...\n")

    check_storage()

    for directory in cache_dirs:
        clean_directory(directory)

    clean_large_files()
    free_storage()
    clean_termux()

    print("\n✅ پاک‌سازی کامل شد! گوشی شما اکنون سریع‌تر است.\n")

    check_storage()

# اجرای اسکریپت
if __name__ == "__main__":
    install_requirements()
    clean_system()
