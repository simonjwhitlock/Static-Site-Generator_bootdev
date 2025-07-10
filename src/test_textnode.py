import unittest

from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_type(self):
        node = TextNode("helphelp im beign repressed", TextType.ITALIC, "https://arse.about.face.uk")
        node2 = TextNode("helphelp im beign repressed", TextType.IMAGE, "https://arse.about.face.uk")
        self.assertNotEqual(node, node2)
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()