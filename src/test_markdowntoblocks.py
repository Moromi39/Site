import unittest
from markdowntoblocks import BlockType, markdown_to_blocks, block_to_block_type


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


    def test_block_to_block_type_heading(self):
        block = "#### This is a heading"
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_block_to_block_type_olist(self):
        block = "1. This\n2. is\n3. an ordered\n4. list"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))

    def test_block_to_block_type_broken_olist(self):
        block = "1. This\n5. is\n3. an ordered\n4. list"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_unordered_list(self):
        block = "- yep\n- an\n- list"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_broken_unordered_list(self):
        block = "- yep\n an\n- list"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))
        
    def test_broken2_unordered_list(self):
        block = "- yep\n-an\n- list"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))
        
        
        
        
        
        


