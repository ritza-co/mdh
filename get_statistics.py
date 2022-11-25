from mistletoe import Document, ast_renderer 
from pprint import pprint
from collections import defaultdict
import sys

type_statistics = defaultdict(int)
character_statistics = defaultdict(int)

def print_stats(name, stats):
    print()
    print(f"# {name}")
    for k in stats:
        padding = 10 - len(k)
        name = k + (" " * padding)
        print(f"   {name}\t{stats[k]}")

def walk_ast(ast, indent='', tpe=None):
    global type_statistics, character_statistics
    for child in ast:
        if 'content' in child:
            type_statistics[tpe] += 1
            character_statistics[tpe] += len(child['content'].split())
            
            
        if 'children' in child:
            walk_ast(child['children'], indent=indent+'  ', tpe=child['type'])


def run(fle, human=False):
    with open(fle) as f:
        lines = f.readlines()
    document = Document(lines)
    output = ast_renderer.get_ast(document)
    walk_ast(output['children'])

    if human:
        print_stats("Type statistics", type_statistics)
        print_stats("Character statistics", character_statistics)
    else:
        lst = sorted(list(type_statistics))
        vls = [str(type_statistics[i]) for i in lst]
        print(' '.join(vls))

if __name__ == '__main__':
    fle = sys.argv[1]
    run(fle)
   




