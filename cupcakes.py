from abc import ABC, abstractmethod
import csv
from pprint import pprint

cupcakes = []

class Cupcake():
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling) -> None:
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for items in args:
            self.sprinkles.append(items)
    
    
    def calc_price(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = 'mini'

    def __init__(self, name, price, flavor, frosting) -> None:
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

class Regular(Cupcake):
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling) -> None:
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

def make_new_cupcake(file):
    number_of_sprinkles = 0
    sprinkles = []
    name = input('What is the name of the cupcake you would like to add?\n')
    price = float(input('What is the price of this cupcake?\n'))
    flavor = input('What flavor is this cupcake?\n')
    frosting = input('What is the frosting used on this cupcake?\n')
    filling = input('What filling is in the cupcake?\n')
    how_many = int(input('How many sprinkles do you want to add?\n'))
    while number_of_sprinkles < how_many:
        cupcake_sprinkles = input('What flavor of sprinkles does the cupcake have?\n')
        sprinkles.append(cupcake_sprinkles)
        number_of_sprinkles += 1
        

    new_cupcake = Regular(name, price, flavor, frosting, filling)
    new_cupcake.add_sprinkles(sprinkles)

    cupcakes.append(new_cupcake)

    print(cupcakes)

    with open(file, 'a', newline='\n') as csvfile:
        fieldnames = ['size','name','price','flavor','frosting','sprinkles','filling']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        if hasattr(new_cupcake, 'filling'):
            writer.writerow({'size': new_cupcake.size, 'name': new_cupcake.name, 'price': new_cupcake.price, 'flavor': new_cupcake.flavor, 'frosting': new_cupcake.frosting, 'filling': new_cupcake.filling, 'sprinkles': new_cupcake.sprinkles})
        else:    
             writer.writerow({'size': new_cupcake.size, 'name': new_cupcake.name, 'price': new_cupcake.price, 'flavor': new_cupcake.flavor, 'frosting': new_cupcake.frosting, 'sprinkles': new_cupcake.sprinkles})

    # with open('sample.csv') as csvfile:
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         pprint(row)

# def get_cupcakes(file, cupcakes):
#     with open(file, 'a', newline='\n') as csvfile:
#         fieldnames = ['size','name','price','flavor','frosting','sprinkles','filling']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()

#         for cupcake in cupcakes:
#             if hasattr(cupcake, 'filling'):
#                 writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'filling': cupcake.filling, 'sprinkles': cupcake.sprinkles})
#             else:    
#                 writer.writerow({'size': cupcake.size, 'name': cupcake.name, 'price': cupcake.price, 'flavor': cupcake.flavor, 'frosting': cupcake.frosting, 'sprinkles': cupcake.sprinkles})

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def add_individual_cupcake_dictionary(file, cupcake):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        str_writer = csv.writer(csvfile)
        str_writer.writerow(["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"])
        writer.writerow(cupcake)

def menu():
    user_input = int(input('What would you like to do?\n new cupcake -1\n cupcake menu - 2\n'))

    if user_input == 1:
        make_new_cupcake('sample.csv')
    elif user_input == 2:
        get_cupcakes('sample.csv', cupcakes)

if __name__ == '__main__':
    menu()