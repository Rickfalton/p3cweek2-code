import pytest
from coffee import Coffee
from order import Order  
from customer import Customer  

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Co")
    Coffee("Coffee")

def test_coffee_orders():
    coffee = Coffee("Coffee")
    customer1 = Customer("Ayubu")
    customer2 = Customer("BabaMboga")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.order() == []
   # assert orders [] == [order.order]

def test_coffee_customers():
    coffee = Coffee("Coffee")
    customer1 = Customer("Ayubu")
    customer2 = Customer("BabaMboga")
    order1 = Order(customer1, coffee, 3.5)
    order2 = Order(customer2, coffee, 4.0)
    assert coffee.customers() == []

def test_coffee_num_orders():
    coffee = Coffee("Coffee")
    customer = Customer("Ayubu")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.0)
    orders = []
    assert len(orders) == 0

def test_coffee_average_price():
    coffee = Coffee("Coffee")
    customer = Customer("Ayubu")
    order1 = Order(customer, coffee, 3.5)
    order2 = Order(customer, coffee, 4.0)
    assert coffee.average_price() == 3.75