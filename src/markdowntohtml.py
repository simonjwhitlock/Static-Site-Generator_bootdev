from markdownblock import BlockType,markdown_to_blocks,block_to_block_type
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_to_textnodes,text_node_to_html_node
from textnode import TextNode,TextType

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    parent_child_nodes = []
    for block in md_blocks:
        block_tag = ""
        match block_to_block_type(block):
            case BlockType.PARA:
                block_tag = "p"
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.HEAD:
                split = block.split(" ", 1)
                block_tag = f"h{len(split[0])}"
                children= text_to_children(split[1])
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.CODE:
                block_tag = "code"
                block_text = block.lstrip("`\n").rstrip("`")
                block_text_node = TextNode(block_text, TextType.CODE)
                children = [text_node_to_html_node(block_text_node)]
                parent_child_nodes.append(ParentNode(tag = "pre", children= children))
            case BlockType.QUOTE:
                block_tag = "blockquote"
                block_text = block.replace("> ","")
                children= text_to_children(block_text)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.LISTU:
                block_tag = "ul"
                children= lists_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.LISTO:
                block_tag = "ol"
                children= lists_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
                
    parent_html_node = ParentNode("div",parent_child_nodes)
    return parent_html_node
            
        
        
def text_to_children(text):
    raw_text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(raw_text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def lists_to_children(text):
    list_items = text.split("\n")
    html_nodes = []
    for item in list_items:
        item_text = item.split(" ", 1)[1]
        item_html_nodes = text_to_children(item_text)
        html_nodes.append(ParentNode(tag = "li", children=item_html_nodes))
    return html_nodes
            