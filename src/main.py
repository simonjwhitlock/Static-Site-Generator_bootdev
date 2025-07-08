from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node,split_nodes_delimiter


def main():
    textnode_one = TextNode("this is a **bold** node", TextType.BOLD)
    textnode_two = TextNode("this is an **italic** node", TextType.ITALIC)
    textnode_three = TextNode("this is a **code** node", TextType.CODE)
    textnode_four = TextNode("this is a **link** node", TextType.LINK, "https://google.com")
    textnode_five = TextNode("this is a **image** node", TextType.IMAGE, "https://google.com")
    split_nodes = split_nodes_delimiter([textnode_one, textnode_two, textnode_three, textnode_four, textnode_five], "**", TextType.TEXT)
    print(split_nodes)
    
    
if __name__ == "__main__":
    main()