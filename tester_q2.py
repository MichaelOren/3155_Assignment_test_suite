import re
from q2.wildcard_matching import wildcard

from report_helper import print_diff

def naive_wildcard(text, pattern):
    results = []
    for i in range(len(text) - len(pattern) + 1):
        for j, p_ch in enumerate(pattern):
            if text[i + j] == p_ch or p_ch == "?":
                if j == len(pattern) - 1:
                    results.append(i + 1)
                continue
            else:
                break
    return results


if __name__ == "__main__":
    text_file = "text_files/reference.txt"
    pattern_file = 'text_files/pattern-collection-wildcards.txt'
    # pattern_file = 'text_files/pattern-collection-wildcards_2.txt'
    print("\n===== First Set =====")
    with open(text_file) as text_line:
        with open(pattern_file) as patterns:
            text = list(text_line.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = naive_wildcard(text, pattern)
                bm = wildcard(text, pattern)
                print_diff(works, bm, pattern, i)
            print("====================")
    
    print("\n===== Second Set =====")
    with open("text_files/add_wildcard_txt_here.txt") as texts:
        with open("text_files/add_wildcard_patterns_here.txt") as patterns:
            counter = -1
            for text, pattern in zip(texts, patterns):
                counter += 1
                text = text.strip()
                pattern = pattern.strip()
                works = naive_wildcard(text, pattern)
                bm = wildcard(text, pattern)
                passed = print_diff(works, bm, pattern, counter)
                if not passed:
                    break
            print("=====================")
