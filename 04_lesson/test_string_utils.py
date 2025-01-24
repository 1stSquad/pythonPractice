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
    assert string_utils.capitilize("hello hello world and my dear friend") == "Hello hello world and my dear friend"
    assert string_utils.capitilize("123") == "123"                  # Негатив
    assert string_utils.capitilize("") == ""                        # Негатив

# Тесты для метода trim
def test_trim(string_utils):
    assert string_utils.trim("   лень") == "лень"                       # Позитив
    assert string_utils.trim("   Lorem aliquip aliqua adipisicing deserunt "
                             "mollit eu pariatur pariatur proident ex reprehenderit "
                             "ipsum fugiat excepteur. Occaecat sit ullamco eu magna ipsum sit nisi. "
                             "Dolore nisi nostrud officia cupidatat culpa eiusmod qui qui. "
                             "Laborum veniam voluptate qui enim occaecat incididunt "
                             "eu sit occaecat irure ad amet excepteur.") == ("Lorem aliquip aliqua "
                                                                             "adipisicing deserunt "
                                                                             "mollit eu pariatur pariatur "
                                                                             "proident ex reprehenderit "
                                                                             "ipsum fugiat excepteur. "
                                                                             "Occaecat sit ullamco eu magna "
                                                                             "ipsum sit nisi. Dolore nisi "
                                                                             "nostrud officia cupidatat culpa eiusmod "
                                                                             "qui qui. Laborum veniam voluptate "
                                                                             "qui enim occaecat incididunt eu "
                                                                             "sit occaecat irure ad amet excepteur.")
    assert string_utils.trim("лень   ") == "лень   "                    # Негатив
    assert string_utils.trim("   лень   ") == "лень   "                 # Негатив
    assert string_utils.trim("   hello world   ") == "hello world   "   # Негатив
    assert string_utils.trim("   ") == ""                               # Негатив
    assert string_utils.trim("") == ""                                  # Негатив

# Тесты для метода to_list
def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]                               # Позитив
    assert string_utils.to_list("a/b/c/d", "/") == ["a", "b", "c", "d"]           # Позитив
    assert string_utils.to_list("one:two:three", ":") == ["one", "two", "three"]  # Позитив
    assert string_utils.to_list("") == []                                                        # Негатив
    assert string_utils.to_list("one,two,three", ";") == ["one,two,three"]        # Негатив

# Тесты для метода contains
def test_contains(string_utils):
    assert string_utils.contains("Лень", "ь") is True     # Позитив
    assert string_utils.contains("Лень", "П") is False    # Позитив
    assert string_utils.contains("Лень", "") is True      # Позитив
    assert string_utils.contains("", "") is True          # Негатив
    assert string_utils.contains("", "ь") is False        # Негатив
    assert string_utils.contains("    ", " ") is True     # Негатив

# Тесты для метода delete_symbol
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("Лень", "Л") == "ень"    # Позитив
    assert string_utils.delete_symbol("Лень", "нь") == "Ле"    # Позитив
    assert string_utils.delete_symbol("Лень", "ар") == "Лень"  # Негатив
    assert string_utils.delete_symbol("", "Л") == ""           # Негатив
    assert string_utils.delete_symbol("Лень", "") == "Лень"    # Негатив

# Тесты для метода starts_with
def test_starts_with(string_utils):
    assert string_utils.starts_with("Лень", "Л") is True        # Позитив
    assert string_utils.starts_with("Лень", "ь") is False       # Негатив
    assert string_utils.starts_with("", "") is True             # Негатив
    assert string_utils.starts_with("", "б") is False           # Негатив

# Тесты для метода end_with
def test_end_with(string_utils):
    assert string_utils.end_with("Лень", "ь") is True           # Позитив
    assert string_utils.end_with("Лень", "Л") is False          # Негатив
    assert string_utils.end_with("", "") is True                # Негатив
    assert string_utils.end_with("", "m") is False              # Негатив


# Тесты для метода is_empty
def test_is_empty(string_utils):
    assert string_utils.is_empty("") is True                                 # Позитив
    assert string_utils.is_empty(" ") is True                                # Позитив
    assert string_utils.is_empty("Лень") is False                            # Негатив
    assert string_utils.is_empty(" Лень") is False                           # Негатив

# Тесты для метода list_to_string
def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"                        # Позитив
    assert string_utils.list_to_string(["Hello", "World"]) == "Hello, World"                # Позитив
    assert string_utils.list_to_string(["Чунга", "Чанга"], "-") == "Чунга-Чанга"  # Позитив
    assert string_utils.list_to_string([]) == ""                                            # Негатив