import re
from q3.modified_kmp import modified_kmp

def tester(text, pattern):
    return [m.start() for m in re.finditer('(?=' + pattern + ')', text)]


if __name__ == "__main__":
    text_file = 'reference.txt'
    pattern_file = 'pattern-collection.txt'
    with open(text_file) as text:
        with open(pattern_file) as patterns:
            text_line = list(text.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = tester(text_line, pattern)
                bm = modified_kmp(text_line, pattern)
                if not set(works) == set(bm):
                    print(pattern)
                    main_list = len(list(set(works) - set(bm)))
                    # print(sorted(main_list))
                    print(main_list)
                    break
                else:
                    print(i, "True")