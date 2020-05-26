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
        cur = iter(self)
        p0 = next(cur)
        x0 = p0.x
        yi = p0.y
        sum = 0
        while True:
            try:
                p = next(cur)
                sum += (p.y - yi) * (p.x - x0)
                yi = p.y
            except StopIteration:
                break
        return sum
    # bool contains(point<U>& rhs)


def create_xmono_rpolygon(lst):
    # def l2r(a, b):
    #     return a.x < b.x

    # def r2l(a, b):
    #     return b.x < a.x

    max_it = max(lst, key=lambda a: a.x)
    pivot = max_it.y

    def downup(a):
        return a.y < pivot

    def updown(a):
        return pivot < a.y

    min_it = min(lst, key=lambda a: a.x)
    dir = downup if min_it.y < pivot else updown
    [lst1, lst2] = partition(dir, lst)

    sorted(lst1, key=lambda a: a.x)
    sorted(lst2, key=lambda a: a.x, reverse=True)

    return rpolygon([p for p in lst1] + [p for p in lst2])


def create_ymono_rpolygon(lst):
    # def b2t(a, b):
    #     return a.y < b.y

    # def t2b(a, b):
    #     return b.y < a.y

    max_it = max(lst, key=lambda a: a.y)
    pivot = max_it.x

    def leftright(a):
        return a.x < pivot

    def rightleft(a):
        return pivot < a.x

    min_it = min(lst, key=lambda a: a.y)
    dir = leftright if min_it.x < pivot else rightleft
    [lst1, lst2] = partition(dir, lst)
    sorted(lst1, key=lambda a: a.y)
    sorted(lst2, key=lambda a: a.y, reverse=True)
    return rpolygon([p for p in lst1] + [p for p in lst2])
