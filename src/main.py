from generate_html import generate_pages_recursive
from copy_directory_content import dir_copy_all
import sys


def main(basepath = "/"):
    print(f"basepath is: `{basepath}`")
    static_source = "./static"
    md_soruce = "./content"
    dest = "./docs"
    html_template = "./template.html"
    dir_copy_all(static_source, dest)
    generate_pages_recursive(md_soruce,html_template,dest,basepath)
        
if __name__ == "__main__":
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
        main(basepath)
    else:
        main()