import os
import shutil

# List of cache directories to clean
CACHE_DIRS = [
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

# Function to install required packages only if missing
def install_requirements():
    print("[⚡] Checking and installing required packages...")

    # Check and install Python
    if not shutil.which("python"):
        os.system("pkg install python -y")

    # Check and install Termux API
    if not shutil.which("termux-info"):
        os.system("pkg install termux-api -y")

# Function to clean directories
def clean_directory(path):
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f"[✅] Deleted: {path}")
        except Exception as e:
            print(f"[❌] Error deleting {path}: {e}")

# Function to free up storage
def free_storage():
    print("[⚡] Removing unnecessary system files...")
    os.system("rm -rf /storage/emulated/0/Android/data/*/cache/")
    os.system("rm -rf /storage/emulated/0/Android/data/*/files/.thumbnails/")
    os.system("rm -rf /storage/emulated/0/Download/*.log")
    os.system("rm -rf /storage/emulated/0/Pictures/*.tmp")

# Function to clean Termux cache and logs
def clean_termux():
    print("[⚡] Cleaning Termux cache and logs...")
    os.system("rm -rf $HOME/.cache/")
    os.system("rm -rf $HOME/.termux/boot/")
    os.system("rm -rf $HOME/.termux/tasker/")
    os.system("rm -rf $HOME/.termux/config")

# Main function to execute cleaning process
def clean_system():
    print("\n🚀 Starting system cleaning...\n")
    
    for directory in CACHE_DIRS:
        clean_directory(directory)

    free_storage()
    clean_termux()

    print("\n✅ Cleaning completed! Your phone is now faster.\n")

# Run script
if __name__ == "__main__":
    install_requirements()
    clean_system()
