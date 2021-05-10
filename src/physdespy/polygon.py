from itertools import filterfalse, tee

from .recti import vector2


class polygon:
    def __init__(self, coords):
        self._origin = coords[0]
        self._vecs = list(c - coords[0] for c in coords[1:])

    def __iadd__(self, rhs: vector2):
        self._origin += rhs
        return self

    def signed_area_x2(self):
        res = 0
        for v1, v2 in zip(self._vecs[:-1], self._vecs[1:]):
            res += v1.cross(v2)
        return res


def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) -->  1 3 5 7 9  and  0 2 4 6 8
    t1, t2 = tee(iterable)
    return filter(pred, t1), filterfalse(pred, t2)


def create_test_polygon(lst):
    max_pt = max(lst, key=lambda a: (a.y, a.x))
    min_pt = min(lst, key=lambda a: (a.y, a.x))
    dx = max_pt.x - min_pt.x
    dy = max_pt.y - min_pt.y

    def right_left(a):
        return dx * (a.y - min_pt.y) < (a.x - min_pt.x) * dy

    [lst1, lst2] = partition(right_left, lst)
    lst1 = list(lst1)  # note!!!!
    lst2 = list(lst2)  # note!!!!
    max_pt1 = max(lst1, key=lambda a: (a.x, a.y))
    [lst3, lst4] = partition(lambda a: a.y < max_pt1.y, lst1)
    min_pt2 = min(lst2, key=lambda a: (a.x, a.y))
    [lst5, lst6] = partition(lambda a: a.y > min_pt2.y, lst2)

    if dx < 0:  # left -> right
        lst3 = sorted(lst3, key=lambda a: (a.y, a.x), reverse=True)
        lst4 = sorted(lst4, key=lambda a: (a.x, a.y), reverse=True)
        lst5 = sorted(lst5, key=lambda a: (a.y, a.x))
        lst6 = sorted(lst6, key=lambda a: (a.x, a.y))
    else:  # right -> left
        lst3 = sorted(lst3, key=lambda a: (a.x, a.y))
        lst4 = sorted(lst4, key=lambda a: (a.y, a.x))
        lst5 = sorted(lst5, key=lambda a: (a.x, a.y), reverse=True)
        lst6 = sorted(lst6, key=lambda a: (a.y, a.x), reverse=True)
    return polygon(lst3 + lst4 + lst5 + lst6)


def create_ymono_polygon(lst):
    max_pt = max(lst, key=lambda a: (a.y, a.x))
    min_pt = min(lst, key=lambda a: (a.y, a.x))
    dx = max_pt.x - min_pt.x
    dy = max_pt.y - min_pt.y

    def right_left(a):
        return dx * (a.y - min_pt.y) < (a.x - min_pt.x) * dy

    [lst1, lst2] = partition(right_left, lst)
    lst1 = sorted(lst1, key=lambda a: (a.y, a.x))
    lst2 = sorted(lst2, key=lambda a: (a.y, a.x), reverse=True)
    return polygon(lst1 + lst2)


def create_xmono_polygon(lst):
    """[summary]

    Arguments:
        lst {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    max_pt = max(lst, key=lambda a: (a.x, a.y))
    min_pt = min(lst, key=lambda a: (a.x, a.y))
    dx = max_pt.x - min_pt.x
    dy = max_pt.y - min_pt.y

    def right_left(a):
        return dx * (a.y - min_pt.y) < (a.x - min_pt.x) * dy

    [lst1, lst2] = partition(right_left, lst)
    lst3 = sorted(lst1, key=lambda a: a.x)
    lst4 = sorted(lst2, key=lambda a: a.x, reverse=True)
    return polygon(lst3 + lst4)
