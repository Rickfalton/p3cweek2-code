#from order import Order 
class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []  # Stores orders placed by this customer

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        """Returns a list of all orders placed by this customer."""
        return self._orders

    def coffees(self):
        """Returns a unique list of coffee objects the customer has ordered."""
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        """Create an order for this customer and associate it with a coffee and price."""
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order
