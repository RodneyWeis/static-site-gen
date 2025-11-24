from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello, World!", TextType.BOLD)
    node2 = TextNode("Click here", text_type=TextType.LINK, url="https://example.com")

    print(node1)
    print(node2)

    # Example of equality check
    node3 = TextNode("Hello, World!", TextType.BOLD)
    print("node1 is equal to node3:", node1 == node3)

main()