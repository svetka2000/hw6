import pytest
from hw6_one_hot_encoder import fit_transform


@pytest.mark.parametrize('result,expected',
                         [(['Moscow', 'New York', 'Moscow', 'London'],
                           [
                             ('Moscow', [0, 0, 1]),
                             ('New York', [0, 1, 0]),
                             ('Moscow', [0, 0, 1]),
                             ('London', [1, 0, 0]),
                         ]),
                             (['Moscow' for i in range(500)], [('Moscow', [1]) for _ in range(500)])]
                         )
def test_exception_1(result, expected):
    assert fit_transform(result) == expected


def test_exception_2():
    with pytest.raises(TypeError):
        fit_transform()


def test_exception_3():
    assert isinstance(fit_transform('Moscow'), type('Moscow', [1]))


def test_exception_4():
    cities = ['Moscow', 'Piter', 'London', 'Moscow', 'Sochi']
    exp_transformed_cities = ('Moscow', [0, 0, 0, 1])
    transformed_cities = fit_transform(cities)
    assert exp_transformed_cities in transformed_cities
