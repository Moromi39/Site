from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        if self.children is None:
            raise ValueError("ParentNode requires children")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        html_string = f'<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>'
        return html_string

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
