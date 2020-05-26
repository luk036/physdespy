from random import randint

from physdespy.recti import point
from physdespy.rpolygon import create_xmono_rpolygon, create_ymono_rpolygon, rpolygon


def test_RPolygon():
    N = 100
    S = [point(randint(0, 99), randint(0, 99)) for _ in range(N)]
    for r in S:
        print(r)

    R = rpolygon(S)
    print(R.area())

    _ = create_xmono_rpolygon(S)
    # print(R1.area())

    _ = create_ymono_rpolygon(S)
    # print(R2.area())
