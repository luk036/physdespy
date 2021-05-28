from physdespy.halton_int import halton
from physdespy.polygon import create_test_polygon, create_ymono_polygon, polygon
from physdespy.recti import point


def test_polygon():
    coords = [(-2, 2), (0, -1), (-5, 1), (-2, 4), (0, -4), (-4, 3), (-6, -2),
              (5, 1), (2, 2), (3, -3), (-3, -3), (3, 3), (-3, -4), (1, 4)]
    S = [point(x, y) for (x, y) in coords]

    S = create_test_polygon(S)
    P = polygon(S)
    assert P.signed_area_x2() == 103


def test_polygon2():
    hgen = halton([2, 3], [11, 7])
    coords = [hgen() for _ in range(20)]
    S = [point(x, y) for (x, y) in coords]
    S = create_ymono_polygon(S)
    P = polygon(S)
    assert P.signed_area_x2() == -4074624


def test_polygon3():
    hgen = halton([3, 2], [7, 11])
    coords = [hgen() for _ in range(50)]
    S = create_test_polygon([point(x, y) for (x, y) in coords])
    for p in S:
        print("{},{}".format(p.x, p.y), end=' ')
    P = polygon(S)
    assert P.signed_area_x2() == -4449600

# def test_polygon3():
#     hgen = halton([2, 3], [11, 7])
#     coords = [hgen() for _ in range(40)]
#     S = [point(x, y) for (x, y) in coords]
#     S = create_ymono_polygon(S)
#     for p in S:
#         print("{},{}".format(p.x, p.y), end=' ')
#     P = polygon(S)
#     assert P.signed_area_x2() == 3198528000
