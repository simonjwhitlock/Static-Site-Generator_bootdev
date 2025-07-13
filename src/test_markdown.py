import unittest

from markdownblock import BlockType,markdown_to_blocks,block_to_block_type



class TestTextNode(unittest.TestCase):
    def test_markdown_blocks1(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        split = markdown_to_blocks(markdown)
        self.assertEqual(3, len(split))
        self.assertEqual("# This is a heading", split[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", split[1])
        self.assertEqual("""- This is the first list item in a list block
- This is a list item
- This is another list item""", split[2])
        
    def test_markdown_blocks2(self):
        markdown = """# This is a heading



This is a paragraph of text. It has some **bold** and _italic_ words inside of it.



- This is the first list item in a list block
- This is a list item
- This is another list item"""
        split = markdown_to_blocks(markdown)
        self.assertEqual(3, len(split))
        self.assertEqual("# This is a heading", split[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", split[1])
        self.assertEqual("""- This is the first list item in a list block
- This is a list item
- This is another list item""", split[2])
        
    def test_markdown_blocks3(self):
        markdown = """     # This is a heading

      This is a paragraph of text. It has some **bold** and _italic_ words inside of it.       

- This is the first list item in a list block
- This is a list item
- This is another list item      """
        split = markdown_to_blocks(markdown)
        self.assertEqual(3, len(split))
        self.assertEqual("# This is a heading", split[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", split[1])
        self.assertEqual("""- This is the first list item in a list block
- This is a list item
- This is another list item""", split[2])

    def test_markdown_blocks4(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

                           

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        split = markdown_to_blocks(markdown)
        self.assertEqual(3, len(split))
        self.assertEqual("# This is a heading", split[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", split[1])
        self.assertEqual("""- This is the first list item in a list block
- This is a list item
- This is another list item""", split[2])

    def test_markdown_blocks5(self):
        markdown = """# This is a heading     
        
        
        

        This is a paragraph of text. It has some **bold** and _italic_ words inside of it.        





- This is the first list item in a list block
- This is a list item
- This is another list item"""
        split = markdown_to_blocks(markdown)
        self.assertEqual(3, len(split))
        self.assertEqual("# This is a heading", split[0])
        self.assertEqual("This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", split[1])
        self.assertEqual("""- This is the first list item in a list block
- This is a list item
- This is another list item""", split[2])
        
    def test_markdown_block_type_para1(self):
        block = "This is a paragraph block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_para2(self):
        block = "# This is the a Heading 1 block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEAD, block_type)
        
    def test_markdown_block_type_head1(self):
        block = "###### This is the a Heading 6 block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEAD, block_type)
        
    def test_markdown_block_type_head2(self):
        block = "####### This is not a heading block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_head3(self):
        block = "#This is not a heading block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_code1(self):
        block = """```
This is a code block
```"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, block_type)
        
    def test_markdown_block_type_code2(self):
        block = "```This is NOT a code block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_quote1(self):
        block = ">This is a one line quote block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)
        
    def test_markdown_block_type_quote2(self):
        block = """>This is line one of a quote block
>This is line 2 of a quote block
>This is line 3 of a quote block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, block_type)
        
    def test_markdown_block_type_quote3(self):
        block = """>This is line one of a broken quote block
>This is line 2 of a broken quote block
-This is line 3 of a broken quote block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_listu1(self):
        block = "- This is a one line unordeded list block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.LISTU, block_type)
        
    def test_markdown_block_type_listu2(self):
        block = """- This is line one of a unordeded list block
- This is line 2 of a unordeded list block
- This is line 3 of a unordeded list block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.LISTU, block_type)
        
    def test_markdown_block_type_listu3(self):
        block = """- This is line one of a broken unordeded list block
- This is line 2 of a broken unordeded list block
1. This is line 3 of a broken unordeded list block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)
        
    def test_markdown_block_type_listo1(self):
        block = "1. This is a one line ordered list block"
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.LISTO, block_type)
        
    def test_markdown_block_type_listo2(self):
        block = """1.This is line one of a ordered list block
2. This is line 2 of a ordered list block
3. This is line 3 of a ordered list block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.LISTO, block_type)
        
    def test_markdown_block_type_listo3(self):
        block = """1. This is line one of a broken ordered list block
3. This is line 2 of a broken ordered list block
4. This is line 3 of a broken ordered list block"""
        block_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, block_type)

        
if __name__ == "__main__":
    unittest.main()