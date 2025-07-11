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
            for text_section in split_text:
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
        text = node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(node)
        else:
            for image in images:
                image_node = TextNode(image[0], TextType.IMAGE, image[1])
                split = text.split("!", 1)
                text_node = TextNode(split[0], node.text_type)
                text = (split[1].split(")", 1))[1]
                new_nodes.append(text_node)
                new_nodes.append(image_node)
    return new_nodes

#funcition to split text nodes and extract links    
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(node)
        else:
            for link in links:
                link_node = TextNode(link[0], TextType.LINK, link[1])
                split = text.split("[", 1)
                text_node = TextNode(split[0], node.text_type)
                text = (split[1].split(")", 1))[1]
                new_nodes.append(text_node)
                new_nodes.append(link_node)
    return new_nodes