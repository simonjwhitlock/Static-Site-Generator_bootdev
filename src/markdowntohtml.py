from markdownblock import BlockType,markdown_to_blocks,block_to_block_type
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_to_textnodes,text_node_to_html_node

def markdown_to_html_node(markdown):
    print("!!!!!!!!! INPUT !!!!!!!!!!!!")
    print(markdown)
    md_blocks = markdown_to_blocks(markdown)
    print("!!!!!!!!! SPLIT TO BLOCKS !!!!!!!!!!!!")
    print(md_blocks)
    print("!!!!!!!!!  !!!!!!!!!!!!")
    parent_child_nodes = []
    for block in md_blocks:
        block_tag = ""
        match block_to_block_type(block):
            case BlockType.PARA:
                block_tag = "p"
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.HEAD:
                split = block.split()
                block_tag = f"h{len(split[0])}"
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.CODE:
                block_tag = "code"
                parent_child_nodes.append(LeafNode(tag = block_tag, value = block))
            case BlockType.QUOTE:
                block_tag = "i"
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.LISTU:
                block_tag = ""
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
            case BlockType.LISTO:
                block_tag = ""
                children= text_to_children(block)
                parent_child_nodes.append(ParentNode(tag=block_tag,children=children))
                
    parent_html_node = ParentNode("div",parent_child_nodes)
    return parent_html_node
            
        
        
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes