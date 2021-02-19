import pytest
import BoidAgent
import cmath
import random
import math
def test_normalize():
    assert BoidAgent.normalize(complex(0,0)) == complex(0,0)
    assert BoidAgent.normalize(complex(1,0)) == complex(1,0)
    assert BoidAgent.normalize(complex(0,1)) == complex(0,1)
    assert BoidAgent.normalize(complex(-1,0)) == complex(-1,0)
    assert BoidAgent.normalize(complex(0,-1)) == complex(0,-1)

def test_normalize_magnitude():
    random.seed(42)
    for _ in range(100):
        c = complex(random.randint(1,100),random.randint(1,100))
        assert math.isclose(abs(BoidAgent.normalize(c)),1)

def test_init_boid():
    a = BoidAgent.BoidAgent()
    assert a.pos == complex(0,0)
    assert a.vel == complex(0,0)
    assert a.surf == None