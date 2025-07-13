from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node,split_nodes_delimiter,split_nodes_image,split_nodes_link,text_to_textnodes
from regex import extract_markdown_images,extract_markdown_links
from markdownblock import markdown_to_blocks,block_to_block_type
from markdowntohtml import markdown_to_html_node

def main():
    block = """```
This is a code block
```"""
    block_type = block_to_block_type(block)
    print(block_type)


def main_ign():
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

```
This is text that _should_ remain
the **same** even with inline stuff
```

- This is the first list item in a list block
- This is a list item
- This is another list item"""
    nodes = markdown_to_html_node(markdown)
    print(nodes)
    print("!!!!!!!!!!!!converting to html!!!!!!!!!!!!!!!!!")
    html = nodes.to_html()
    print(html)
        
if __name__ == "__main__":
    main()