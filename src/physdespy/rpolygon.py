from itertools import filterfalse, tee

from .recti import vector2


class rpolygon:
    def __init__(self, coords):
        """[summary]

        Args:
            coords ([type]): [description]
        """
        self._origin = coords[0]
        self._vecs = list(c - coords[0] for c in coords[1:])

    def __iadd__(self, rhs: vector2):
        """[summary]

        Args:
            rhs (vector2): [description]

        Returns:
            [type]: [description]
        """
        self._origin += rhs
        return self

    def signed_area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        vecs = self._vecs
        res = vecs[0].x * vecs[0].y
        for v0, v1 in zip(vecs[:-1], vecs[1:]):
            res += v1.x * (v1.y - v0.y)
        return res

    def to_polygon(self):
        ''' @todo '''
        pass


def partition(pred, iterable):
    'Use a predicate to partition entries into true entries and false entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8 and 1 3 5 7 9
    t1, t2 = tee(iterable)
    return filter(pred, t1), filterfalse(pred, t2)


def create_ymono_rpolygon(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    min_pt = min(lst, key=lambda a: (a.y, a.x))
    max_pt = max(lst, key=lambda a: (a.y, a.x))
    d = max_pt - min_pt

    def r2l(a):
        return d.x * (a.y - min_pt.y) < (a.x - min_pt.x) * d.y

    def l2r(a):
        return d.x * (a.y - min_pt.y) > (a.x - min_pt.x) * d.y

    [lst1, lst2] = partition(l2r, lst) if d.x > 0 \
        else partition(r2l, lst)
    lst1 = sorted(lst1, key=lambda a: (a.y, a.x))
    lst2 = sorted(lst2, key=lambda a: (a.y, a.x), reverse=True)
    return lst1 + lst2


def create_xmono_rpolygon(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    min_pt = min(lst, key=lambda a: (a.x, a.y))
    max_pt = max(lst, key=lambda a: (a.x, a.y))
    d = max_pt - min_pt

    def r2l(a):
        return d.y * (a.x - min_pt.x) < (a.y - min_pt.y) * d.x

    def l2r(a):
        return d.y * (a.x - min_pt.x) > (a.y - min_pt.y) * d.x

    [lst1, lst2] = \
        partition(l2r, lst) if d.y > 0 else \
        partition(r2l, lst)
    lst1 = sorted(lst1, key=lambda a: (a.x, a.y))
    lst2 = sorted(lst2, key=lambda a: (a.x, a.y), reverse=True)
    return lst1 + lst2


def create_test_rpolygon(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
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

    if dx < 0:
        lsta = sorted(lst6, key=lambda a: (a.x, a.y), reverse=True)
        lstb = sorted(lst5, key=lambda a: (a.y, a.x))
        lstc = sorted(lst4, key=lambda a: (a.x, a.y))
        lstd = sorted(lst3, key=lambda a: (a.y, a.x), reverse=True)
    else:
        lsta = sorted(lst3, key=lambda a: (a.x, a.y))
        lstb = sorted(lst4, key=lambda a: (a.y, a.x))
        lstc = sorted(lst5, key=lambda a: (a.x, a.y), reverse=True)
        lstd = sorted(lst6, key=lambda a: (a.y, a.x), reverse=True)
    return lsta + lstb + lstc + lstd
