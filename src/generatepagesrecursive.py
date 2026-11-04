import os

from generatepage import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, file)

        if os.path.isfile(content_path) and content_path.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, file.replace(".md", ".html"))
            generate_page(content_path, template_path, dest_path, basepath)
        elif os.path.isdir(content_path):
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(content_path, template_path, dest_path, basepath)



