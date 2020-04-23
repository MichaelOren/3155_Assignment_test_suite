import re
from q1.mirrored_boyermoore import mirrored_boyer_moore

def tester(text, pattern):
    return [m.start() for m in re.finditer('(?=' + pattern + ')', text)]


if __name__ == "__main__":
    # text_file = "reference.txt"
    # pattern_file = "pattern-collection.txt"
    text_file = 'reference.txt'
    pattern_file = 'pattern-collection.txt'
    with open(text_file) as text:
        with open(pattern_file) as patterns:
            text_line = list(text.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                # print(len(tester(text_line, pattern)))
                # try:
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
    
    # string = "aabaabacababacabacaxaabaaacababacababcy"
    # pattern = "acababacaba"
    # works = tester(string, pattern)
    # bm = boyerMoore(string, pattern)
    # if not works == bm:
    #     print(pattern)
    # else:
    #     print(True)
    # t = ["fasdjadjafaweoirfjadvjnzxclkfeyflzjxkjadvnzadlsdkjfyhweaf", "jad"]
    # pattern = t[1]
    # string = t[0]
    # works = tester(string, pattern)
    # bm = boyerMoore(string, pattern)
    # if not works == bm:
    #     print(pattern)
    # else:
    #     print(True)