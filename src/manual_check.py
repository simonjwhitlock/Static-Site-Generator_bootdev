from generate_html import generate_page, generate_pages_recursive, extract_title
from markdownblock import block_to_block_type, markdown_to_blocks
from markdowntohtml import markdown_to_html_node
from nodeconversion import text_to_textnodes,text_node_to_html_node

def main():
    source = "./content/blog/tom/index.md"
    md = "_An unpopular opinion, I know._"
    blocks = text_to_textnodes(md)
    print(blocks)
    
if __name__ == "__main__":
    main()