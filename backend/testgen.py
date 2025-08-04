def generate_test_case(code):
    """
    Simple mock logic to simulate AI-generated test case.
    You can later upgrade this with HuggingFace or Gemini API.
    """
    if "def add" in code:
        summary = "Test addition of two numbers"
        test_code = """
def test_add():
    assert add(2, 3) == 5
"""
    elif "def subtract" in code:
        summary = "Test subtraction of two numbers"
        test_code = """
def test_subtract():
    assert subtract(5, 2) == 3
"""
    else:
        summary = "Basic placeholder test case"
        test_code = "# TODO: Write test case here"

    return summary, test_code
