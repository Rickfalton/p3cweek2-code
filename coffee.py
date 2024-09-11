class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []  # Stores orders for this coffee

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = value

    def orders(self):
        """Returns a list of all orders for this coffee."""
        return self._orders

    def customers(self):
        """Returns a unique list of customers who have ordered this coffee."""
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        """Returns the number of times this coffee has been ordered."""
        return len(self._orders)

    def average_price(self):
        """Returns the average price for this coffee based on all orders."""
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders) if self._orders else 0
