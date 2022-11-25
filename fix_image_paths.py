import sys

from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer

md = MarkdownIt("gfm-like").enable('table')

def fix_image_paths(text, findtext, replacetext):
    env = {}
    tokens = md.parse(text, env)
    
    for i, token in enumerate(tokens):
        if token.type == "inline":
            for child in token.children:
                if child.type == "image":
                    child.attrs['src'] = child.attrs['src'].replace(findtext, replacetext)
                    
    rendered  = MDRenderer().render(tokens, md.options, env, extensions={"tables"})
    print(rendered)
    # print(tokens)


def run(fle, findtext, replacetext):
    with open(fle) as f:
        text = f.read()
    fix_image_paths(text, findtext, replacetext)

if __name__ == '__main__':
    fle = sys.argv[1]
    findtext = sys.argv[2]
    replacetext = sys.argv[3]
    run(fle, findtext, replacetext)



