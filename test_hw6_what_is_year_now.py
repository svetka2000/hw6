from hw6_what_is_year_now import what_is_year_now
import urllib.request
import pytest
from unittest.mock import patch
import io


def test_2020():
    data = io.StringIO('{"currentDateTime": "2020-03-01"}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        assert what_is_year_now() == 2020


def test_2021():
    data = io.StringIO('{"currentDateTime": "02.12.2021"}')
    with patch.object(urllib.request, 'urlopen', return_value=data):
        assert what_is_year_now() == 2021


def test_error():
    data = io.StringIO('{"currentDateTime": "2_12_2021"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=data):
            assert what_is_year_now() == 2021
