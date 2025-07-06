from textnode import TextType,TextNode


def main():
    new_textnode = TextNode("This is some anchor text", TextType.ITALIC, "https://www.boot.dev")
    print("help")
    print(new_textnode.__repr__())
    
if __name__ == "__main__":
    main()