from physdespy.polygon import create_test_polygon
from physdespy.recti import point


def test_polygon():
    coords = [(-2, 2), (0, -1), (-5, 1), (-2, 4), (0, -4), (-4, 3), (-6, -2),
              (5, 1), (2, 2), (3, -3), (-3, -3), (3, 3), (-3, -4), (1, 4)]
    S = [point(x, y) for (x, y) in coords]

    P = create_test_polygon(S)
    print('----------------------')
    # print(R2.area())
    for v in P:
        print(v)

    assert (False)
