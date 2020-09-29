import uppgift40


def test_reverse_text():
    expected = "Teststring"[::-1]
    got = "".join(uppgift40.reverse("Teststring"))
    assert expected == got

def test_reverse_text_wrong():
    expected = "Tststring"[::-1]
    got = "".join(uppgift40.reverse("Teststring"))
    assert expected != got


def test_count_upper_letters():
    expected = 0
    got = uppgift40.text("asdaasd")
    assert expected == got


def test_value_true():
    expected = True
    got = uppgift40.minmax(44, 10, 56)
    assert expected == got


def test_value_False():
    expected = False
    got = uppgift40.minmax(60, 10, 56)
    assert expected == got


def test_value_False_2():
    expected = False
    got = uppgift40.minmax(5, 10, 56)
    assert expected == got
