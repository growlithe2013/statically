from textnode import *
from htmlnode import *
from text_to_html import *



def main():
    node = TextNode("Hello world", TextType.LINK, "Eeveelutionary.com")
    print(node)

main()