from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type.value.upper():
        case "TEXT":
            return LeafNode(None, text_node.text)
        case "BOLD":
            return LeafNode("b", text_node.text)
        case "ITALIC":
            return LeafNode("i", text_node.text)
        case "CODE":
            return LeafNode("code", text_node.text)
        case "LINK":
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case "IMAGE":
            return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Invalid markup text.")