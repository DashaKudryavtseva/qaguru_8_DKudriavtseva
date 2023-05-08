import pytest
from models.product_model import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(
            1000
        ), 'Товара в наличии меньше указаного количества либо значение некорректно'

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(400)
        assert product.quantity == 600

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_new_product(self, cart, product):
        cart.add_product(product, 200)
        assert cart.products[product]

    def test_cart_add_exist_product(self, cart, product):
        cart.add_product(product, 200)
        cart.add_product(product, 200)
        assert cart.products[product] == 400

    def test_cart_remove_product_decreese_quantity(self, cart, product):
        cart.add_product(product, 200)
        cart.remove_product(product, 10)
        assert cart.products[product] == 190
        # for p, q in cart.products.items():
        #     print(f'{p}, {q}')

    def test_cart_remove_product_in_empty_cart(self, cart, product):
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 200)
        cart.remove_product(product)
        assert len(cart.products) == 0

    def test_cart_clear(self, cart):
        table = Product("table", 150, "This is a table", 5000)
        chair = Product("chair", 300, "This is a chair", 4500)
        cart.add_product(table, 20)
        cart.add_product(chair, 30)
        cart.products.clear()
        assert len(cart.products) == 0

    def test_cart_get_total_price(self, cart):
        table = Product("table", 150, "This is a table", 5000)
        chair = Product("chair", 300, "This is a chair", 4500)
        cart.add_product(table, 20)
        cart.add_product(chair, 30)
        assert cart.get_total_price() == 12000

    def test_buy(self, cart, product):
        cart.add_product(product, 20)
        cart.buy()
        assert product.quantity == 980

    def test_buy_over_quantity(self, cart, product):
        cart.add_product(product, 1020)
        with pytest.raises(ValueError):
            cart.buy()
