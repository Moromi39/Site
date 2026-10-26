import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ineq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("this is a text node", TextType.LINK, "boot.dev")
        node2 = TextNode("this is a text node", TextType.LINK)
        self.assertIsNot(node.url, None)
        self.assertIsNone(node2.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img_url(self):
        node = TextNode("This is alt text", TextType.IMAGE, "https://realURL.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://realURL.com") #pyright: ignore[reportOptionalSubscript]
        self.assertEqual(html_node.props["alt"], "This is alt text") #pyright: ignore[reportOptionalSubscript]

    

if __name__ == "__main__":
    unittest.main()
