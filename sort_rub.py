import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor


def copy_file_to_extension_folder(src_file, target_root):
    extension = os.path.splitext(src_file)[1][1:]
    if extension == "":
        extension = "no_extension"
    target_dir = os.path.join(target_root, extension)
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, os.path.basename(src_file))
    shutil.copy(src_file, target_file)
    print(f"the file {src_file} was moved to {target_file}")


def process_directory(directory, target_root):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                src_file = os.path.join(root, file)
                executor.submit(copy_file_to_extension_folder, src_file, target_root)


if __name__ == "__main__":
    print("The movement started")
    if len(sys.argv) < 3:
        print("python sort_rub.py ./In ./Out")
        sys.exit(1)

    source_dir = sys.argv[1]
    target_dir = sys.argv[2]

    print(f"Start from {source_dir} to {target_dir}")
    process_directory(source_dir, target_dir)
    print("The movement finished")
