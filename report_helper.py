def print_diff(correct, user, pattern, i):
    if not set(correct) == set(user):
        print("Test #{} failed:".format(i))
        print("    Pattern: {}".format(pattern))
        false_trues = list(set(user) - set(correct))
        missed_occs = list(set(correct) - set(user))
        print("    {} occurences missed and {} occurences mistakenly reported".format(len(missed_occs), len(false_trues)))
        return False
    else:
        print("Test #{} passed.".format(i))
        return True
