import os
import shutil
import time

# لیست مسیرهای کش و فایل‌های بیهوده برای حذف
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

# لیست فایل‌های بیهوده و حجیم
large_files = [
    "/storage/emulated/0/Download/*.log",
    "/storage/emulated/0/*.tmp",
    "/storage/emulated/0/*.bak",
    "/storage/emulated/0/*.old",
    "/storage/emulated/0/*.dmp",
    "/storage/emulated/0/*.apk",
    "/storage/emulated/0/Android/data/*/cache/*.log"
]

# درخواست دسترسی به حافظه به‌صورت خودکار
def request_storage_permission():
    print("\n[⚡] Granting storage access...")
    os.system("termux-setup-storage && sleep 2")

# نصب پیش‌نیازها بدون توقف اسکریپت
def install_requirements():
    print("\n[⚡] Installing necessary Termux packages...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install termux-api -y")

# حذف محتویات پوشه‌ها بدون توقف
def clean_directory(path):
    if os.path.exists(path):
        os.system(f"find {path} -type f -delete")
        print(f"[✅] Cleaned: {path}")

# حذف فایل‌های بزرگ و بیهوده
def clean_large_files():
    print("\n[⚡] Removing large unnecessary files...")
    for file_pattern in large_files:
        os.system(f"rm -rf {file_pattern}")

# آزادسازی فضای ذخیره‌سازی
def free_storage():
    print("\n[⚡] Deleting junk system files...")
    os.system("rm -rf /storage/emulated/0/Android/data/*/cache/")
    os.system("rm -rf /storage/emulated/0/Android/data/*/files/.thumbnails/")
    os.system("rm -rf /storage/emulated/0/Download/*.log")
    os.system("rm -rf /storage/emulated/0/*.tmp")

# پاک‌سازی کش و لاگ‌های Termux
def clean_termux():
    print("\n[⚡] Cleaning Termux logs...")
    os.system("rm -rf $HOME/.cache/")
    os.system("rm -rf $HOME/.termux/boot/")
    os.system("rm -rf $HOME/.termux/tasker/")
    os.system("rm -rf $HOME/.termux/config")

# نمایش فضای ذخیره‌سازی
def check_storage():
    print("\n📊 Checking storage status...")
    os.system("df -h /storage/emulated/0")

# اجرای پیوسته بدون توقف
def clean_system():
    request_storage_permission()
    install_requirements()

    while True:
        print("\n🚀 Starting cleanup cycle...\n")

        check_storage()

        for directory in cache_dirs:
            clean_directory(directory)

        clean_large_files()
        free_storage()
        clean_termux()

        print("\n✅ Cleanup completed! Your phone is now optimized.\n")

        check_storage()

        print("\n⏳ Next cleanup in 5 minutes...")
        time.sleep(300)  # 5 دقیقه صبر می‌کند، سپس مجدداً اجرا می‌شود

# اجرای اسکریپت
if __name__ == "__main__":
    clean_system()
