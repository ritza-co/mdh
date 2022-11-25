import sys

import black
from markdown_it import MarkdownIt

md = MarkdownIt("gfm-like")

def format_code(text):
    tokens = md.parse(text)
    code_sample_index = 0

    for token in tokens:
        if token.type == 'fence':
            if token.info == 'python':
                code_sample_index += 1
                print(f"Code Sample {code_sample_index} (appears on lines {token.map} of original file)")
                
                print("-----------------------")
                print(black.format_str(token.content, mode=black.FileMode()))
                print("-----------------------")

def run(fle):
    with open(fle) as f:
        text = f.read()
    format_code(text)

if __name__ == '__main__':
    fle = sys.argv[1]
    run(fle)



