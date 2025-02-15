import os
import shutil
import subprocess

# لیست دایرکتوری‌هایی که باید پاک شوند
cache_dirs = [
    "/data/data/com.termux/cache/",
    "/data/data/com.android.chrome/cache/",
    "/data/data/com.instagram.android/cache/",
    "/data/data/com.whatsapp/cache/",
    "/data/data/com.facebook.katana/cache/",
    "/data/data/com.android.vending/cache/",
    "/data/data/com.google.android.youtube/cache/",
    "/storage/emulated/0/Android/data/com.android.chrome/cache/",
    "/storage/emulated/0/Android/data/com.instagram.android/cache/",
    "/storage/emulated/0/Android/data/com.whatsapp/cache/",
    "/storage/emulated/0/Android/data/com.facebook.katana/cache/",
    "/storage/emulated/0/Android/data/com.google.android.youtube/cache/"
]

# لیست فایل‌های موقت
temp_dirs = [
    "/data/local/tmp/",
    "/storage/emulated/0/DCIM/.thumbnails/",
    "/storage/emulated/0/Download/.tmp/",
    "/storage/emulated/0/Android/data/com.android.gallery3d/cache/"
]

# تابع حذف دایرکتوری‌ها
def clean_directory(path):
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"[✅] حذف شد: {path}")
        except Exception as e:
            print(f"[❌] خطا در حذف {path}: {e}")
    else:
        print(f"[⚡] یافت نشد: {path}")

# تابع نصب پیش‌نیازها
def install_requirements():
    print("[⚡] در حال نصب پیش‌نیازهای Termux...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install python -y")
    os.system("pkg install termux-api -y")

# تابع آزادسازی حافظه رم
def free_memory():
    print("[⚡] در حال آزادسازی حافظه رم...")
    os.system("sync; echo 3 > /proc/sys/vm/drop_caches")

# اجرای تمیزکاری
def clean_system():
    print("\n🚀 شروع پاک‌سازی کش و فایل‌های اضافی...\n")
    for directory in cache_dirs + temp_dirs:
        clean_directory(directory)

    free_memory()
    print("\n✅ پاک‌سازی کامل شد! گوشی شما اکنون سریع‌تر است.\n")

# اجرای اسکریپت
if __name__ == "__main__":
    install_requirements()
    clean_system()
