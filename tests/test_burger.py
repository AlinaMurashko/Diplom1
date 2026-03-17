import pytest

from constants import bun_constants as bun
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    @pytest.mark.parametrize(
        "bun_name",
        [
            "",  # Пустое имя
            "bun" * 100,  # Длинное имя
            "bun@#$%",  # Спецсимволы
            "Булка",  # Кириллица
        ]
    )
    def test_set_buns_with_different_names(self, burger, bun_name):
        """Тест установки булочки с граничными значениями имени"""
        bun_object = Bun(bun_name, 100)

        burger.set_buns(bun_object)

        # Проверяем через методы, не через атрибуты
        assert burger.get_price() == bun_object.get_price() * 2
        assert f"(==== {bun_name} ====)" in burger.get_receipt()

    @pytest.mark.parametrize(
        "bun_price",
        [
            0,  # Нулевая цена
            0.01,  # Минимальная цена
            1000,  # Большая цена
            -50,  # Отрицательная цена
        ]
    )
    def test_set_buns_with_different_prices(self, burger, bun_price):
        """Тест установки булочки с граничными значениями цены"""
        bun_name = "green bun"
        bun_object = Bun(bun_name, bun_price)

        burger.set_buns(bun_object)

        # Проверяем через методы, не через атрибуты
        assert burger.get_price() == bun_object.get_price() * 2
        assert f"(==== {bun_name} ====)" in burger.get_receipt()

    def test_set_buns_changes_bun(self, burger, black_bun, white_bun):
        """Тест смены булочки"""
        burger.set_buns(black_bun)
        price_with_black = burger.get_price()

        burger.set_buns(white_bun)
        price_with_white = burger.get_price()

        assert price_with_black != price_with_white
        assert bun.BUN_NAME_BLACK not in burger.get_receipt()
        assert bun.BUN_NAME_WHITE in burger.get_receipt()

    @pytest.mark.parametrize(
        "ingredient_type",
        [
            INGREDIENT_TYPE_SAUCE,
            INGREDIENT_TYPE_FILLING,
            "unknown_type",  # Неизвестный тип
            "",  # Пустой тип
        ]
    )
    def test_add_ingredient_with_different_types(self, burger, black_bun, ingredient_type):
        """Тест добавления ингредиентов с разными типами"""
        burger.set_buns(black_bun)
        ingredient = Ingredient(ingredient_type, "test", 100)

        burger.add_ingredient(ingredient)

        # Проверяем через методы
        assert burger.get_price() == black_bun.get_price() * 2 + 100
        assert f"= {ingredient_type.lower()} test =" in burger.get_receipt()

    @pytest.mark.parametrize(
        "ingredient_price",
        [
            0,  # Нулевая цена
            0.01,  # Минимальная цена
            1000,  # Большая цена
            -50,  # Отрицательная цена
        ]
    )
    def test_add_ingredient_with_different_prices(self, burger, black_bun, ingredient_price):
        """Тест добавления ингредиентов с разными ценами"""
        burger.set_buns(black_bun)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test", ingredient_price)

        burger.add_ingredient(ingredient)

        assert burger.get_price() == black_bun.get_price() * 2 + ingredient_price

    def test_add_multiple_ingredients_increases_price(self, burger, black_bun, hot_sauce, cutlet_filling):
        """Тест увеличения цены при добавлении ингредиентов"""
        burger.set_buns(black_bun)
        initial_price = burger.get_price()

        burger.add_ingredient(hot_sauce)
        burger.add_ingredient(cutlet_filling)

        final_price = burger.get_price()
        assert final_price == initial_price + hot_sauce.get_price() + cutlet_filling.get_price()

    def test_remove_ingredient_changes_price(self, burger_with_ingredients):
        """Тест изменения цены при удалении ингредиента"""
        initial_price = burger_with_ingredients.get_price()

        burger_with_ingredients.remove_ingredient(0)
        new_price = burger_with_ingredients.get_price()

        assert new_price < initial_price

    def test_remove_ingredient_changes_receipt(self, burger_with_ingredients, hot_sauce):
        """Тест изменения чека при удалении ингредиента"""
        burger_with_ingredients.remove_ingredient(0)
        receipt_after = burger_with_ingredients.get_receipt()

        assert f"= sauce {hot_sauce.get_name()} =" not in receipt_after

    @pytest.mark.parametrize(
        "from_idx, to_idx",
        [
            (0, 1),  # Перемещение вперед
            (1, 0),  # Перемещение назад
        ]
    )
    def test_move_ingredient_changes_order(self, burger_with_ingredients, from_idx, to_idx):
        """Тест изменения порядка ингредиентов при перемещении"""
        receipt_before = burger_with_ingredients.get_receipt()
        lines_before = receipt_before.split('\n')
    
        burger_with_ingredients.move_ingredient(from_idx, to_idx)
        receipt_after = burger_with_ingredients.get_receipt()
        lines_after = receipt_after.split('\n')
    
        # Проверяем, что порядок строк изменился
        assert lines_before[1:3] != lines_after[1:3]

    def test_move_ingredient_same_index_no_changes(self, burger_with_ingredients):
        """Тест перемещения на тот же индекс"""
        receipt_before = burger_with_ingredients.get_receipt()

        burger_with_ingredients.move_ingredient(0, 0)
        receipt_after = burger_with_ingredients.get_receipt()

        assert receipt_before == receipt_after

    def test_get_price_with_bun_only(self, burger, black_bun):
        """Тест цены бургера только с булочкой"""
        burger.set_buns(black_bun)
        assert burger.get_price() == black_bun.get_price() * 2

    def test_get_price_with_ingredients(self, burger_with_ingredients, black_bun, hot_sauce, cutlet_filling):
        """Тест цены бургера с ингредиентами"""
        expected_price = black_bun.get_price() * 2 + hot_sauce.get_price() + cutlet_filling.get_price()
        assert burger_with_ingredients.get_price() == expected_price

    def test_get_receipt_with_bun_only(self, burger, black_bun):
        """Тест чека только с булочкой"""
        burger.set_buns(black_bun)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')

        assert lines[0] == f"(==== {black_bun.get_name()} ====)"
        assert lines[1] == f"(==== {black_bun.get_name()} ====)"
        assert lines[2] == ""
        assert lines[3] == f"Price: {black_bun.get_price() * 2}"
        assert len(lines) == 4

    def test_get_receipt_with_ingredients(self, burger_with_ingredients, black_bun, hot_sauce, cutlet_filling):
        """Тест чека с ингредиентами"""
        receipt = burger_with_ingredients.get_receipt()
        lines = receipt.split('\n')

        expected_price = black_bun.get_price() * 2 + hot_sauce.get_price() + cutlet_filling.get_price()

        assert lines[0] == f"(==== {black_bun.get_name()} ====)"
        assert lines[1] == f"= sauce {hot_sauce.get_name()} ="
        assert lines[2] == f"= filling {cutlet_filling.get_name()} ="
        assert lines[3] == f"(==== {black_bun.get_name()} ====)"
        assert lines[4] == ""
        assert lines[5] == f"Price: {expected_price}"
        assert len(lines) == 6
