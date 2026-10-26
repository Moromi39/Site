import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
