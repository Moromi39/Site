
class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list[HTMLNode] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        
        html_string = ""

        for key in self.props:
            html_string += f' {key}="{self.props[key]}"'

        return html_string

    def __repr__(self):
        yep = f'tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n'     
        return yep
    


