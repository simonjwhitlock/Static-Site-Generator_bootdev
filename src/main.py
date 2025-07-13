from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node,split_nodes_delimiter,split_nodes_image,split_nodes_link,text_to_textnodes
from regex import extract_markdown_images,extract_markdown_links
from markdownblock import markdown_to_blocks,block_to_block_type
from markdowntohtml import markdown_to_html_node


def main():
    markdown = """###### Big **BOLD** heading with _EMPASIS_    

# here lies the ashes of sanity

_abstarcte of a stupid aritcal_

>this is a multi line
>quote block
>by a pretentious arse

```
for some _reason_ they
**wrote some damn code!**
```



- to make stuff sureal they wrote
- a dumb list too

1. and an ordered one
2. because why the hell not


"""
    nodes = markdown_to_html_node(markdown)
    print(nodes)
    print("!!!!!!!!!!!!converting to html!!!!!!!!!!!!!!!!!")
    html = nodes.to_html()
    print(html)
        
if __name__ == "__main__":
    main()