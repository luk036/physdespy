from .vector2 import vector2


class point:
    __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __lt__(self, rhs):
        return (self.x, self.y) < (rhs.x, rhs.y)

    def __gt__(self, rhs):
        return (self.x, self.y) > (rhs.x, rhs.y)

    def __le__(self, rhs):
        return (self.x, self.y) <= (rhs.x, rhs.y)

    def __ge__(self, rhs):
        return (self.x, self.y) >= (rhs.x, rhs.y)

    def __eq__(self, rhs):
        return (self.x, self.y) == (rhs.x, rhs.y)

    def __ne__(self, rhs):
        return (self.x, self.y) != (rhs.x, rhs.y)

    def __iadd__(self, rhs: vector2):
        self._x += rhs.x
        self._y += rhs.y
        return self

    def __add__(self, rhs: vector2):
        tmp = self.copy()
        return tmp.__iadd__(rhs)

    def __isub__(self, rhs: vector2):
        self._x -= rhs.x
        self._y -= rhs.y
        return self

    def __sub__(self, rhs: vector2):
        tmp = self.copy()
        return tmp.__isub__(rhs)

    def flip(self):
        return point(self.y, self.x)

    def __str__(self):
        return '({self.x}, {self.y})'.format(self=self)


class dualpoint(point):
    def __init__(self, x, y):
        point.__init__(self, x, y)

    @property
    def x(self):
        return self._y

    @property
    def y(self):
        return self._x


class interval:
    __slots__ = ('_lower', '_upper')

    def __init__(self, lower, upper):
        self._lower = lower
        self._upper = upper

    @property
    def lower(self):
        return self._lower

    @property
    def upper(self):
        return self._upper

    def len(self):
        return self.upper - self.lower

    def __eq__(self, rhs):
        return (self.lower, self.upper) == (rhs.lower, rhs.upper)

    def __lt__(self, rhs):
        return self.upper < rhs.lower

    def __gt__(self, rhs):
        return rhs < self

    def __le__(self, rhs):
        return not (rhs < self)

    def __ge__(self, rhs):
        return not (self < rhs)

    def contains(self, a) -> bool:
        return not (a < self.lower or self.upper < a)

    def __str__(self):
        return '[{self.lower}, {self.upper}]'.format(self=self)


class rectangle:
    __slots__ = ('_x', '_y')

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def lower(self):
        return point(self.x.lower, self.y.lower)

    @property
    def upper(self):
        return point(self.x.upper, self.y.upper)

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def flip(self):
        return rectangle(self.y, self.x)

    def __str__(self):
        return '({self.x}, {self.y})'.format(self=self)

    def contains(self, a) -> bool:
        return self.x.contains(a.x) and self.y.contains(a.y)

    def area(self):
        return self.x.len() * self.y.len()
