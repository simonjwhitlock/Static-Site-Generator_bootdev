import unittest

from generate_html import extract_title



class TestTextNode(unittest.TestCase):
    def test_markdown_title1(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        title = extract_title(markdown)
        self.assertEqual("This is a heading", title)
        
    def test_markdown_title2(self):
        block = "# This is the a Heading 1 block"
        title = extract_title(block)
        self.assertEqual("This is the a Heading 1 block", title)
        
    def test_markdown_title3(self):
        block = "### This is the a Heading 6 block"
        with self.assertRaises(Exception):
            extract_title(block)
        
    def test_markdown_title4(self):
        block = """### This is the a Heading 6 block"

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        with self.assertRaises(Exception):
            extract_title(block)


        
if __name__ == "__main__":
    unittest.main()