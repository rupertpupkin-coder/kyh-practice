import uppgift39


def test_maxiumum_number_a():
    a = 123
    b = 33
    c = 22
    assert uppgift39.maximum(a, b, c) == 123


def test_maxiumum_number_b():
    a = 1
    b = 3
    c = 2
    assert uppgift39.maximum(a, b, c) == 3


def test_maxiumum_number_c():
    a = 1
    b = 2
    c = 22
    assert uppgift39.maximum(a, b, c) == 22

def test_add_all_numbers_a():
    expected = 300
    got = uppgift39.add([100, 99, 101])
    assert expected == got

def test_add_all_numbers_b():
    expected = 5
    got = uppgift39.add([2, 1, 2])
    assert expected == got

def test_add_all_numbers_c():
    expected = 14
    got = uppgift39.add([7, 6, 1])
    assert expected == got

def test_product_numbers_a():
    expected = 10
    got = uppgift39.multiply([5, 2, 1])
    assert expected == got

def test_product_numbers_b():
    expected = 20
    got = uppgift39.multiply([5, 2, 2])
    assert expected == got

def test_product_numbers_c():
    expected = 100
    got = uppgift39.multiply([50, 2, 1])
    assert expected == got



