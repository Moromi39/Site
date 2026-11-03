from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks_list = markdown.split("\n\n")
    stripped_blocks_list = [item.strip() for item in blocks_list]


    return [block for block in stripped_blocks_list if block != ""]



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = 'heading'
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block) -> BlockType:
    if re.findall(r"^#{1,6} ", markdown_block):
        return BlockType.HEADING
    if re.findall(r"^```\n[\s\S]*```", markdown_block):
        return BlockType.CODE
    if re.findall(r"^>.*(\n>.*)*$", markdown_block):
        return BlockType.QUOTE
    if re.findall(r"^- .*(\n- .*)*$", markdown_block):
        return BlockType.UNORDERED_LIST
    lines = markdown_block.split("\n")
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


