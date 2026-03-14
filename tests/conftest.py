import pytest
from constants import bun_constants as bun
from constants import ingredient_constants as ing
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    """Фикстура для создания пустого бургера"""
    return Burger()


@pytest.fixture
def black_bun():
    """Фикстура для создания черной булочки"""
    return Bun(bun.BUN_NAME_BLACK, bun.BUN_PRICE_BLACK)


@pytest.fixture
def white_bun():
    """Фикстура для создания белой булочки"""
    return Bun(bun.BUN_NAME_WHITE, bun.BUN_PRICE_WHITE)


@pytest.fixture
def hot_sauce():
    """Фикстура для создания острого соуса"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)


@pytest.fixture
def cutlet_filling():
    """Фикстура для создания котлеты"""
    return Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)


@pytest.fixture
def burger_with_ingredients(black_bun, hot_sauce, cutlet_filling):
    """Фикстура для создания бургера с ингредиентами"""
    burger = Burger()
    burger.set_buns(black_bun)
    burger.add_ingredient(hot_sauce)
    burger.add_ingredient(cutlet_filling)
    return burger