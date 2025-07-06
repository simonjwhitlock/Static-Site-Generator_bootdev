from textnode import TextType,TextNode
from htmlnode import HTMLnode,HTMLTAG


def main():
    new_textnode = TextNode("This is some anchor text", TextType.ITALIC, "https://www.boot.dev")
    print("help")
    print(new_textnode.__repr__())
    new_htmlnode = HTMLnode(tag = HTMLTAG.BOLD, value = "heelp!")
    print(new_htmlnode.__repr__())
    
    
if __name__ == "__main__":
    main()