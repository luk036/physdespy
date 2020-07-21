from physdespy.recti import point
from physdespy.rpolygon import create_ymono_rpolygon


def test_RPolygon():
    coords = [(-2, 2), (0, -1), (-5, 1), (-2, 4), (0, -4), (-4, 3),
              (-6, -2), (5, 1), (2, 2), (3, -3), (-3, -4), (1, 4)]
    S = [point(x, y) for (x, y) in coords]

    P = create_ymono_rpolygon(S)
    print('----------------------')
    for v in P:
        print(v)

    assert (False)
