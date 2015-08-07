import os
from hts import Bam

HERE = os.path.dirname(__file__)

SAM = os.path.join(HERE, "e.sam")

def test_aux():

    b = Bam(SAM)
    r = next(b)
    assert r.aux == [('NH', 'C', 1)], r.aux
