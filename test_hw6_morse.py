import pytest
from hw6_morse import decode


@pytest.mark.parametrize('result,expected',
                         [('.--- .. -. --. .-.. . -....- -... . .-.. .-.. ...', 'JINGLE-BELLS'),
                          ('.--. -.-- - .... --- -.', 'PYTHON'),
                          ('', ''),
                          ('... --- ...', 'SOS')])
def test_exception(result, expected):
    assert decode(result) == expected
