import os
import shutil

# List of cache directories
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

# List of unnecessary large files
large_files = [
    "/storage/emulated/0/Download/*.log",
    "/storage/emulated/0/*.tmp",
    "/storage/emulated/0/*.bak",
    "/storage/emulated/0/*.old",
    "/storage/emulated/0/*.dmp",
    "/storage/emulated/0/*.apk",
    "/storage/emulated/0/Android/data/*/cache/*.log"
]

# Automatically grant storage permission
def request_storage_permission():
    print("\n[⚡] Granting storage access...")
    os.system("termux-setup-storage")

# Install necessary Termux packages
def install_requirements():
    print("\n[⚡] Installing required packages...")
    os.system("pkg update -y && pkg upgrade -y")
    os.system("pkg install termux-api -y")

# Remove files from directories
def clean_directory(path):
    if os.path.exists(path):
        os.system(f"find {path} -type f -delete")
        print(f"[✅] Cleaned: {path}")

# Remove large unnecessary files
def clean_large_files():
    print("\n[⚡] Removing large unnecessary files...")
    for file_pattern in large_files:
        os.system(f"rm -rf {file_pattern}")

# Free up storage space
def free_storage():
    print("\n[⚡] Deleting junk system files...")
    os.system("rm -rf /storage/emulated/0/Android/data/*/cache/")
    os.system("rm -rf /storage/emulated/0/Android/data/*/files/.thumbnails/")
    os.system("rm -rf /storage/emulated/0/Download/*.log")
    os.system("rm -rf /storage/emulated/0/*.tmp")

# Clean Termux cache and logs
def clean_termux():
    print("\n[⚡] Cleaning Termux logs...")
    os.system("rm -rf $HOME/.cache/")
    os.system("rm -rf $HOME/.termux/boot/")
    os.system("rm -rf $HOME/.termux/tasker/")
    os.system("rm -rf $HOME/.termux/config")

# Show storage space before and after cleanup
def check_storage():
    print("\n📊 Checking storage status...")
    os.system("df -h /storage/emulated/0")

# Run cleaning process once (no delay, no loop)
def clean_system():
    request_storage_permission()
    install_requirements()

    print("\n🚀 Starting cleanup...\n")

    check_storage()

    for directory in cache_dirs:
        clean_directory(directory)

    clean_large_files()
    free_storage()
    clean_termux()

    print("\n✅ Cleanup completed! Your phone is now optimized.\n")

    check_storage()

# Run script
if __name__ == "__main__":
    clean_system()
