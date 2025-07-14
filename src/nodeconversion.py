from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from regex import extract_markdown_images,extract_markdown_links

#function to convert a text node into a html leaf node.
def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="",props= {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextType value not valid")
        
#function to split out sub strings with alertnative text types.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT:
            split_text = node.text.split(delimiter)
            node_text_type = True
            if len(split_text) % 2 == 0:
                raise ValueError("invalid markdown, section not closed")
            for text_section in split_text:
                if text_section == "":
                    node_text_type = not node_text_type
                    continue
                if node_text_type:
                    new_node = TextNode(text_section,TextType.TEXT)
                    node_list.append(new_node)
                else:
                    new_node = TextNode(text_section,text_type)
                    node_list.append(new_node)
                node_text_type = not node_text_type
        else:
            node_list.append(node)
    return node_list

#funcition to split text nodes and extract images
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

#funcition to split text nodes and extract links    
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    delineaters = {TextType.BOLD: "**", TextType.ITALIC: "_", TextType.CODE: "`"}
    new_nodes = [TextNode(text, TextType.TEXT)]
    for type, delineater in delineaters.items():
        new_nodes = split_nodes_delimiter(new_nodes, delineater, type)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes