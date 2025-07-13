import unittest
from textnode import TextType,TextNode
from htmlnode import HTMLNode,LeafNode,ParentNode
from nodeconversion import text_node_to_html_node,split_nodes_delimiter, split_nodes_image, split_nodes_link,text_to_textnodes

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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_images2(self):
        node = TextNode(
            "This is text with no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_split_images3(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_images4(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node,node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with no images", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images5(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with no images",
            TextType.TEXT,
        )
        node3 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node,node2,node3])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("This is text with no images", TextType.TEXT),
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
        
    def test_text_to_textnodes1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(10 , len(nodes))
        self.assertEqual("This is ", nodes[0].text)
        self.assertEqual(TextType.TEXT, nodes[0].text_type)
        self.assertEqual("text", nodes[1].text)
        self.assertEqual(TextType.BOLD, nodes[1].text_type)
        self.assertEqual("italic", nodes[3].text)
        self.assertEqual(TextType.ITALIC, nodes[3].text_type)
        self.assertEqual("code block", nodes[5].text)
        self.assertEqual(TextType.CODE, nodes[5].text_type)
        self.assertEqual("obi wan image", nodes[7].text)
        self.assertEqual(TextType.IMAGE, nodes[7].text_type)
        self.assertEqual("link", nodes[9].text)
        self.assertEqual(TextType.LINK, nodes[9].text_type)
        
    def test_text_to_textnodes2(self):
        text = "This is **text**"
        nodes = text_to_textnodes(text)
        self.assertEqual(2 , len(nodes))
        self.assertEqual("This is ", nodes[0].text)
        self.assertEqual(TextType.TEXT, nodes[0].text_type)
        self.assertEqual("text", nodes[1].text)
        self.assertEqual(TextType.BOLD, nodes[1].text_type)
        
    def test_text_to_textnodes3(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(text)
        self.assertEqual(1 , len(nodes))
        self.assertEqual("obi wan image", nodes[0].text)
        self.assertEqual(TextType.IMAGE, nodes[0].text_type)
        self.assertEqual("https://i.imgur.com/fJRm4Vk.jpeg", nodes[0].url)



    
if __name__ == "__main__":
    unittest.main()