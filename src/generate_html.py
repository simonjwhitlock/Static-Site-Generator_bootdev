import os
from markdowntohtml import markdown_to_html_node
from markdownblock import markdown_to_blocks

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_index = os.listdir(dir_path_content)
    for path in dir_index:
        source = os.path.join(dir_path_content, path)
        dest = os.path.join(dest_dir_path,path)
        if os.path.isdir(source):
            if not os.path.exists(dest):
                os.mkdir(dest)
            generate_pages_recursive(source,template_path,dest)
        if os.path.isfile(source):
            if path.split(".")[-1] == "md":
                dest = os.path.splitext(dest)[0]+".html"
                generate_page(source,template_path,dest)
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(from_path) or not os.path.isfile(from_path):
        raise Exception(f"from file: {from_path} does not exist")
    if not os.path.exists(template_path) or not os.path.isfile(template_path):
        raise Exception(f"template file: {template_path} does not exist")
    with open(from_path, 'r') as file:
        md = file.read()
        
    title = extract_title(md)
    print(title)
    html_nodes = markdown_to_html_node(md)
    html_content = html_nodes.to_html()
    
    with open(template_path, 'r') as template:
        html = template.read()
        
    html = html.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    with open(dest_path, 'w') as dest:
        dest.write(html)
    
def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        split = block.split(" ", 1)
        if split[0] == "#":
            return split[1].strip()
    raise Exception("no heading 1 in markdown")