import sys

from markdown_it import MarkdownIt

md = MarkdownIt("gfm-like")

def get_code_line_ranges(text):
    tokens = md.parse(text)
    code_ranges = []
    for token in tokens:
        if token.type == 'fence':
            print(token.map, token.info)


def get_code(text):
    tokens = md.parse(text)

    for token in tokens:
        if token.type == 'fence':
            print(token.map, token.info)
            print(token.content)

def run(fle):
    with open(fle) as f:
        text = f.read()
    get_code_line_ranges(text)

if __name__ == '__main__':
    fle = sys.argv[1]
    run(fle)



