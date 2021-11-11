import json
from datetime import datetime


class Pizza:
    """Pizza class with getters, setters"""

    def __init__(self, name, price, ingredients):
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    # @property
    # def day(self):
    #     return self.__day
    #
    # @day.setter
    # def day(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("Wrong input type!")
    #     self.__day = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong input type!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong input type!")
        if value < 0:
            raise ValueError("Wrong input value!")
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, values):
        if not all([isinstance(ingredient, str) for ingredient in values]):
            raise TypeError("Wrong type of ingredient")
        self.__ingredients = values

    def __str__(self):
        return f'Pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class MondayPizza(Pizza):

    def __str__(self):
        return f'Monday\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class TuesdayPizza(Pizza):

    def __str__(self):
        return f'Tuesday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class WednesdayPizza(Pizza):
    def __str__(self):
        return f'Wednesday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class ThursdayPizza(Pizza):
    def __str__(self):
        return f'Thursday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class FridayPizza(Pizza):

    def __str__(self):
        return f'Friday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class SaturdayPizza(Pizza):
    def __str__(self):
        return f'Saturday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class SundayPizza(Pizza):
    def __str__(self):
        return f'Sunday:\n pizza: name {self.name}\n price: {self.price}, \n ' \
               f'ingredients: {self.ingredients}'


class Customer:
    """Customer class with getters and setters"""

    def __init__(self, surname, name):
        self.surname = surname
        self.name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of surname!")

        if len(value) <= 0:
            raise ValueError("Surname must not be empty")

        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of customer name")

        if len(value) <= 0:
            raise ValueError("Customer name must not be empty")

        self.__name = value


class Order:
    """Order class with add_product, del_product and sum_order methods"""

    ingredients = {'mozzarella': 20,
                   'ham': 40,
                   'bacon': 30,
                   'BBQ sauce': 10,
                   'tomato': 15}

    def __init__(self, new_customer=None, new_pizza=None):
        if not isinstance(new_customer, Customer):
            raise TypeError("Wrong type of customer")
        self.new_customer = new_customer

        if not isinstance(new_pizza, Pizza):
            raise TypeError("Wrong type of pizza")
        self.pizza = new_pizza

    def add_ingredients(self):
        print(self.ingredients)
        for item in self.ingredients:
            if input(f"Would you like to add {item} Y/N ?").lower() == "y":
                self.pizza.ingredients.append(item)
                self.pizza.price += self.ingredients[item]
        self.write_data()

    def write_data(self):
        data = {'customer name': self.new_customer.name,
                'day': datetime.today().strftime('%A'),
                'name': self.pizza.name,
                'price': self.pizza.price,
                'ingredients': self.ingredients
                }
        with open("order.json", "w") as write_file:
            json.dump(data, write_file)


def fabric():
    current_date = datetime.today().strftime('%A')

    if current_date == "Monday":
        return deserialization(MondayPizza)
    elif current_date == "Tuesday":
        return deserialization(TuesdayPizza)
    elif current_date == "Wednesday":
        return deserialization(WednesdayPizza)
    elif current_date == "Thursday":
        return deserialization(ThursdayPizza)
    elif current_date == "Friday":
        return deserialization(FridayPizza)
    elif current_date == "Saturday":
        return deserialization(SaturdayPizza)
    elif current_date == "Sunday":
        return deserialization(SundayPizza)


def deserialization(pizzarito):
    with open("pizza_of_the_day.json", 'r') as file:
        pizza_of_the_day = json.load(file)
    for pizza_toppings in pizza_of_the_day:
        if pizza_toppings["day"] == datetime.today().strftime('%A'):
            return pizzarito(pizza_toppings["name"], pizza_toppings["price"],
                             pizza_toppings["ingredients"])


customer = Customer("Shevchenko", "Vladyslav")
pizza = fabric()
print(pizza)
order = Order(customer, pizza)
order.add_ingredients()
