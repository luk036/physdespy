from physdespy.halton_int import halton
from physdespy.recti import point
from physdespy.rpolygon import (
    create_test_rpolygon,
    create_xmono_rpolygon,
    create_ymono_rpolygon,
    rpolygon
)


def test_RPolygon():
    coords = [(-2, 2), (0, -1), (-5, 1), (-2, 4), (0, -4), (-4, 3),
              (-6, -2), (5, 1), (2, 2), (3, -3), (-3, -4), (1, 4)]
    S, is_anticlockwise = create_ymono_rpolygon([point(x, y) for x, y in coords])
    for p1, p2 in zip(S, S[1:] + [S[0]]):
        print("{},{} {},{}".format(p1.x, p1.y, p2.x, p1.y), end=' ')
    P = rpolygon(S)
    assert is_anticlockwise
    assert P.signed_area() == 45


def test_RPolygon2():
    hgen = halton([3, 2], [7, 11])
    coords = [hgen() for _ in range(20)]
    S, is_anticlockwise = create_ymono_rpolygon([point(x, y) for x, y in coords])
    for p1, p2 in zip(S, S[1:] + [S[0]]):
        print("{},{} {},{}".format(p1.x, p1.y, p2.x, p1.y), end=' ')
    P = rpolygon(S)
    assert not is_anticlockwise
    assert P.signed_area() == -1871424


def test_RPolygon3():
    coords = [(-2, 2), (0, -1), (-5, 1), (-2, 4), (0, -4), (-4, 3),
              (-6, -2), (5, 1), (2, 2), (3, -3), (-3, -4), (1, 4)]
    S, is_anticlockwise = create_xmono_rpolygon([point(x, y) for x, y in coords])
    for p1, p2 in zip(S, S[1:] + [S[0]]):
        print("{},{} {},{}".format(p1.x, p1.y, p2.x, p1.y), end=' ')
    P = rpolygon(S)
    assert not is_anticlockwise
    assert P.signed_area() == -53


def test_RPolygon4():
    hgen = halton([3, 2], [7, 11])
    coords = [hgen() for _ in range(20)]
    S, is_anticlockwise = create_xmono_rpolygon([point(x, y) for x, y in coords])
    for p1, p2 in zip(S, S[1:] + [S[0]]):
        print("{},{} {},{}".format(p1.x, p1.y, p2.x, p1.y), end=' ')
    P = rpolygon(S)
    assert is_anticlockwise
    assert P.signed_area() == 2001024


def test_RPolygon5():
    hgen = halton([3, 2], [7, 11])
    coords = [hgen() for _ in range(50)]
    S = create_test_rpolygon([point(x, y) for x, y in coords])
    for p1, p2 in zip(S, S[1:] + [S[0]]):
        print("{},{} {},{}".format(p1.x, p1.y, p2.x, p1.y), end=' ')
    P = rpolygon(S)
    assert P.signed_area() == -2176416
