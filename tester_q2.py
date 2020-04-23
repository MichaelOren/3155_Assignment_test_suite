import re
from q2.wildcard_matching import wildcard

def naive_wildcard(text, pattern):
    results = []
    for i in range(len(text) - len(pattern) + 1):
        for j, p_ch in enumerate(pattern):
            if text[i + j] == p_ch or p_ch == "?":
                if j == len(pattern) - 1:
                    results.append(i)
                continue
            else:
                break
    return results


if __name__ == "__main__":
    text_file = 'reference.txt'
    pattern_file = 'pattern-collection-wildcards.txt'
    with open(text_file) as text:
        with open(pattern_file) as patterns:
            text_line = list(text.readlines())[0]
            for i, pattern in enumerate(patterns):
                pattern = pattern.strip()
                works = naive_wildcard(text_line, pattern)
                bm = wildcard(text_line, pattern)
                if not set(works) == set(bm):
                    print(pattern)
                    main_list = len(list(set(works) - set(bm)))
                    # print(sorted(main_list))
                    print(main_list)
                    break
                else:
                    print(i, "True")