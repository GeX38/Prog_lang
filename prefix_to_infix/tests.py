import pytest
from prefix_to_infix import PrefixToInfixConverter

@pytest.fixture
def converter():
    return PrefixToInfixConverter()

def test_prefix_to_infix_unary_operators(converter):
    assert converter.prefix_to_infix("+ 5") == "(+5)"
    assert converter.prefix_to_infix("- 7") == "(-7)"
    assert converter.prefix_to_infix("+ - * 5 3 2 4") == "(((5 * 3) - 2) + 4)"
    assert converter.prefix_to_infix("+ / 10 2 * 3 2") == "((10 / 2) + (3 * 2))"

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("+ 1 2 3")

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("")

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("+")

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("1 2 3 +")