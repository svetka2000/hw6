import pytest
from hw6 import decode


@pytest.mark.parametrize('result,expected',
                         [('.--- .. -. --. .-.. . -....- -... . .-.. .-.. ...', 'JINGLE-BELLS'),
                          ('.--. -.-- - .... --- -.', 'PYTHON'),
                          ('', ''),
                          ('... --- ...', 'SOS')])
def test_exception(result, expected):
    with pytest.raises(ValueError):
        if decode(result) == expected:
            raise ValueError