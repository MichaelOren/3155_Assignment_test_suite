import re
from q1.mirrored_boyermoore import mirrored_boyer_moore

from report_helper import print_diff

def tester(text, pattern):
    return [m.start() + 1 for m in re.finditer('(?=' + pattern + ')', text)]


if __name__ == "__main__":
    text_file = "text_files/reference.txt"
    pattern_file = 'text_files/pattern-collection.txt'
    # pattern_file = 'text_files/pattern-collection_2.txt'
    print("\n===== First Set =====")
    with open(text_file) as text_line:
        with open(pattern_file) as patterns:
            text = list(text_line.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = tester(text, pattern)
                bm = mirrored_boyer_moore(text, pattern)
                passed = print_diff(works, bm, pattern, i)
                if not passed:
                    break
            print("======================")
    
    print("\n===== Second Set ======")
    with open("text_files/add_text_here.txt") as texts:
        with open("text_files/add_patterns_here.txt") as patterns:
            counter = -1
            for text, pattern in zip(texts, patterns):
                counter += 1
                text = text.strip()
                pattern = pattern.strip()
                works = tester(text, pattern)
                bm = mirrored_boyer_moore(text, pattern)
                passed = print_diff(works, bm, pattern, counter)
                if not passed:
                    break
            print("=======================")
