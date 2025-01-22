import pytest
from StringUtils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для метода capitilize
def test_capitilize(string_utils):
    assert string_utils.capitilize("лень") == "Лень"                # Позитив
    assert string_utils.capitilize("привет мир") == "Привет мир"    # Позитив
    assert string_utils.capitilize("hello world") == "Hello world"  # Позитив
    assert string_utils.capitilize("123") == "123"                  # Негатив
    assert string_utils.capitilize("") == ""                        # Негатив

# Тесты для метода trim
def test_trim(string_utils):
    assert string_utils.trim("   лень") == "лень"                       # Позитив
    assert string_utils.trim("лень   ") == "лень   "                    # Негатив
    assert string_utils.trim("   лень   ") == "лень   "                 # Негатив
    assert string_utils.trim("   hello world   ") == "hello world   "   # Негатив
    assert string_utils.trim("   ") == ""                               # Негатив
    assert string_utils.trim("") == ""                                  # Негатив

# Тесты для метода to_list
def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]                              # Позитив
    assert string_utils.to_list("a/b/c/d", "/") == ["a", "b", "c", "d"]           # Позитив
    assert string_utils.to_list("one:two:three", ":") == ["one", "two", "three"]  # Позитив
    assert string_utils.to_list("") == []                                                       # Негатив
    assert string_utils.to_list("one,two,three", ";") == ["one,two,three"]        # Негатив

# Тесты для метода contains
def test_contains(string_utils):
    assert string_utils.contains("Лень", "ь") is True     # Позитив
    assert string_utils.contains("Лень", "П") is False    # Позитив
    assert string_utils.contains("Лень", "") is True      # Позитив
    assert string_utils.contains("", "") is True          # Негатив


# Тесты для метода delete_symbol
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("Лень", "Л") == "ень"    # Позитив
    assert string_utils.delete_symbol("Лень", "нь") == "Ле"    # Позитив
    assert string_utils.delete_symbol("Лень", "ар") == "Лень"  # Негатив
    assert string_utils.delete_symbol("", "Л") == ""           # Негатив

# Тесты для метода starts_with
def test_starts_with(string_utils):
    assert string_utils.starts_with("Лень", "Л") is True
    assert string_utils.starts_with("Лень", "ь") is False
    assert string_utils.starts_with("", "") is True
    assert string_utils.starts_with("", "б") is False

# Тесты для метода end_with
def test_end_with(string_utils):
    assert string_utils.end_with("Лень", "ь") is True
    assert string_utils.end_with("Лень", "Л") is False
    assert string_utils.end_with("", "") is True
    assert string_utils.end_with("", "m") is False

# Тесты для метода is_empty
def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True
    assert string_utils.is_empty(" ") is True
    assert string_utils.is_empty("Лень") is False
    assert string_utils.is_empty(" Лень") is False

# Тесты для метода list_to_string
def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Hello", "World"]) == "Hello, World"
    assert string_utils.list_to_string(["Чунга", "Чанга"], "-") == "Чунга-Чанга"
    assert string_utils.list_to_string([]) == ""  # Пустой список