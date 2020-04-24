import re
from q3.modified_kmp import modified_kmp

from report_helper import print_diff

def tester(text, pattern):
    return [m.start() + 1 for m in re.finditer('(?=' + pattern + ')', text)]


if __name__ == "__main__":
    # text_file = "text_files/reference.txt"
    # pattern_file = 'text_files/pattern-collection.txt'
    # with open(text_file) as text_line:
    #     with open(pattern_file) as patterns:
    #         text = list(text_line.readlines())[0]
    #         for i, pattern in enumerate(patterns):
    #             pattern = pattern.strip()
    #             works = tes, pattern)
    #             bm = modified_kmp(text, pattern)
    #             if not set(works) == set(bm):
    #                 print(pattern)
    #                 main_list = len(list(set(works) - set(bm)))
    #                 # print(sorted(main_list))
    #                 print(main_list)
    #                 break
    #             else:
    #                 print(i, "True")

    with open("text_files/add_text_here.txt") as texts:
        with open("text_files/add_patterns_here.txt") as patterns:
            counter = -1
            for text, pattern in zip(texts, patterns):
                counter += 1
                text = text.strip()
                pattern = pattern.strip()
                works = tester(text, pattern)
                bm = modified_kmp(text, pattern)
                passed = print_dff(works, bm, pattern, counter)
                if not passed:
                    break
            print("====================")
