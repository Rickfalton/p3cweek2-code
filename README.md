## Coffee Order System
## Overview
This project models a simple coffee ordering system, featuring classes for customers, coffees, and orders.

## Classes
## Customer
Represents an individual customer who can place orders for coffee.

## Attributes:

name (str): Customer's name (1 to 15 characters).
_orders (list): List of orders placed by the customer.
## Methods:

orders(): Returns all orders placed by the customer.
coffees(): Returns a unique list of Coffee objects ordered by the customer.
create_order(coffee, price): Creates an order linked to a Coffee object and price, then adds it to the list of orders.

## Coffee
Represents a type of coffee that customers can order.

## Attributes:

name (str): Coffee name (minimum 3 characters).
_orders (list): List of orders for this coffee.
## Methods:

orders(): Returns all orders for this coffee.
customers(): Returns unique customers who have ordered this coffee.
num_orders(): Returns total number of times this coffee has been ordered.
average_price(): Calculates the average price for this coffee based on all orders (returns 0 if no orders exist).

## Order
Represents an individual order placed by a customer for a specific coffee.

## Attributes:

customer (Customer): Customer who placed the order.
coffee (Coffee): Type of coffee ordered.
price (float): Price of the order (must be between 1.0 and 10.0).

## Testing
This project uses the pytest framework to test the functionality of the classes.

## Test Cases
** Coffee Tests **

Name validation
Orders retrieval
Customers retrieval
Number of orders
Average price calculation

** Customer Tests **

Name validation
Order creation
Orders retrieval
Coffees retrieval
Most expensive order

** Order Tests **
Price validation
Property correctness
All orders retrieval

### Usage
To run the tests, navigate to your project directory and execute:
pytest

## Setup/Installation Requirements
** Environment **

Linux or WSL (for Windows users)
Visual Studio Code installed
A GitHub account

** Clone the Repository **

Open your terminal.
Navigate to your desired working directory.
Clone the repository using SSH:git@github.com:Rickfalton/p3cweek2-code.git
git clone git@github.com:Rickfalton/p3cweek2-code.git

** Open the Project **

Change into the cloned directory:
cd <repository-name>
Open the project in Visual Studio Code:

code .
** Run the Application **

In Visual Studio Code, go to the "Run" tab and click "Start Debugging."
