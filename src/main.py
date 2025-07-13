from generate_html import generate_page, extract_title
from copy_directory_content import dir_copy_all


def main():
    source = "./static"
    dest = "./public"
    print(f"source: {source}, dest: {dest}")
    dir_copy_all(source, dest)
    
    print(generate_page("./content/index.md","./template.html","./public/index.html"))
        
if __name__ == "__main__":
    main()