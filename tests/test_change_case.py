from text_utils.change_case import lower


def test_lower():
    """Test the lower function."""
    lower_case = lower()
    assert lower_case("Hello World") == "hello world"
    assert lower_case("PYTHON") == "python"
    assert lower_case("12345") == "12345"
    assert lower_case("") == ""