from uppgift36.pwstrength import compute_strength


def test_password_with_length_11_gives_1_point():
    pw = "1" * 11
    assert compute_strength(pw) == 1

def test_password_with_length_5_gives_0_point():
    pw = "1" * 5
    assert compute_strength(pw) == 0

def test_password_with_special_characters_gives_1_point():
    pw = "#%&+_-"
    assert compute_strength(pw) == 1

def test_password_with_number_and_letter_gives_1_point():
    pw = "1a"
    assert compute_strength(pw) == 1

def test_password_empty_gives_0_point():
    pw = ""
    assert compute_strength(pw) == 0

def test_password_with_bad_chars_0_point():
    pw = "!" * 11
    assert compute_strength(pw) == 0

def test_password_with_length_11_and_number_letters_and_specialchars_gives_3_point():
    pw = "aaa111&&&&" * 11
    assert compute_strength(pw) == 3

def test_password_with_length_3_and_number_letters_and_specialchars_gives_2_point():
    pw = "a1&"
    assert compute_strength(pw) == 2

def test_password_with_length_11_and_number_letters_and_gives_2_point():
    pw = "a1" * 11
    assert compute_strength(pw) == 2

def test_password_with_length_11_and_specialchars_gives_2_point():
    pw = "&" * 11
    assert compute_strength(pw) == 2