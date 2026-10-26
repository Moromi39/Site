from textnode import TextNode, TextType


def main():
    testnode = TextNode("yep test", TextType.LINK, "https://www.boot.dev")
    print(testnode)


if __name__ == "__main__":
    main()
