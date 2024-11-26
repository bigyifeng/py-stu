from functools import reduce


def str2num(s):
    if not isinstance(s, int):
        raise ValueError(f"fn:str2num is fail, because '{s}' is not a integer")
    return int(s)


def calc(exp):
    try:
        ss = exp.split("+")
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)
    except ValueError as e:
        print(e)
        return None


def main():
    r = calc("100 + 200 + 345")
    print("100 + 200 + 345 =", r)
    r = calc("99 + 88 + 7.6")
    print("99 + 88 + 7.6 =", r)


main()
