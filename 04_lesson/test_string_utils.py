import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  Hello world", "Hello world"),
    ("python", "python"),
])
def test_trim_positive(input_str, expected):
        assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("_123 ", "_123 "),
    ("", ""),
    ("\npython", "\npython"),
])
def test_trim_negative(input_str, expected):
        assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("Hello World", " ", True),
])
def test_contains_positive(string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SkyPro", "z", False),
    ("", "a", False),
])
def test_contains_negative(string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Hello", "l", "Heo"),
    ("banana", "a", "bnn"),
])
def delete_symbol_contains_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "Y", "SkyPro"),
    ("Hello", "h", "Hello"),
    (" ", "i", " "),
])
def delete_symbol_contains_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected