import re
from q1.mirrored_boyermoore import mirrored_boyer_moore

def tester(text, pattern):
    return [m.start() + 1 for m in re.finditer('(?=' + pattern + ')', text)]


if __name__ == "__main__":
    text_file = "text_files/reference.txt"
    pattern_file = 'text_files/pattern-collection.txt'
    # pattern_file = 'text_files/pattern-collection_2.txt'
    with open(text_file) as text:
        with open(pattern_file) as patterns:
            text_line = list(text.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = tester(text_line, pattern)
                bm = mirrored_boyer_moore(text_line, pattern)
                if not set(works) == set(bm):
                    print(pattern)
                    main_list = len(list(set(works) - set(bm)))
                    # print(sorted(main_list))
                    print(main_list)
                    break
                else:
                    print(i, "True")