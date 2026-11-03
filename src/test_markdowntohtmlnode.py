import unittest
from markdowntohtmlnode import markdown_to_html_node

class markdown_to_html_node_test(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
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
        print(html)
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_headings(self):
        md = """
# Heading one

### Heading **three**

###### Heading six
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading one</h1><h3>Heading <b>three</b></h3><h6>Heading six</h6></div>",
        )

    def test_blockquote(self):
        md = """
> This is a quote
> with **two** lines
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>two</b> lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- first
- **second**
- third with `code`
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ul><li>first</li><li><b>second</b></li><li>third with <code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. first
2. _second_
3. third
"""
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first</li><li><i>second</i></li><li>third</li></ol></div>",
        )

    def test_ordered_list_double_digits(self):
        items = "\n".join(f"{i}. item{i}" for i in range(1, 12))
        html = markdown_to_html_node(items).to_html()
        expected_items = "".join(f"<li>item{i}</li>" for i in range(1, 12))
        self.assertEqual(html, f"<div><ol>{expected_items}</ol></div>")

    def test_link_in_paragraph(self):
        md = "Go to [my site](https://example.com) now"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            '<div><p>Go to <a href="https://example.com">my site</a> now</p></div>',
        )

    def test_list_item_with_link(self):
        md = "- see [docs](https://example.com)\n- plain"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(
            html,
            '<div><ul><li>see <a href="https://example.com">docs</a></li><li>plain</li></ul></div>',
        )
    def test_extra_blank_lines_between_blocks(self):
        md = "first\n\n\n\nsecond"
        html = markdown_to_html_node(md).to_html()
        self.assertEqual(html, "<div><p>first</p><p>second</p></div>")

if __name__ == "__main__":
    unittest.main()
