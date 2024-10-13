import os
import shutil
import argparse

def recursive_copy_and_sort(src, dst):
    try:
        # Create the destination directory if it does not exist
        if not os.path.isdir(dst):
            os.makedirs(dst)
        
        for entry in os.listdir(src):
            src_path = os.path.join(src, entry)
            if os.path.isdir(src_path):
                # Recursively copy and sort files in subdirectories
                new_dst = os.path.join(dst, os.path.basename(src_path))
                recursive_copy_and_sort(src_path, new_dst)
            else:
                # Handle file sorting
                file_extension = os.path.splitext(entry)[1][1:].lower()  # Extract and normalize file extension
                ext_dir = os.path.join(dst, file_extension)
                if not os.path.isdir(ext_dir):
                    os.makedirs(ext_dir)
                shutil.copy2(src_path, ext_dir)
    except Exception as error:
        print(f"Error processing '{src}': {error}")

def run_copying():
    parser = argparse.ArgumentParser(description="Copy files recursively and sort them by file extension.")
    parser.add_argument("src", help="Source directory path")
    parser.add_argument("dst", nargs='?', default="dist", help="Destination directory path (default: 'dist')")
    args = parser.parse_args()
    
    src_dir = args.src
    dst_dir = args.dst
    
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return
    
    recursive_copy_and_sort(src_dir, dst_dir)
    print("Files have been successfully copied and sorted.")

if __name__ == "__main__":
    run_copying()
