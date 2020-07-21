from itertools import filterfalse, tee


def partition(pred, iterable):
    'Use a predicate to partition entries into false entries and true entries'
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


class rpolygon(list):
    def __new__(cls, *args, **kwargs):
        """[summary]

        Returns:
            [type]: [description]
        """
        return list.__new__(cls, *args, **kwargs)

    def area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        cur = iter(self)
        p0 = next(cur)
        x0 = p0.x
        yi = p0.y
        sum = 0
        for p in cur:
            sum += (p.y - yi) * (p.x - x0)
            yi = p.y
        return sum


def create_ymono_rpolygon(lst):
    max_pt = max(lst, key=lambda a: (a.y, a.x))
    min_pt = min(lst, key=lambda a: (a.y, a.x))
    dx = max_pt.x - min_pt.x
    dy = max_pt.y - min_pt.y

    def right_left(a):
        return dx * (a.y - min_pt.y) < (a.x - min_pt.x) * dy

    def left_right(a):
        return dx * (a.y - min_pt.y) > (a.x - min_pt.x) * dy

    if dx < 0:
        [lst1, lst2] = partition(left_right, lst)
    else:
        [lst1, lst2] = partition(right_left, lst)

    lst1 = sorted(lst1, key=lambda a: (a.y, a.x))
    lst2 = sorted(lst2, key=lambda a: (a.y, a.x), reverse=True)
    return rpolygon(lst1 + lst2)


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
    return rpolygon(lst3 + lst4 + lst5 + lst6)


def create_xmono_rpolygon(lst):
    """[summary] (TODO: partition() is not the same as C++'s std::partition())

    Arguments:
        lst {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    max_pt = max(lst, key=lambda a: a.x)
    pivot = max_pt.y

    def downup(a):
        return a.y < pivot

    def updown(a):
        return pivot < a.y

    min_pt = min(lst, key=lambda a: a.x)
    dir = downup if min_pt.y < pivot else updown
    [lst1, lst2] = partition(dir, lst)

    sorted(lst1, key=lambda a: a.x)
    sorted(lst2, key=lambda a: a.x, reverse=True)

    return rpolygon([p for p in lst1] + [p for p in lst2])
