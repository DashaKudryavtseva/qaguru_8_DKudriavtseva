from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """

    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        return self.quantity >= quantity

    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity):
            self.quantity = self.quantity - quantity
        else:
            raise ValueError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, quantity=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if not self.products:
            self.products.update({product: quantity})
        else:
            for key, value in self.products.items():
                if key == product:
                    self.products[key] = value + quantity
                    break
                else:
                    self.products.update({product: quantity})
                    break

    def remove_product(self, product: Product, quantity=None):
        """
        Метод удаления продукта из корзины.
        Если quantity не передан, то удаляется вся позиция
        Если quantity больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if self.products:
            for key, value in self.products.items():
                if key == product and quantity is None or quantity > value:
                    self.products.pop(product)
                    break
                elif key == product:
                    self.products[key] = value - quantity
                    break
        else:
            raise ValueError

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0

        for key, value in self.products.items():
            total_price += key.price * value

        return total_price

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for key, value in self.products.items():
            key.buy(value)
        self.clear()
