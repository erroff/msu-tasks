

def sort(p: list) -> list:
    return sorted(p)
    pass


def find(p: list, i) -> int:
    try:
        return p.index(i)
    except ValueError:
        return -1
    pass


def my_min(p: list) -> int:
    return min(p)
    pass


def my_max(p: list) -> int:
    return max(p)
    pass


def my_sum(p: list) -> int:
    return sum(p)


def revert(p: list) -> list:
    p.reverse()
    return p
    pass


def unique(p: list) -> list:
    return list(set(p))
    pass


def capitalize(s: str) -> str:
    return s.capitalize()
    pass


def lower(s: str) -> str:
    return s.lower()
    pass


def upper(s: str) -> str:
    return s.upper()
    pass


def replace(s: str, old: str, new: str) -> str:
    return s.replace(old, new)
    pass


def swapcase(s: str) -> str:
    return s.swapcase()
    pass


def split(s: str, separator: str) -> list[str]:
    return s.split(separator)
    pass
