import unittest
from htmlnode import HTMLNode  


class TestHtmlNode(unittest.TestCase):
    def test_None(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.value)
        self.assertIsNone(node.props)

    def test_Not_None(self):
        node = HTMLNode("yep tag")
        self.assertIsNotNone(node.tag)

    def test_props_method(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        print(node)
        print(node.props_to_html())
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        

        
