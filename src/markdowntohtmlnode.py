from markdowntoblocks import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from texttotextnodes import text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def ulist_to_html_nodes(block):
    items = block.split("\n")
    nodes = []
    for item in items:
        nodes.append(ParentNode("li", text_to_children(item[2:]), None))
    return nodes

def olist_to_html_nodes(block):
    items = block.split("\n")
    nodes = []
    for item in items:
        nodes.append(ParentNode("li", text_to_children(item.split(". ", 1)[1]), None))
    return nodes
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            node = ParentNode("p", text_to_children(text), None)
        elif block_type == BlockType.HEADING:
            heading_num = len(block) - len(block.lstrip("#"))
            text = block[heading_num:].strip()
            node = ParentNode(f"h{heading_num}", text_to_children(text), None)
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            stripped = [line.lstrip(">").strip() for line in lines]
            text = " ".join(stripped)
            node = ParentNode("blockquote", text_to_children(text), None)
        elif block_type == BlockType.UNORDERED_LIST:
            node = ParentNode("ul", ulist_to_html_nodes(block), None)
        elif block_type == BlockType.ORDERED_LIST:
            node = ParentNode("ol", olist_to_html_nodes(block), None)
        elif block_type == BlockType.CODE:
            inner = block[4:-3]
            text_node = TextNode(inner, TextType.TEXT)
            code = text_node_to_html_node(text_node)
            node = ParentNode("pre", [ParentNode("code", [code], None)], None)
        else:
            raise ValueError("Unrecognized BlockType")


        nodes.append(node)  

    return ParentNode("div", nodes, None)
            
        
