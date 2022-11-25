#!/opt/homebrew/bin/python3

import sys

if __name__ == '__main__':
    cmd = sys.argv[1]
    fle = sys.argv[2]

    if cmd == "stats":
        from markdown_helper.get_statistics import run
        run(fle)

    elif cmd == "extract-code":
        from markdown_helper.extract_code import run
        run(fle)

    elif cmd == "format-code":
        from markdown_helper.format_code_samples import run
        run(fle)

    elif cmd == "fix-image-paths":
        from markdown_helper.fix_image_paths import run
        findtext = sys.argv[3]
        replacetext = sys.argv[4]
        run(fle, findtext, replacetext)

    elif cmd == "img-local":
        from markdown_helper.move_images_local import run
        run(fle)

