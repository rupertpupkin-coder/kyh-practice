from conversions import m_to_mm, cm_to_m, mm_to_m


def test_meters_to_mm():
    expected = 1000
    got = m_to_mm(m=1)
    assert expected == got

def test_cm_to_m():
    expected = 2
    got = cm_to_m(cm=200)
    assert expected == got

def test_mm_to_m():
    expected = 1
    got = mm_to_m(mm=1000)
    assert expected == got