##Customer
The Customer class represents an individual customer who can place orders for coffee.

***Attributes:
name (str): The name of the customer (1 to 15 characters).
_orders (list): A list of orders placed by the customer.
Methods:
orders(): Returns a list of all orders placed by the customer.
coffees(): Returns a unique list of Coffee objects the customer has ordered.
create_order(coffee, price): Creates an Order for the customer, linking it to the provided Coffee object and price, then appends it to the list of orders.

##Coffee
The Coffee class represents a type of coffee that customers can order.

Attributes:
name (str): The name of the coffee (minimum 3 characters).
_orders (list): A list of orders for this specific coffee.
Methods:
orders(): Returns a list of all orders for this coffee.
customers(): Returns a unique list of customers who have ordered this coffee.
num_orders(): Returns the total number of times this coffee has been ordered.
average_price(): Returns the average price for this coffee based on all orders. If no orders exist, returns 0.

## Order
The Order class represents an individual order placed by a customer for a specific coffee.

Attributes:
customer (Customer): The customer who placed the order.
coffee (Coffee): The type of coffee ordered.
price (float): The price of the order (must be between 1.0 and 10.0).

## Testing
The pytest framework is used to test the functionality of the classes. The tests cover validation, order creation, and retrieval methods.

## Test Cases

**Coffee Test**
Test_coffee_name_validation: Ensures that a ValueError is raised if the coffee name is too short.
Test_coffee_orders: Checks that the orders method returns the correct orders for a coffee.
Test_coffee_customers: Verifies that the customers method returns the correct set of customers for a coffee.
Test_coffee_num_orders: Confirms that the num_orders method returns the correct number of orders.
Test_coffee_average_price: Ensures that the average_price method calculates the average price of orders correctly.
**Customer Test**
Test_customer_name_validation: Ensures that a ValueError is raised if the customer name is too short or too long.
Test_customer_create_order: Verifies that the create_order method creates a new order with the correct details.
Test_customer_orders: Checks that the orders method returns the correct orders for a customer.
Test_customer_coffees: Ensures that the coffees method returns the correct set of coffee names for a customer.
Test_customer_most_aficionado: Confirms that the most_aficionado method returns the customer with the most expensive order for a coffee.
**Order**
Test_order_price_validation: Ensures that a ValueError is raised if the order price is out of the valid range.
Test_order_properties: Verifies that the Order properties return the correct details.
Test_order_all_orders: Checks that the all_orders method returns the correct list of orders.

## Usage
To run the tests you should : Use pytest to run your tests: bash pytest 

## Setup/Installation Requirements
One would need either linux or wsl for window users
A copy of visual basic code installed
A github account
Open your terminal and go to the directory you wish to work from.
Go to the following url using ur github account 
Go to the code tab and clone the ssh key
Go back to the termina and type git clone <-followed by the ssh key you copied /cloned ->
Enter your new cloned repository and type in code .
On the visual studio code that has now opened, go to the the run tab and hit start debugging.
