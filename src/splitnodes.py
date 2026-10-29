from textnode import TextNode, TextType


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
            raise Exception("Invalid Markdown Syntax")

        for i, text in enumerate(text_split):
            if text == "":
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))

            else:
                new_nodes.append(TextNode(text, text_type))

    return new_nodes


