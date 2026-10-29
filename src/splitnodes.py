from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text_split = node.text.split(delimiter)

        if len(text_split) == 1:
            new_nodes.append(node)
            continue

        if len(text_split) % 2 == 0:
            raise ValueError("Invalid Markdown Syntax")

        for i, text in enumerate(text_split):
            if text == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))

            else:
                new_nodes.append(TextNode(text, text_type))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        extraction = extract_markdown_images(node.text)

        if extraction == []:
            new_nodes.append(node)
            continue

        text = node.text 
        # parts_list = []

        for img in extraction:
            alt, link = img

            before, after = text.split(f"![{alt}]({link})", 1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.IMAGE, link))

            # parts_list.append(img)
            text = after
        
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))


    return new_nodes


        



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        extraction = extract_markdown_links(node.text)

        if extraction == []:
            new_nodes.append(node)
            continue

        text = node.text 
        # parts_list = []

        for img in extraction:
            alt, link = img

            before, after = text.split(f"[{alt}]({link})", 1)

            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.LINK, link))

            # parts_list.append(img)
            text = after
        
        if text != "":
            new_nodes.append(TextNode(text, TextType.TEXT))


    return new_nodes
