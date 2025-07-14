from generate_html import generate_pages_recursive
from copy_directory_content import dir_copy_all


def main():
    static_source = "./static"
    md_soruce = "./content"
    dest = "./public"
    html_template = "./template.html"
    dir_copy_all(static_source, dest)
    generate_pages_recursive(md_soruce,html_template,dest)
        
if __name__ == "__main__":
    main()