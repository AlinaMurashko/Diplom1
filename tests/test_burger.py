import pytest

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.constants import bun_constants as bun
from tests.constants import ingredient_constants as ing


class TestBurger:

    def test_initial_state(self):
        """Тест начального состояния бургера"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            [bun.BUN_NAME_BLACK, bun.BUN_PRICE_BLACK],
            [bun.BUN_NAME_WHITE, bun.BUN_PRICE_WHITE],
            [bun.BUN_NAME_RED, bun.BUN_PRICE_RED],
            [bun.BUN_NAME_SESAME, bun.BUN_PRICE_SESAME],
            [bun.BUN_NAME_BRIOCHE, bun.BUN_PRICE_BRIOCHE]
        ]
    )
    def test_set_buns(self, bun_name, bun_price):
        """Тест установки булочки"""
        burger = Burger()
        bun_object = Bun(bun_name, bun_price)

        burger.set_buns(bun_object)

        assert burger.bun == bun_object
        assert burger.bun.get_name() == bun_name
        assert burger.bun.get_price() == bun_price

    @pytest.mark.parametrize(
        "ingredient_type, ingredient_name, ingredient_price",
        [
            [INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT],
            [INGREDIENT_TYPE_SAUCE, ing.SAUCE_SOUR_CREAM, ing.PRICE_SAUCE_SOUR_CREAM],
            [INGREDIENT_TYPE_SAUCE, ing.SAUCE_KETCHUP, ing.PRICE_SAUCE_KETCHUP],
            [INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.SAUCE_BBQ],
            [INGREDIENT_TYPE_SAUCE, ing.SAUCE_MAYO, ing.PRICE_SAUCE_MAYO],
            [INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET],
            [INGREDIENT_TYPE_FILLING, ing.FILLING_CHEESE, ing.PRICE_FILLING_CHEESE],
            [INGREDIENT_TYPE_FILLING, ing.FILLING_LETTUCE, ing.PRICE_FILLING_LETTUCE],
            [INGREDIENT_TYPE_FILLING, ing.FILLING_TOMATO, ing.PRICE_FILLING_TOMATO],
            [INGREDIENT_TYPE_FILLING, ing.FILLING_ONION, ing.PRICE_FILLING_ONION],
        ]
    )
    def test_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        """Тест добавления одного ингредиента"""
        burger = Burger()
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient
        assert burger.ingredients[0].get_type() == ingredient_type
        assert burger.ingredients[0].get_name() == ingredient_name
        assert burger.ingredients[0].get_price() == ingredient_price

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.PRICE_SAUCE_BBQ)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        assert len(burger.ingredients) == 3
        assert burger.ingredients == [ingredient1, ingredient2, ingredient3]

    def test_remove_ingredient_first(self):
        """Тест удаления первого ингредиента"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_remove_ingredient_last(self):
        """Тест удаления последнего ингредиента"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient1

    def test_remove_ingredient_middle(self):
        """Тест удаления ингредиента из середины"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.PRICE_SAUCE_BBQ)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ingredient1, ingredient3]

    def test_move_ingredient_forward(self):
        """Тест перемещения ингредиента вперед"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.PRICE_SAUCE_BBQ)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    def test_move_ingredient_backward(self):
        """Тест перемещения ингредиента назад"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.PRICE_SAUCE_BBQ)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(2, 0)

        assert burger.ingredients == [ingredient3, ingredient1, ingredient2]

    def test_move_ingredient_same_index(self):
        """Тест перемещения ингредиента на тот же индекс"""
        burger = Burger()
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        original_order = burger.ingredients.copy()
        burger.move_ingredient(0, 0)

        assert burger.ingredients == original_order

    @pytest.mark.parametrize(
        "bun_name, bun_price, ingredients_data, expected_price",
        [
            [
                bun.BUN_NAME_BLACK,
                bun.BUN_PRICE_BLACK,
                [
                    (INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT)
                ],
                bun.BUN_PRICE_BLACK * 2 + ing.PRICE_SAUCE_HOT
            ],
            [
                bun.BUN_NAME_WHITE,
                bun.BUN_PRICE_WHITE,
                [],
                bun.BUN_PRICE_WHITE * 2
            ],
            [
                bun.BUN_NAME_RED,
                bun.BUN_PRICE_RED,
                [
                    (INGREDIENT_TYPE_SAUCE, ing.SAUCE_HOT, ing.PRICE_SAUCE_HOT),
                    (INGREDIENT_TYPE_FILLING, ing.FILLING_CUTLET, ing.PRICE_FILLING_CUTLET)
                ],
                bun.BUN_PRICE_RED * 2 + ing.PRICE_SAUCE_HOT + ing.PRICE_FILLING_CUTLET
            ],
            [
                bun.BUN_NAME_SESAME,
                bun.BUN_PRICE_SESAME,
                [
                    (INGREDIENT_TYPE_SAUCE, ing.SAUCE_BBQ, ing.PRICE_SAUCE_BBQ),
                    (INGREDIENT_TYPE_FILLING, ing.FILLING_CHEESE, ing.PRICE_FILLING_CHEESE),
                    (INGREDIENT_TYPE_SAUCE, ing.SAUCE_MAYO, ing.PRICE_SAUCE_MAYO)
                ],
                bun.BUN_PRICE_SESAME * 2 + ing.PRICE_SAUCE_BBQ + ing.PRICE_FILLING_CHEESE + ing.PRICE_SAUCE_MAYO
            ],
        ]
    )
    def test_get_price(self, bun_name, bun_price, ingredients_data, expected_price):
        """Тест расчета цены бургера"""
        burger = Burger()

        bun_object = Bun(bun_name, bun_price)
        burger.set_buns(bun_object)

        for ing_type, ing_name, ing_price in ingredients_data:
            ingredient = Ingredient(ing_type, ing_name, ing_price)
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    @pytest.mark.parametrize(
        "bun_name, bun_receipt, bun_price, ingredients_data, expected_ingredient_receipts, expected_price",
        [
            [
                bun.BUN_NAME_BLACK,
                bun.RECEIPT_BUN_BLACK,
                bun.BUN_PRICE_BLACK,
                [
                    ing.INGREDIENT_HOT_SAUCE
                ],
                [
                    ing.RECEIPT_SAUCE_HOT
                ],
                bun.BUN_PRICE_BLACK * 2 + ing.PRICE_SAUCE_HOT
            ],
            [
                bun.BUN_NAME_WHITE,
                bun.RECEIPT_BUN_WHITE,
                bun.BUN_PRICE_WHITE,
                [
                    ing.INGREDIENT_CUTLET,
                    ing.INGREDIENT_KETCHUP
                ],
                [
                    ing.RECEIPT_FILLING_CUTLET,
                    ing.RECEIPT_SAUCE_KETCHUP
                ],
                bun.BUN_PRICE_WHITE * 2 + ing.PRICE_FILLING_CUTLET + ing.PRICE_SAUCE_KETCHUP
            ],
            [
                bun.BUN_NAME_RED,
                bun.RECEIPT_BUN_RED,
                bun.BUN_PRICE_RED,
                [
                    ing.INGREDIENT_SOUR_CREAM,
                    ing.INGREDIENT_CHEESE
                ],
                [
                    ing.RECEIPT_SAUCE_SOUR_CREAM,
                    ing.RECEIPT_FILLING_CHEESE
                ],
                bun.BUN_PRICE_RED * 2 + ing.PRICE_SAUCE_SOUR_CREAM + ing.PRICE_FILLING_CHEESE
            ],
        ]
    )
    def test_get_receipt_with_constants(self, bun_name, bun_receipt, bun_price, ingredients_data, expected_ingredient_receipts, expected_price):
        """Тест формирования чека с использованием констант"""
        burger = Burger()

        bun_object = Bun(bun_name, bun_price)
        burger.set_buns(bun_object)

        for ing_type, ing_name, ing_price in ingredients_data:
            ingredient = Ingredient(ing_type, ing_name, ing_price)
            burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()
        assert bun_receipt in receipt

        for ingredient_receipt in expected_ingredient_receipts:
            assert ingredient_receipt in receipt

        assert bun_receipt in receipt
        assert f"Price: {expected_price}" in receipt
