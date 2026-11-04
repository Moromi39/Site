import os
import shutil
from generatepage import generate_page
from textnode import TextNode, TextType


def main():
    copy_static("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_recursive(src, dst)

def copy_recursive(src, dst):
    for file in os.listdir(src):
        src_path = os.path.join(src, file)
        dst_path = os.path.join(dst, file)
        if os.path.isfile(src_path):
            print(f"Copying {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        if os.path.isdir(src_path):
            os.mkdir(dst_path)
            copy_recursive(src_path, dst_path)






if __name__ == "__main__":
    main()
