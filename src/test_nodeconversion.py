import unittest
from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node,split_nodes_delimiter

class TestNodeConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is some bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is some bold text") 
        
    def test_italic(self):
        node = TextNode("This is some italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is some italic text") 
    
    def test_code(self):
        node = TextNode("This is some code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is some code")
    
    def test_link(self):
        node = TextNode("This is the link text", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is the link text") 
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
        
    def test_image(self):
        node = TextNode("This is the alt text", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is the alt text"})
        
    def test_split_textnode_onecode(self):
        textnode_one = TextNode("This is some anchor text with a `code block` in it", TextType.TEXT)
        split_nodes = split_nodes_delimiter([textnode_one], "`", TextType.CODE)
        self.assertEqual(split_nodes[0].text,"This is some anchor text with a ")
        self.assertEqual(split_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[1].text,"code block")
        self.assertEqual(split_nodes[1].text_type, TextType.CODE)
        self.assertEqual(split_nodes[2].text," in it")
        self.assertEqual(split_nodes[2].text_type, TextType.TEXT)
        
    def test_split_textnode_onebold(self):
        textnode_one = TextNode("This is some anchor text with a **bold block** in it", TextType.TEXT)
        split_nodes = split_nodes_delimiter([textnode_one], "**", TextType.BOLD)
        self.assertEqual(split_nodes[0].text,"This is some anchor text with a ")
        self.assertEqual(split_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[1].text,"bold block")
        self.assertEqual(split_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(split_nodes[2].text," in it")
        self.assertEqual(split_nodes[2].text_type, TextType.TEXT)
        
    def test_split_two_textnodes_one_bold(self):
        textnode_one = TextNode("This is some anchor text with a `code block` in it, and `another code block`", TextType.TEXT)
        textnode_two = TextNode("this is a bold node with a random `code block` in the middle", TextType.BOLD)
        split_nodes = split_nodes_delimiter([textnode_one,textnode_two], "`", TextType.CODE)
        self.assertEqual(split_nodes[0].text,"This is some anchor text with a ")
        self.assertEqual(split_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[1].text,"code block")
        self.assertEqual(split_nodes[1].text_type, TextType.CODE)
        self.assertEqual(split_nodes[2].text," in it, and ")
        self.assertEqual(split_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[3].text,"another code block")
        self.assertEqual(split_nodes[3].text_type, TextType.CODE)
        self.assertEqual(split_nodes[4].text,"")
        self.assertEqual(split_nodes[4].text_type, TextType.TEXT)
        self.assertEqual(split_nodes[5].text,"this is a bold node with a random `code block` in the middle")
        self.assertEqual(split_nodes[5].text_type, TextType.BOLD)

    def test_split_two_textnodes_one_bold(self):
        textnode_one = TextNode("this is a **bold** node", TextType.BOLD)
        textnode_two = TextNode("this is an **italic** node", TextType.ITALIC)
        textnode_three = TextNode("this is a **code** node", TextType.CODE)
        textnode_four = TextNode("this is a **link** node", TextType.LINK, "https://google.com")
        textnode_five = TextNode("this is a **image** node", TextType.IMAGE, "https://google.com")
        split_nodes = split_nodes_delimiter([textnode_one, textnode_two, textnode_three, textnode_four, textnode_five],"**", TextType.TEXT)
        self.assertEqual (split_nodes, [textnode_one, textnode_two, textnode_three, textnode_four, textnode_five])
    
if __name__ == "__main__":
    unittest.main()