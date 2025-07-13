import unittest
from markdowntohtml import markdown_to_html_node

class TestHTMLgeneration(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_ordered_list(self):
        md = """1. This is the first list item in a list block
2. This is a list item
3. This is another list item"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ol></div>",
        )
        
    def test_unordered_list(self):
        md = """- This is the first list item in a list block
- This is a list item
- This is another list item"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>",
        )

    def test_heading1 (self):
        md = "# this is a heading 1 line"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a heading 1 line</h1></div>",
        )

    def test_heading5 (self):
        md = "##### this is a heading 5 line"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>this is a heading 5 line</h5></div>",
        )

    def test_quote (self):
        md = """>this is a multi line
>quote block"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><i>this is a multi line quote block</i></div>",
        )
    
    def test_combined (self):
        md = """###### Big **BOLD** heading with _EMPASIS_    

# here lies the ashes of sanity

_abstarcte of a stupid aritcal_

>this is a multi line
>quote block
>by a pretentious arse

```
for some _reason_ they
**wrote some damn code!**
```



- to make stuff sureal they wrote
- a dumb list too

1. and an ordered one
2. because why the hell not


"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Big <b>BOLD</b> heading with <i>EMPASIS</i></h6><h1>here lies the ashes of sanity</h1><p>abstarcte of a stupid aritcal</p><i>this is a multi line quote block by a pretentious arse</i><pre><code>for some _reason_ they\n**wrote some damn code!**\n</code></pre><ul><li>to make stuff sureal they wrote</li><li>a dumb list too</li></ul><ol><li>and an ordered one</li><li>because why the hell not</li></ol></div>",
        )
        
if __name__ == "__main__":
    unittest.main()