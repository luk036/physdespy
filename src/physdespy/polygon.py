from itertools import filterfalse, tee

from .recti import vector2


class polygon:
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

    def signed_area_x2(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        vecs = self._vecs
        res = vecs[0].x * vecs[1].y - vecs[-1].x * vecs[-2].y
        for v0, v1, v2 in zip(vecs[:-2], vecs[1:-1], vecs[2:]):
            res += v1.x * (v2.y - v0.y)
        return res

    def is_rectilinear(self):
        '''@todo '''
        pass


def partition(pred, iterable):
    'Use a predicate to partition entries into true entries and false entries'
    # partition(is_odd, range(10)) -->   0 2 4 6 8 and 1 3 5 7 9
    t1, t2 = tee(iterable)
    return filter(pred, t1), filterfalse(pred, t2)


def create_ymono_polygon(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    topmost_pt = max(lst, key=lambda a: (a.y, a.x))
    bottommost_pt = min(lst, key=lambda a: (a.y, a.x))
    d = topmost_pt - bottommost_pt

    def right_left(a):
        return d.x * (a.y - bottommost_pt.y) < (a.x - bottommost_pt.x) * d.y

    [lst1, lst2] = partition(right_left, lst)
    lst1 = sorted(lst1, key=lambda a: (a.y, a.x))
    lst2 = sorted(lst2, key=lambda a: (a.y, a.x), reverse=True)
    return lst1 + lst2


def create_xmono_polygon(lst):
    """[summary]

    Arguments:
        lst {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    rightmost_pt = max(lst, key=lambda a: (a.x, a.y))
    leftmost_pt = min(lst, key=lambda a: (a.x, a.y))
    d = rightmost_pt - leftmost_pt
    # dy = rightmost_pt.y - leftmost_pt.y
    # dx = rightmost_pt.x - leftmost_pt.x

    def right_left(a):
        return d.y * (a.x - leftmost_pt.x) < (a.y - leftmost_pt.y) * d.x

    [lst1, lst2] = partition(right_left, lst)
    lst3 = sorted(lst1, key=lambda a: (a.x, a.y))
    lst4 = sorted(lst2, key=lambda a: (a.x, a.y), reverse=True)
    return lst3 + lst4


def create_test_polygon(lst):
    """[summary]

    Args:
        lst ([type]): [description]

    Returns:
        [type]: [description]
    """
    topmost_pt = max(lst, key=lambda a: (a.y, a.x))
    bottommost_pt = min(lst, key=lambda a: (a.y, a.x))
    dx = topmost_pt.x - bottommost_pt.x
    dy = topmost_pt.y - bottommost_pt.y

    def right_left(a):
        return dx * (a.y - bottommost_pt.y) < (a.x - bottommost_pt.x) * dy

    [lst1, lst2] = partition(right_left, lst)
    lst1 = list(lst1)  # note!!!!
    lst2 = list(lst2)  # note!!!!
    topmost_pt1 = max(lst1, key=lambda a: (a.x, a.y))
    [lst3, lst4] = partition(lambda a: a.y < topmost_pt1.y, lst1)
    bottommost_pt2 = min(lst2, key=lambda a: (a.x, a.y))
    [lst5, lst6] = partition(lambda a: a.y > bottommost_pt2.y, lst2)

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
