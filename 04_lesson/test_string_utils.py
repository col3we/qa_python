import pytest
from string_utils import StringUtils

string_utils = StringUtils()


def test_capitalize():
    assert string_utils.capitalize("Тест") == "Тест"
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("") == ""

    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


def test_trim():
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("") == ""

    with pytest.raises(AttributeError):
        string_utils.trim(None)


def test_contains():
    assert string_utils.contains("123", "2") is True
    assert string_utils.contains("123", "a") is False
    assert string_utils.contains("", "a") is False

    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


def test_delete_symbol():
    assert string_utils.delete_symbol("Тест", "Т") == "ест"
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol("Тест", "Z") == "Тест"

    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
