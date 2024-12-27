'''These imorted packages nessary for this module'''
import random
from acme import Product


ADJECTIVES = ['Awsome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguis', 'Mousetrap', '???']


def generate_products(num_products=30):
    ''' This function will produce nimbers of Product class objects'''
    product_list = []
    for i in range(num_products):
        adjective = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        name = adjective + ' ' + noun
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = round(random.uniform(0.0, 2.5), 2)
        product_list.append(Product(name, price, weight, flammability))

    return product_list


def inventory_report(product_list):
    '''This func uses the objects of func as it's argument'''
    unique_name = len({i.name for i in product_list})
    sum_price = sum(i.price for i in product_list)
    average_price = sum_price / len(product_list)
    sum_weight = sum(i.weight for i in product_list)
    average_weight = sum_weight / len(product_list)
    sum_flammability = sum(i.flammability for i in product_list)
    average_flammability = sum_flammability / len(product_list)

    return (unique_name, average_price, average_weight, average_flammability)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
