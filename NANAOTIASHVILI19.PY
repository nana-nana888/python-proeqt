import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

def serialize_products(products, filename):
    with open(filename, 'w') as file:
        json.dump([product.__dict__ for product in products], file, indent=4)

def deserialize_products(filename):
    with open(filename, 'r') as file:
        product_dicts = json.load(file)
        products = [Product(**product_dict) for product_dict in product_dicts]
    return products


products = [
    Product("Apple", 1.5, 10),
    Product("Banana", 0.9, 25),
    Product("Orange", 1.2, 30)
]

serialize_products(products, "products.json")


deserialized_products = deserialize_products("products.json")

for product in deserialized_products:
    print(product)
