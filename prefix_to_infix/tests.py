import pytest
from prefix_to_infix import PrefixToInfixConverter

@pytest.fixture
def converter():
    return PrefixToInfixConverter()

def test_prefix_to_infix(converter):
    assert converter.prefix_to_infix("+ + 10 20 30") == "((10 + 20) + 30)"
    assert converter.prefix_to_infix("* 5 2") == "(5 * 2)"
    assert converter.prefix_to_infix("- 8 3") == "(8 - 3)"
    assert converter.prefix_to_infix("/ 10 5") == "(10 / 5)"
    
    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("- - 1 2")

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("+ 1")

    with pytest.raises(ValueError, match="Invalid expression"):
        converter.prefix_to_infix("+ 1 2 3")
