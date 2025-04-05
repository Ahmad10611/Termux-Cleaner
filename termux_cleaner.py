#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import shutil

def format_size(bytes_amount):
    """Convert bytes to human-readable format."""
    if bytes_amount >= 1024**3:
        return f"{bytes_amount/1024**3:.2f} GB"
    elif bytes_amount >= 1024**2:
        return f"{bytes_amount/1024**2:.2f} MB"
    elif bytes_amount >= 1024:
        return f"{bytes_amount/1024:.2f} KB"
    else:
        return f"{bytes_amount} B"

# مسیر حافظه داخلی (اصلی‌ترین مسیر shared storage)
BASE_PATH = "/storage/emulated/0"

# اطمینان از وجود مسیر پایه
if not os.path.isdir(BASE_PATH):
    print("خطا: مسیر حافظه داخلی در دسترس نیست. مطمئن شوید termux-setup-storage را اجرا کرده‌اید.")
    exit(1)

# دریافت وضعیت حافظه قبل از پاکسازی
total, used, free = shutil.disk_usage(BASE_PATH)
used_before = total - free
free_before = free

print(f"حافظه قبل از پاکسازی – استفاده‌شده: {format_size(used_before)} ، آزاد: {format_size(free_before)}")

removed_any = False  # نشانگر حذف شدن حداقل یک فایل/پوشه

# 1. پاک کردن محتویات کش تمامی برنامه‌ها در Android/data/*/cache
cache_dirs = glob.glob(os.path.join(BASE_PATH, "Android", "data", "*", "cache"))
for cache_dir in cache_dirs:
    if os.path.isdir(cache_dir):
        # پیمایش تمامی فایل‌ها و پوشه‌های داخل پوشه کش
        for root, dirs, files in os.walk(cache_dir, topdown=False):
            # حذف فایل‌های داخل پوشه کش
            for filename in files:
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    removed_any = True
                    print(f"✓ حذف فایل کش: {file_path}")
                except Exception as e:
                    print(f"✗ خطا در حذف فایل: {file_path} -> {e}")
            # حذف پوشه‌های خالی باقی‌مانده داخل کش
            for dirname in dirs:
                dir_path = os.path.join(root, dirname)
                try:
                    os.rmdir(dir_path)
                    removed_any = True
                    print(f"✓ حذف پوشه خالی: {dir_path}")
                except Exception as e:
                    # در صورت عدم امکان حذف (مثلاً پوشه غیرفرصت)، پیام خطا چاپ می‌شود
                    print(f"✗ خطا در حذف پوشه: {dir_path} -> {e}")

# 2. حذف پوشه‌های کش بندانگشتی (DCIM/.thumbnails و Pictures/.thumbnails)
thumb_dirs = [
    os.path.join(BASE_PATH, "DCIM", ".thumbnails"),
    os.path.join(BASE_PATH, "Pictures", ".thumbnails")
]
for tdir in thumb_dirs:
    if os.path.isdir(tdir):
        try:
            shutil.rmtree(tdir)  # حذف کل پوشه بندانگشتی‌ها
            removed_any = True
            print(f"✓ حذف پوشه بندانگشتی‌ها: {tdir}")
        except Exception as e:
            print(f"✗ خطا در حذف {tdir}: {e}")

# 3. حذف پوشه LOST.DIR (یا محتوای آن) اگر وجود داشته باشد
lost_dir = os.path.join(BASE_PATH, "LOST.DIR")
if os.path.isdir(lost_dir):
    try:
        shutil.rmtree(lost_dir)
        removed_any = True
        print(f"✓ حذف پوشه LOST.DIR: {lost_dir}")
    except Exception as e:
        print(f"✗ خطا در حذف {lost_dir}: {e}")

# 4. حذف پوشه سطل زباله (.trash) اگر وجود داشته باشد
trash_dir = os.path.join(BASE_PATH, ".trash")
if os.path.isdir(trash_dir):
    try:
        shutil.rmtree(trash_dir)
        removed_any = True
        print(f"✓ حذف پوشه .trash: {trash_dir}")
    except Exception as e:
        print(f"✗ خطا در حذف {trash_dir}: {e}")

# 5. حذف پوشه دانلودهای موقت (Download/.tmp) اگر وجود داشته باشد
tmp_dl_dir = os.path.join(BASE_PATH, "Download", ".tmp")
if os.path.isdir(tmp_dl_dir):
    try:
        shutil.rmtree(tmp_dl_dir)
        removed_any = True
        print(f"✓ حذف پوشه دانلود موقت: {tmp_dl_dir}")
    except Exception as e:
        print(f"✗ خطا در حذف {tmp_dl_dir}: {e}")

# 6. جست‌وجوی سراسری و حذف فایل‌ها با پسوندهای غیرضروری مشخص‌شده
patterns = ["*.log", "*.tmp", "*.bak", "*.old", "*.dmp", ".thumbdata*"]
for pattern in patterns:
    for filepath in glob.glob(os.path.join(BASE_PATH, "**", pattern), recursive=True):
        if os.path.isfile(filepath) or os.path.islink(filepath):
            try:
                os.remove(filepath)
                removed_any = True
                print(f"✓ حذف فایل: {filepath}")
            except Exception as e:
                print(f"✗ خطا در حذف فایل: {filepath} -> {e}")

# 7. نمایش گزارش نهایی فضای حافظه پس از پاکسازی
total, used, free = shutil.disk_usage(BASE_PATH)
used_after = total - free
free_after = free
freed_space = free_after - free_before

print(f"حافظه پس از پاکسازی – استفاده‌شده: {format_size(used_after)} ، آزاد: {format_size(free_after)}")
if freed_space >= 0:
    print(f"فضای آزاد شده: {format_size(freed_space)}")

# 8. در صورت عدم حذف هیچ فایل/پوشه‌ای، نمایش پیام مربوطه
if not removed_any:
    print("هیچ فایل یا کش اضافی برای پاکسازی یافت نشد.")
