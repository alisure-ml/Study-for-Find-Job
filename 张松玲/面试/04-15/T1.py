import sys

"""
Tom,Lily,Tom,Lucy,Lucy,Jack
"""
import sys
def check(name):
    if "A" <= name[0] <= "Z":
        for c in name[1:]:
            if not ("a" <= c <= "z"):
                return False
        return True
    else:
        return False

def f():
    names = sys.stdin.readline().strip().split(",")
    name_dict = {}
    for name in names:
        ch = check(name)
        if ch:
            if name not in name_dict:
                name_dict[name] = 1
            else:
                name_dict[name] += 1
        else:
            return "error.0001"
        pass
    count = max(name_dict.values())
    max_name = [name for name in name_dict.keys() if name_dict[name] == count]
    return sorted(max_name)[0]


if __name__ == '__main__':
    name = f()
    print name
    pass
