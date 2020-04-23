import re
from q2.wildcard_matching import wildcard

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
    with open(text_file) as text:
        with open(pattern_file) as patterns:
            text_line = list(text.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = naive_wildcard(text_line, pattern)
                bm = wildcard(text_line, pattern)
                if not set(works) == set(bm):
                    print(pattern)
                    main_list = list(set(bm) - set(works))
                    print(sorted(list(main_list)))
                    print(len(main_list))
                else:
                    print(i, "True")