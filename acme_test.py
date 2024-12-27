'''These are the modules we use for test our
code from acme and acme_report modules'''
from acme import Product
from acme_report import generate_products


def test_default_product_price():
    ''' Test default product price being 10'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_default_product_weight():
    ''' Test default product weight is 20'''
    prod = Product('Test Product')
    assert prod.weight == 20


def test_stealability_method():
    ''' Test return with default values for price and weight'''
    prod = Product('Test Product')
    assert prod.stealability() == 'Kinda stealable.'


def test_explode_method():
    ''' Test return with default values for flammability and weight'''
    prod = Product('Test Product')
    assert prod.explode() == '..boom!'


def test_generate_products():
    ''' Test return with default values a list with len == 30'''
    product_list = generate_products()
    assert len(product_list) == 30
