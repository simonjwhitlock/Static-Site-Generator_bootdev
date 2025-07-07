from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node


def main():
    new_textnode = TextNode("This is some anchor text", TextType.TEXT)
    print("help")
    print(new_textnode.__repr__())
    converted = text_node_to_html_node(new_textnode)
    print(converted.to_html())
    
    
if __name__ == "__main__":
    main()