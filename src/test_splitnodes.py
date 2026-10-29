import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(answer, split_nodes_delimiter([node], "`", TextType.CODE))


    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(answer, split_nodes_delimiter([node], "_", TextType.ITALIC))

    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(answer, split_nodes_delimiter([node], "**", TextType.BOLD))

    def test_multi(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        node2 = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        node3 = TextNode("This is text with a second _italic block 2_ word", TextType.TEXT)
        node4 = TextNode("This is text with a `code block` word", TextType.TEXT)
        answer = [
            TextNode("This is text with a **bold block** word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a second ", TextType.TEXT),
            TextNode("italic block 2", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ]
        self.assertEqual(answer, split_nodes_delimiter([node, node2, node3, node4], "_", TextType.ITALIC))

    def test_unclosed(self):
        node = TextNode("This is text with a **bold block word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delimiter_at_edges(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        answer = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(answer, split_nodes_delimiter([node], "`", TextType.CODE))
    
    def test_non_text(self):
        node = TextNode("This is text with a `code block`", TextType.CODE)
        self.assertEqual([node], split_nodes_delimiter([node], "`", TextType.CODE))



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
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_links_with_trail(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [second link](https://www.boot.dev) with trailing shit",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" with trailing shit", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_images_with_links_also(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and one link [link](https://www.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and one link [link](https://www.boot.dev)", TextType.TEXT)
            ],
            new_nodes,
        )
